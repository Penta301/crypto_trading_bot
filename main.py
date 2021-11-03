API_KEY = 'O3yy0kaccrldEZraeMCWTmeTGP4jATej5mXYd85erfuf6EIly4B8Twul5d4RVx8i'
SECRET_KEY = 'y4yKxq2eWhvLOyOpcIqW8uMXaMWC3A3pC03dAn4kgEAzaLYk0XOOnthO4bFvl6Oj'

import requests
from binance.spot import Spot 
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client
import time

symbol = input('Insert the symbol: ').upper()
spot_client = Client()
spot_client.start()

def get_klines(symbol, interval):
    disconnect = False

    def message_handler(message):
        market = message.get('k')
        if market:
            close_price = market.get('c')
            high_price = market.get('h')
            low_price = market.get('l')

            print('The close price is: ', close_price)
            print('The high price is: ', high_price)
            print('The low price is: ', low_price)

        time.sleep(5)

    spot_client.kline(symbol=f'{symbol}USDT', id=1, interval=interval, callback=message_handler)

    if disconnect:
        spot_client.stop()

def get_price():

    response = spot_client.avg_price(f'{symbol}USDT')
    static_price = float(response['price'])

    two_dot_five_percentage = static_price * 0.5 / 100
    one_dot_pive_percentage = static_price * 1.5 / 100

    objective = static_price + two_dot_five_percentage
    margin_risk = static_price - one_dot_pive_percentage

    while True:
        update_response = spot_client.avg_price(f'{symbol}USDT')
        price = float(update_response['price'])


        if price >= objective:
            print('objective reached', price)
            break

        if price <= margin_risk:
            print('margin reached', price)
            break

        print(price)
        print('this is the objective',objective)
        print('this is the margin',margin_risk)

        time.sleep(0.5)

get_klines(symbol, '1m')
