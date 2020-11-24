
import pandas
from src.model import *

def load_dept():
    data = pandas.read_csv('intputs/departement2020.csv')
    for index, row in data.iterrows():
        print(f"id={row['dep']}, name={row['libelle']}")
        Department.create(id=row["dep"], name=row["libelle"])