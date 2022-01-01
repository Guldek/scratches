import requests
import datetime
from pathlib import Path
import csv

dates = []

dateFormatFromCsv = '%d/%m/%Y'
currency = 'EUR'

fileWithPurchasesDates = Path("C:/Users/.Michal/Desktop/ideas.csv")

with open(fileWithPurchasesDates, 'rt') as file:
    csv_file_content = csv.reader(file)
    for date in csv_file_content:
        dates.append(date)

for purchaseDate in dates:
    while True:
        dateBefore = (datetime.datetime.strptime(purchaseDate, dateFormatFromCsv) - datetime.timedelta(days=1))
        dayBeforeFormatted = dateBefore.strftime('%Y-%m-%d')
        purchaseDate = dateBefore.strftime(dateFormatFromCsv)

        basicUrl = 'https://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}'
        url = basicUrl.format(currency=currency, date=dayBeforeFormatted)
        params = {'format': "json"}

        r = requests.get(url=url, params=params)
        if r.status_code != 404:
            data = r.json()
            rates = data['rates'][0]['mid']
            print(rates)
            break

