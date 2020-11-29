from src.environment import INPUT_DATA_GOUV_URL

from src.extract import extract
from src.load import load
from src.tools.db_creation import db_creation
from src.transform import transform


def etl_accident():
    for file in INPUT_DATA_GOUV_URL:
        year = file.get("year")
        print(year)
        dict = {}
        for input_url in file.get("urls"):
            url = input_url.get("url")
            type = input_url.get("type")

            data = extract(url, type)

            data = transform(data, type)

            dict[type] = data
        load(dict['vehicles'], dict['users'], dict['places'], dict['characteristics'])


if __name__ == "__main__":
    db_creation()
    etl_accident()
