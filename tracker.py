import requests
import time

def fetch_price(crypto):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data[crypto]["usd"]
        return price
    else:
        print("Error fetching price.")
        return None

def display_price(crypto, price):
    print(f"{crypto} Price: ${price}")

def price_tracker(crypto, interval):
    while True:
        price = fetch_price(crypto)
        if price:
            display_price(crypto, price)
        time.sleep(interval)

# Example usage: Tracking the price of Bitcoin (BTC) every 10 seconds :
price_tracker("bitcoin", 10)
