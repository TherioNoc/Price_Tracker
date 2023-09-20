# Price Tracker

A simple python code that fetches and tracks the real-time prices of various cryptocurrencies...

    
__Note:__ Before executing the code you need to install 2 libraries. You can install with the following python commands:

```
pip install requests
```

```
pip install time
```

In the example usage, we call the ```price_tracker``` function to track the price of Bitcoin (BTC) every 10 seconds. You can modify the cryptocurrency symbol and interval to suit your needs. The ``` fetch_price ``` function requests the cryptocurrency price using the CoinGecko API. It takes the crypto symbol (e.g., "bitcoin", "ethereum") as input and returns the price in USD.
