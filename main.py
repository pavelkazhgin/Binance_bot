import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv('./.env')

api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

print('THIS IS apikey', api_key)
print('THIS IS secret_key', secret_key)




client = Client(
    api_key,
    secret_key,
    testnet=True
)

tickers = client.get_all_tickers()
print(tickers)

# trades = client.get_historical_trades(symbol="BTCUSDT")
# print(trades)
