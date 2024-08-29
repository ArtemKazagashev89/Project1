import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_transaction(transaction: dict) -> float:
    """Функция конвертации"""
    amount = transaction["amount"]
    currency = transaction["currency"]
    if currency == "RUB":
        return amount
    elif currency in ["USD", "EUR"]:
        api_key = os.environ["API_KEY"]
        responce = requests.get(
            f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB&apikey={api_key}"
        )
        if responce.status_code == 200:
            data = responce.json()
            exchange_rate = data["rates"]["RUB"]
            return amount * exchange_rate
        else:
            raise Exception("Failed to retrieve exchange rate")
    else:
        raise Exception("Unsupported currency")
