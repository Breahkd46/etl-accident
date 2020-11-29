import csv
import pandas
import requests

def extract(url, type):
    print(f"Fetch for {type} at : {url}")

    with requests.Session() as s:
        download = s.get(url)

        decoded_content = download.content.decode('ISO-8859-1')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        output = pandas.DataFrame(list(cr), columns=HEADERS.get(type))
        output.drop([0], inplace=True)
        return output