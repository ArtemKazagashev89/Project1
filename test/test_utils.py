import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transaction


def test_load_transaction_success():
    # Тест на успешное чтение файла с корректным JSON
    mock_data = json.dumps([{"id": 1, "amount": 100}, {"id": 2, "amount": 150}])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transaction("fake_path.json")
        assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 150}]


def test_load_transaction_empty_file():
    # Тест на чтение пустого файла
    mock_data = json.dumps([])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transaction("fake_path.json")
        assert result == []


def test_load_transaction_invalid_json():
    # Тест на чтение файла с некорректным JSON
    mock_data = json.dumps({"id": 1, "amount": 100})  # не список
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = load_transaction("fake_path.json")
        assert result == []


def test_load_transaction_file_not_found():
    # Тест на обработку исключения FileNotFoundError
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_transaction("fake_path.json")
        assert result == []
