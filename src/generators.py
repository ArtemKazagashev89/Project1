from typing import Generator, Any


def filter_by_currency(transactions, currency_code) -> Generator:
    """Фунуция возвращает транзакции по заданной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions) -> Generator:
    """Функция возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end) -> Generator:
    """Функция генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:]
