import json


def load_transaction(file_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
