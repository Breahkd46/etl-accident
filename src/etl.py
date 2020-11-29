import csv
import pandas
import requests

from src.db_creation import db_creation
from src.environment import *
from src.formater import *
from src.model import *

from sqlalchemy import create_engine


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

    data.rename(columns={'Num_Acc': 'num_acc', 'catv': 'codevehtype'}, inplace=True)

    data["num_acc"] = data["num_acc"].apply(formater_Num_Acc)
    data["codevehtype"] = data["codevehtype"].apply(formater_catv)

    # Filter
    data_out = data[(data['num_acc'] != 0)]
    return data_out


def transform_users(data):
    print("transform users")
    column_to_save = ['Num_Acc', 'place', 'catu', 'grav', 'sexe', 'an_nais']
    column_to_drop = [ele for ele in HEADER_USERS if ele not in column_to_save]

    data.drop(columns=column_to_drop, inplace=True)

    data.rename(columns={'Num_Acc': 'num_acc',
                         'catu': 'user_category',
                         'grav': 'gravity',
                         'sexe': 'sex',
                         'an_nais': 'birth_year'}, inplace=True)

    data["num_acc"] = data["num_acc"].apply(formater_Num_Acc)
    data["place"] = data["place"].apply(formater_place)
    data["user_category"] = data["user_category"].apply(formater_catu)
    data["gravity"] = data["gravity"].apply(formater_grav)
    data["sex"] = data["sex"].apply(formater_sexe)
    data["birth_year"] = data["birth_year"].apply(formater_an)

    # Filter
    data_out = data[(data['num_acc'] != 0)]
    return data_out


def transform_places(data):
    print("transform places")
    column_to_save = ['Num_Acc', 'surf']
    column_to_drop = [ele for ele in HEADER_PLACES if ele not in column_to_save]

    data.drop(columns=column_to_drop, inplace=True)

    data.rename(columns={'Num_Acc': 'num_acc',
                         'surf': 'surface'}, inplace=True)

    data["num_acc"] = data["num_acc"].apply(formater_Num_Acc)
    data["surface"] = data["surface"].apply(formater_surf)

    # Filter
    data_out = data[(data['num_acc'] != 0)]
    return data_out


def transform_characteristics(data):
    print("transform characteristics")

    column_to_save = ['Num_Acc', 'an', 'lum', 'atm', 'lat', 'long', 'dep']
    column_to_drop = [ele for ele in HEADER_CHARACTERISTICS if ele not in column_to_save]

    data.drop(columns=column_to_drop, inplace=True)

    data.rename(columns={'Num_Acc': 'num_acc',
                         'an': 'year',
                         'dep': 'dept'}, inplace=True)

    data["num_acc"] = data["num_acc"].apply(formater_Num_Acc)
    data["year"] = data["year"].apply(formater_an)
    data["lum"] = data["lum"].apply(formater_lum)
    data["atm"] = data["atm"].apply(formater_atm)
    data["lat"] = data["lat"].apply(formater_lat)
    data["long"] = data["long"].apply(formater_lat)
    data["dept"] = data["dept"].apply(formater_dept)

    # Filter
    data_out = data[(data['num_acc'] != 0)]
    return data_out


def loader(vehicles, users, places, characteristics):
    print("Transform ALL")

    location = characteristics.drop(columns=['year', 'lum', 'atm'])
    weathercondition = characteristics.drop(columns=['year', 'lum', 'lat', 'long', 'dept']) \
        .join(places.set_index('num_acc'), on='num_acc')
    accident = characteristics.drop(columns=['atm', 'lat', 'long', 'dept'])
    accident_vehtype = vehicles
    usertype = users

    print("accident")
    load_to_postgresql(accident, "accident")

    print("location")
    load_to_postgresql(location, "location")

    print("weathercondition")
    load_to_postgresql(weathercondition, "weathercondition")

    print("accident_vehtype")
    load_to_postgresql(accident_vehtype, "accident_vehtype")

    print("usertype")
    load_to_postgresql(usertype, "usertype")


def load_to_postgresql(data, table):
    alchemyEngine = create_engine(
        f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}",
        pool_recycle=3600)

    postgreSQLConnection = alchemyEngine.connect()

    try:
        frame = data.to_sql(table, postgreSQLConnection, if_exists='append', index=False)
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("PostgreSQL Table %s has been created successfully." % table)
    finally:
        postgreSQLConnection.close()


def etl_accident():
    for input in INPUT_DATA_GOUV_URL:
        year = input.get("year")
        print(year)
        dict = {}
        for input_url in input.get("urls"):
            url = input_url.get("url")
            type = input_url.get("type")

            data = extract(url, type)

            data = transform(data, type)

            dict[type] = data
        loader(dict['vehicles'], dict['users'], dict['places'], dict['characteristics'])


if __name__ == "__main__":
    db_creation()
    etl_accident()
