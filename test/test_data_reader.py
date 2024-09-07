from unittest.mock import mock_open, patch

import pandas as pd

from src.data_reader import read_transactions_from_csv, read_transactions_from_excel


# Тест для функции считывания из CSV
def test_read_transactions_from_csv():
    mock_csv_data = "id,amount\n1,100\n2,150\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = read_transactions_from_csv("fake_path.csv")
        expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 150}]
        assert result == expected


# Тест для функции считывания из Excel
def test_read_transactions_from_excel():
    mock_excel_data = pd.DataFrame({"id": [1, 2], "amount": [100, 150]})

    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = mock_excel_data
        result = read_transactions_from_excel("fake_path.xlsx")
        expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 150}]
        assert result == expected
