import pandas as pd
import numpy as np
from datetime import datetime

# Read caracteristique csv
df = pd.read_csv(
    "./caracteristiques-2018.csv",
    encoding='latin-1'
)

df_s = pd.read_csv(
    "./caracteristiques-2017.csv",
    encoding='latin-1'
)

# Drop columns which will not be used
column_to_drop = [
    "Num_Acc","an",
    "mois","jour",
    "hrmn","agg",
    "lum","int",
    "col","com",
    "gps","dep",
    "atm"
]


df.drop(columns=column_to_drop, inplace=True)
df_s.drop(columns=column_to_drop, inplace=True)

auto_gen_id = 0

ids = []
ids_s = []

adrs = []
adrs_s = []

longs = []
longs_s = []

lats = []
lats_s = []

for i in df.index:
    adr = df["adr"][i]
    lat = df["long"][i]
    longi = df["lat"][i]

    if type(lat) is np.float64:
        lat = np.float(lat)
    
    if type(longi) is np.float64:
        longi = np.float(longi)

    adrs.append(adr)
    lats.append(lat)
    longs.append(longi)
    ids.append(auto_gen_id)
    auto_gen_id += 1

for i in df_s.index:
    adr = df_s["adr"][i]
    lat = df_s["long"][i]
    longi = df_s["lat"][i]

    if type(lat) is np.float64:
        lat = np.float(lat)
    
    if type(longi) is np.float64:
        longi = np.float(longi)

    adrs_s.append(adr)
    lats_s.append(lat)
    longs_s.append(longi)
    ids_s.append(auto_gen_id)
    auto_gen_id += 1


datas = {'id': ids,'adr': adrs,'lat': lats,'long' : longs}
res = pd.DataFrame(datas, columns= ['id','adr', 'lat','long'])

datas_s = {'id': ids_s,'adr': adrs_s,'lat': lats_s,'long' : longs_s}
res_s = pd.DataFrame(datas_s, columns= ['id','adr', 'lat','long'])

res.to_csv("./cleaned/location2018.csv", index=False)
res_s.to_csv("./cleaned/location2017.csv", index=False)

