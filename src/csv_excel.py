from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict]:

    """Считывает финансовые операции из CSV-файла."""

    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении файла CSV: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict]:

    """Считывает финансовые операции из Excel-файла."""

    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        return transactions
    except Exception as e:
        print(f"Ошибка при чтении файла Excel: {e}")
        return []
