import json
import requests
from config import *


class APIException(Exception):
    pass


class Converter:
    BASE_URL ='ttps://api.exchangeratesapi.io/latest'

    currencies = ['EUR', 'USD', 'RUB']

    @staticmethod
    def get_price(base: str, quote: str, amount: float):
        if base == quote:
            return amount

        if base not in Converter.currencies or quote not in Converter.currencies:
            raise APIException("Invalid currency name.")

        params = {'base': base, 'symbols': quote}
        response = requests.get(Converter.BASE_URL, params=params)

        if response.status_code != 200:
            raise APIException("Error: Failed to retrieve exchange rate information.")

        data = json.loads(response.text)

        rate = data['rates'].get(quote)

        if not rate:
            raise APIException("Error: Failed to retrieve exchange rate information.")

        return rate * amount
