import re
from collections import Counter


def search_transactions(transactions, search_string):
    """Функция"""
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction["description"])]


def count_transaction_types(transactions, categories):
    """Функция"""
    count_categories = Counter(transaction["category"] for transaction in transactions)
    return dict(count_categories)
