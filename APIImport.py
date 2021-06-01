import requests

request=requests.get('https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=EUR&apikey=R73DEFZ9W84OJYY8')
print(request.status_code)
print(request.text)

data=request.json()

print(data['Meta Data'])
