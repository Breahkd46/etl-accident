import pandas as pd
import numpy as np
from datetime import datetime

# Read caracteristique csv
df = pd.read_csv(
    "./usagers-2018.csv",
    encoding='latin-1'
)

df_s = pd.read_csv(
    "./usagers-2017.csv",
    encoding='latin-1'
)

# Drop columns which will not be used
column_to_drop = [
    "Num_Acc",
    "trajet","secu",
    "locp","actp",
    "etatp","num_veh",
]

df.drop(columns=column_to_drop, inplace=True)
df_s.drop(columns=column_to_drop, inplace=True)

sexes = []
places = []
gravs = []
naiss = []
catus = []

sexes_s = []
places_s = []
gravs_s= []
naiss_s = []
catus_s = []

for i in df.index:
    sexe = df["sexe"][i]
    place = df["place"][i]
    grav = df["grav"][i]
    nais = df["an_nais"][i]
    catu = df["catu"][i]

    if type(sexe) is np.int64:
        sexe = np.intc(sexe)

    if type(catu) is np.int64:
        catu = np.intc(catu)

    if type(nais) is np.float64:
        nais = np.intc(nais)

    if type(place) is np.float64:
        place = np.intc(place)
    
    if type(grav) is np.int64:
        grav = np.intc(grav)

    sexes.append(sexe)
    naiss.append(nais)
    places.append(place)
    gravs.append(grav)
    catus.append(catu)

for i in df_s.index:
    sexe = df_s["sexe"][i]
    place = df_s["place"][i]
    grav = df_s["grav"][i]
    nais = df_s["an_nais"][i]
    catu = df_s["catu"][i]

    if type(sexe) is np.int64:
        sexe = np.intc(sexe)

    if type(catu) is np.int64:
        catu = np.intc(catu)

    if type(nais) is np.float64:
        nais = np.intc(nais)

    if type(place) is np.float64:
        place = np.intc(place)
    
    if type(grav) is np.int64:
        grav = np.intc(grav)

    sexes_s.append(sexe)
    naiss_s.append(nais)
    places_s.append(place)
    gravs_s.append(grav)
    catus_s.append(catu)

df["place"] = places
df["sexe"] = sexes
df["grav"] = gravs
df["an_nais"] = naiss
df["catu"] = catus

df_s["place"] = places_s
df_s["sexe"] = sexes_s
df_s["grav"] = gravs_s
df_s["an_nais"] = naiss_s
df_s["catu"] = catus_s

res = df.rename(columns={"grav": "gravity",
                         "sexe": "sex",
                         "place": "place",
                         "an_nais":"birth_year",
                         "catu":"user_category"})

res_s = df_s.rename(columns={"grav": "gravity",
                         "sexe": "sex",
                         "place": "place",
                         "an_nais":"birth_year",
                         "catu":"user_category"})

res.to_csv("./cleaned/user_type2018.csv", index=False)
res_s.to_csv("./cleaned/user_type2017.csv", index=False)