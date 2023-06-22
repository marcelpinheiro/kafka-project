import requests

# Coinbase API URL for Bitcoin price
api_url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

def get_bitcoin_price():
    response = requests.get(api_url)
    data = response.json()

    if 'data' in data and 'amount' in data['data']:
        return data['data']['amount']
    else:
        return None

# Retrieve and print the latest Bitcoin price
bitcoin_price = get_bitcoin_price()
if bitcoin_price:
    print(f"Latest Bitcoin Price: {bitcoin_price} USD")
else:
    print("Failed to retrieve Bitcoin price.")
