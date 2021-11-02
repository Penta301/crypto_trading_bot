API_KEY = 'O3yy0kaccrldEZraeMCWTmeTGP4jATej5mXYd85erfuf6EIly4B8Twul5d4RVx8i'
SECRET_KEY = 'y4yKxq2eWhvLOyOpcIqW8uMXaMWC3A3pC03dAn4kgEAzaLYk0XOOnthO4bFvl6Oj'

import requests
from binance.spot import Spot as Client 
import time


def get_price():
    spot_client = Client(key=API_KEY, secret=SECRET_KEY)

    symbol = input('Insert the symbol: ').upper()

    response = spot_client.avg_price(f'{symbol}USDT')
    static_price = float(response['price'])

    two_dot_five_percentage = static_price * 2.5 / 100
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

        time.sleep(5)

# def get_average(symbol, interval):
#     response = spot_client.klines(f'{symbol}USDT', interval)


get_price()