from src.environment import HEADER_VEHICLES, HEADER_USERS, HEADER_PLACES, HEADER_CHARACTERISTICS
from src.tools.formater import *


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