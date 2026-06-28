import requests


url = 'https://apiv2.nobitex.ir/v3/orderbook/USDTIRT'
response = requests.get(url)

print(response)
print(response.json())

print(response.json().get('lastTradePrice'))



# web scraping

