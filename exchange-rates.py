
import requests
import datetime

dates = [
"12/02/2021",
"25/03/2021",
"23/04/2021",
"31/05/2021",
"08/07/2021",
"19/08/2021",
"28/10/2021"]

dateFormatFromCsv = '%d/%m/%Y';
currency = 'EUR'

for purchaseDate in dates:
	while (True):
		dateBefore = (datetime.datetime.strptime(purchaseDate, dateFormatFromCsv) - datetime.timedelta(days=1))
		dayBeforeFormatted = dateBefore.strftime('%Y-%m-%d')
		purchaseDate = dateBefore.strftime(dateFormatFromCsv)
		
		basicUrl = 'https://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}'
		url = basicUrl.format(currency = currency, date = dayBeforeFormatted)
		params = {'format':"json"}
		  
		# sending get request and saving the response as response object
		r = requests.get(url = url, params = params)
		if(r.status_code != 404):
			data = r.json()
			rates = data['rates'][0]['mid']
			print(rates)
			break;   
		
		# extracting data in json format
		