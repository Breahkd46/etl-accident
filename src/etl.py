import csv
import pandas
import requests

from src.environment import *
from src.formater import *
from src.model import *


def extract(url, type):
    print(f"Fetch for {type} at : {url}")

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('ISO-8859-1')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        output = pandas.DataFrame(list(cr), columns=HEADERS.get(type))
        output.drop([0], inplace=True)
        return output


def transform(input, type):
    if type == "vehicles":
        return transform_vehicles(input)
    elif type == "users":
        return transform_users(input)
    elif type == "places":
        return transform_places(input)
    elif type == "characteristics":
        return transform_characteristics(input)
    else:
        print(f"no type defined for : {type}")
        return


def transform_vehicles(data):
    print("transform vehicles")
    column_to_save = ["Num_Acc", "catv"]
    column_to_drop = [ele for ele in HEADER_VEHICLES if ele not in column_to_save]

    data.drop(columns=column_to_drop, inplace=True)

    data["Num_Acc"] = data["Num_Acc"].apply(formater_Num_Acc)
    data["catv"] = data["catv"].apply(formater_catv)
    return data


def transform_users(data):
    print("transform users")
    column_to_save = ['Num_Acc', 'place', 'catu', 'grav', 'sexe', 'an_nais']
    column_to_drop = [ele for ele in HEADER_USERS if ele not in column_to_save]

    data.drop(columns=column_to_drop, inplace=True)

    data["Num_Acc"] = data["Num_Acc"].apply(formater_Num_Acc)
    data["place"] = data["place"].apply(formater_place)
    data["catu"] = data["catu"].apply(formater_catu)
    data["grav"] = data["grav"].apply(formater_grav)
    data["sexe"] = data["sexe"].apply(formater_sexe)
    data["an_nais"] = data["an_nais"].apply(formater_an)
    return data


def transform_places(data):
    print("transform places")
    column_to_save = ['Num_Acc', 'surf']
    column_to_drop = [ele for ele in HEADER_PLACES if ele not in column_to_save]

    data.drop(columns=column_to_drop, inplace=True)

    data["Num_Acc"] = data["Num_Acc"].apply(formater_Num_Acc)
    data["surf"] = data["surf"].apply(formater_surf)

    return data


def transform_characteristics(data):
    print("transform characteristics")

    column_to_save = ['Num_Acc', 'an', 'lum', 'atm', 'lat', 'long', 'dep']
    column_to_drop = [ele for ele in HEADER_CHARACTERISTICS if ele not in column_to_save]

    data.drop(columns=column_to_drop, inplace=True)

    data["Num_Acc"] = data["Num_Acc"].apply(formater_Num_Acc)
    data["an"] = data["an"].apply(formater_an)
    data["lum"] = data["lum"].apply(formater_lum)
    data["atm"] = data["atm"].apply(formater_atm)
    data["lat"] = data["lat"].apply(formater_lat)
    data["long"] = data["long"].apply(formater_lat)
    data["dep"] = data["dep"].apply(formater_dept)

    return data


def load(input, type):
    if type == "vehicles":
        load_vehicles(input)
    elif type == "users":
        load_users(input)
    elif type == "places":
        load_places(input)
    elif type == "characteristics":
        load_characteristics(input)
    else:
        print(f"no type defined for : {type}")


def load_vehicles(data):
    print("load vehicles")
    # print(data)
    for index, row in data.iterrows():
        # print(f"row : {row['Num_Acc']}")
        accident, created = Accident.get_or_create(num_acc=row["Num_Acc"])
        accident.veh_type = row["catv"]
        accident.save()
        if index > 100:
            break
    print("END LOAD vehicles")

def load_users(data):
    print("load users")
    # print(data)
    # ['Num_Acc', 'place', 'catu', 'grav', 'sexe', 'an_nais']

    for index, row in data.iterrows():
        # print(f"row : {row['Num_Acc']}")
        accident, created = Accident.get_or_create(num_acc=row["Num_Acc"])
        user_type, uCreated = UserType.get_or_create(place=row["place"],
                                           user_category=row["catu"],
                                           gravity=row["grav"],
                                           sex=row["sexe"],
                                           birth_year=row["an_nais"]
                                           )
        accident.user_type = user_type.id
        accident.save()
        if index > 100:
            break
    print("END LOAD users")


def load_places(data):
    print("load places")

    # ['Num_Acc', 'surf']

    for index, row in data.iterrows():
        # print(f"row : {row['Num_Acc']}")
        accident, created = Accident.get_or_create(num_acc=row["Num_Acc"])
        try:
            weather_cond = WeatherCondition.get(id=accident.weather_cond)
            weather_cond.surface = row["surf"]
            weather_cond.save()
        except DoesNotExist:
            weather_cond = WeatherCondition.create(surface=row["surf"])
            accident.weather_cond = weather_cond.id
            accident.save()

        if index > 100:
            break
    print("END LOAD places")


def load_characteristics(data):
    print("load characteristics")

    # ['Num_Acc', 'an', 'lum', 'atm', 'lat', 'long', 'dep']

    for index, row in data.iterrows():
        # print(f"row : {row['Num_Acc']}")
        # print(f"Dept {row['dep']}")
        accident, created = Accident.get_or_create(num_acc=row["Num_Acc"])
        if accident.weather_cond is not None:
            weather_cond = WeatherCondition.get(id=accident.weather_cond)
            weather_cond.atm = row["atm"]
            weather_cond.save()
        else:
            weather_cond = WeatherCondition.create(surface=row["atm"])
            accident.weather_cond = weather_cond.id

        accident.year = row["an"]
        accident.lum = row["lum"]

        location, created = Location.get_or_create(dept=row["dep"], lat=row["lat"], long=row["long"])
        accident.location = location.id
        accident.save()
        if index > 100:
            break
    print("END LOAD characteristics")


if __name__ == "__main__":
    for input in INPUT_DATA_GOUV_URL:
        year = input.get("year")
        print(year)
        for input_url in input.get("urls"):
            url = input_url.get("url")
            type = input_url.get("type")

            data = extract(url, type)

            data = transform(data, type)

            load(data, type)
