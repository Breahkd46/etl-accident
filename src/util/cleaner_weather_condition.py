import pandas as pd
import numpy as np
from datetime import datetime

# Read caracteristique csv
df = pd.read_csv(
    "./caracteristiques-2018.csv",
    encoding='latin-1'
)
df_lieux = pd.read_csv(
    "./lieux-2018.csv",
    encoding='latin-1'
)

df_s = pd.read_csv(
    "./caracteristiques-2017.csv",
    encoding='latin-1'
)
df_lieux_s = pd.read_csv(
    "./lieux-2017.csv",
    encoding='latin-1'
)


# df_s = pd.read_csv(
#     "./usagers-2017.csv",
#     encoding='latin-1'
# )

# Drop columns which will not be used
column_to_drop = [
    "Num_Acc","an",
    "mois","jour",
    "hrmn","agg",
    "lum","int",
    "col","com",
    "adr","gps",
    "lat","long",
    "dep"
]

column_to_drop_lieux = [
    "Num_Acc","catr",
    "voie","v1",
    "v2","circ",
    "nbv","pr",
    "pr1","vosp",
    "prof","plan",
    "lartpc","larrout",
    "infra","situ",
    "env1"
]

df.drop(columns=column_to_drop, inplace=True)
df_lieux.drop(columns=column_to_drop_lieux, inplace=True)

df_s.drop(columns=column_to_drop, inplace=True)
df_lieux_s.drop(columns=column_to_drop_lieux, inplace=True)


auto_gen_id = 0

ids = []
ids_s = []

atms = []
atms_s = []

surfs = []
surfs_s = []

for i in df.index:
    atm = df["atm"][i]

    if type(atm) is np.float64:
        atm = np.intc(atm)

    atms.append(atm)
    ids.append(auto_gen_id)
    auto_gen_id += 1

for i in df_s.index:
    atm = df_s["atm"][i]

    if type(atm) is np.float64:
        atm = np.intc(atm)

    atms_s.append(atm)
    ids_s.append(auto_gen_id)
    auto_gen_id += 1

for i in df_lieux.index:
    surf = df_lieux["surf"][i]

    if type(surf) is np.float64:
        surf = np.intc(surf)

    if np.intc(surf) == -2147483648: 
        surf = -1

    surfs.append(surf)

for i in df_lieux_s.index:
    surf = df_lieux_s["surf"][i]

    if type(surf) is np.float64:
        surf = np.intc(surf)

    if np.intc(surf) == -2147483648: 
        surf = -1

    surfs_s.append(surf)



datas = {'id': ids,'atm': atms,'surface': surfs}
res = pd.DataFrame(datas, columns= ['id','atm', 'surface'])

datas_s = {'id': ids_s,'atm': atms_s,'surface': surfs_s}
res_s = pd.DataFrame(datas_s, columns= ['id','atm', 'surface'])

res.to_csv("./cleaned/weather_condition2018.csv", index=False)
res_s.to_csv("./cleaned/weather_condition2017.csv", index=False)
