import csv
import pandas
import requests

from src import environment


def fetch_csv(url, type):
    print(f"Fetch for {type} at : {url}")

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('ISO-8859-1')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return pandas.DataFrame(list(cr), columns=environment.HEADERS.get(type))


def extract():
    for input in environment.INPUT_DATA_GOUV_URL:
        year = input.get("year")
        print(year)
        for input_url in input.get("urls"):
            data = fetch_csv(input_url.get("url"), input_url.get("type"))
            print(type(data))
            print(data)


if __name__ == "__main__":
    extract()
