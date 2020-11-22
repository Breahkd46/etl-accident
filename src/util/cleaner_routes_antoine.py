import pandas as pd
import numpy as np
import math

# Read accidents csv
df = pd.read_csv(
    "C:\\Users\\AdminEtu\\Desktop\\Antoine\\M2ICE\\Decisionnel\\Projet\\lieux-2018.csv",
    encoding='latin-1',
    low_memory=False
)

# Drop columns which will not be used
fields_to_drop = [
    "v1",
    "v2",
    "nbv",
    "vosp",
    "pr",
    "pr1",
    "lartpc",
    "larrout",
    "env1"
]

df.drop(columns=fields_to_drop, inplace=True)

# Check all fields with errors
catrs = []
circs = []
plans = []
voies = []
profs = []
surfs = []
infras = []
for i in df.index:

    # catr errors handling
    catr = df["catr"][i]
    if math.isnan(catr):
        catr = 0
    elif type(catr) is np.int64:
        pass
    elif type(catr) is np.float64:
        catr = np.intc(catr)
    elif catr > 6 and catr < 9:
        catr = 0
    else:
        catr = 0
    catrs.append(catr)
    
    # circ errors handling
    circ = df["circ"][i]
    if math.isnan(circ):
        circ = 0
    elif type(circ) is np.int64:
        pass
    elif type(circ) is np.float64:
        circ = np.intc(circ)
    else:
        circ = 0
    circs.append(circ)

    # plan errors handling
    plan = df["plan"][i]
    if math.isnan(plan):
        plan = 0
    elif type(plan) is np.int64:
        pass
    elif type(plan) is np.float64:
        plan = np.intc(plan)
    else:
        plan = 0
    plans.append(plan)

    # voie errors handling
    voie = str(df["voie"][i])
    if not voie.strip() or voie == "nan":
        voie = 0
    voies.append(voie)

    # prof errors handling
    prof = df["prof"][i]
    if math.isnan(prof):
        prof = 0
    elif type(prof) is np.int64:
        pass
    elif type(prof) is np.float64:
        prof = np.intc(prof)
    else:
        prof = 0
    profs.append(prof)

    # surf errors handling
    surf = df["surf"][i]
    if math.isnan(surf):
        surf = 0
    elif type(surf) is np.int64:
        pass
    elif type(surf) is np.float64:
        surf = np.intc(surf)
    else:
        surf = 0
    surfs.append(surf)

    # infra errors handling
    infra = df["infra"][i]
    if math.isnan(infra):
        infra = 0
    elif type(infra) is np.int64:
        pass
    elif type(infra) is np.float64:
        infra = np.intc(infra)
    else:
        infra = 0
    infras.append(infra)


df["catr"] = catrs
df["circ"] = circs
df["plan"] = plans
df["voie"] = voies
df["prof"] = profs
df["surf"] = surfs
df["infra"] = infras

res = df.rename(columns={"Num_Acc": "numacc"})

res.to_csv("C:\\Users\\AdminEtu\\Desktop\\Antoine\\M2ICE\\Decisionnel\\Projet\\bdd\\output\\routes-2018.csv", index=False)
