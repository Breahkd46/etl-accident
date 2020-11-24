DATABASE_NAME = "etl_accident"
DATABASE_USER = "root"
DATABASE_PASSWORD = "root"
DATABASE_HOST = "localhost"

INPUT_DATA_GOUV_URL = [
    {
        "year": 2018,
        "urls": [
            {
                "type": "vehicles",
                "url": "https://www.data.gouv.fr/fr/datasets/r/b4aaeede-1a80-4d76-8f97-543dad479167"
            },
            {
                "type": "users",
                "url": "https://www.data.gouv.fr/fr/datasets/r/72b251e1-d5e1-4c46-a1c2-c65f1b26549a"
            },
            {
                "type": "places",
                "url": "https://www.data.gouv.fr/fr/datasets/r/d9d65ca1-16a3-4ea3-b7c8-2412c92b69d9"
            },
            {
                "type": "characteristics",
                "url": "https://www.data.gouv.fr/fr/datasets/r/6eee0852-cbd7-447e-bd70-37c433029405"
            }
        ]
    },
    {
        "year": 2017,
        "urls": [
            {
                "type": "vehicles",
                "url": "https://www.data.gouv.fr/fr/datasets/r/d6103d0c-6db5-466f-b724-91cbea521533"
            }, {
                "type": "users",
                "url": "https://www.data.gouv.fr/fr/datasets/r/07bfe612-0ad9-48ef-92d3-f5466f8465fe"
            }, {
                "type": "places",
                "url": "https://www.data.gouv.fr/fr/datasets/r/9b76a7b6-3eef-4864-b2da-1834417e305c"
            }, {
                "type": "characteristics",
                "url": "https://www.data.gouv.fr/fr/datasets/r/9a7d408b-dd72-4959-ae7d-c854ec505354"
            }
        ]
    }
]

HEADER_VEHICLES = ['Num_Acc', 'senc', 'catv', 'occutc', 'obs', 'obsm', 'choc', 'manv', 'num_veh']
HEADER_USERS = ['Num_Acc', 'place', 'catu', 'grav', 'sexe', 'trajet', 'secu', 'locp', 'actp', 'etatp', 'an_nais', 'num_veh']
HEADER_PLACES = ['Num_Acc', 'catr', 'voie', 'v1', 'v2', 'circ', 'nbv', 'pr', 'pr1', 'vosp', 'prof', 'plan', 'lartpc',
               'larrout', 'surf', 'infra', 'situ', 'env1']

HEADER_CHARACTERISTICS = ['Num_Acc', 'an', 'mois', 'jour', 'hrmn', 'lum', 'agg', 'int', 'atm', 'col', 'com', 'adr', 'gps',
                       'lat', 'long', 'dep']

HEADERS = {
    "vehicles": HEADER_VEHICLES,
    "users": HEADER_USERS,
    "places": HEADER_PLACES,
    "characteristics": HEADER_CHARACTERISTICS
}