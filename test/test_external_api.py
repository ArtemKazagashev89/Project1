import os
from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_transaction


def test_convert_transaction_rub():
    # Тестирование преобразования в RUB
    transaction = {"amount": 100, "currency": "RUB"}
    result = convert_transaction(transaction)
    assert result == 100


def test_convert_transaction_usd_success():
    # Тестирование преобразования из USD в RUB с успешным запросом
    transaction = {"amount": 100, "currency": "USD"}

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}

    with patch("requests.get", return_value=mock_response):
        os.environ["API_KEY"] = "test_api_key"  # Установите временный API ключ
        result = convert_transaction(transaction)
        assert result == 7500.0  # 100 USD * 75 RUB/USD


def test_convert_transaction_eur_success():
    # Тестирование преобразования из EUR в RUB с успешным запросом
    transaction = {"amount": 100, "currency": "EUR"}

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 90.0}}

    with patch("requests.get", return_value=mock_response):
        os.environ["API_KEY"] = "test_api_key"  # Установите временный API ключ
        result = convert_transaction(transaction)
        assert result == 9000.0  # 100 EUR * 90 RUB/EUR


def test_convert_transaction_usd_failure():
    # Тестирование ситуации, когда API вернул ошибку
    transaction = {"amount": 100, "currency": "USD"}

    mock_response = Mock()
    mock_response.status_code = 500  # Симуляция ошибки сервера

    with patch("requests.get", return_value=mock_response):
        os.environ["API_KEY"] = "test_api_key"  # Установите временный API ключ
        with pytest.raises(Exception, match="Failed to retrieve exchange rate"):
            convert_transaction(transaction)


def test_convert_transaction_unsupported_currency():
    # Тестирование ситуации с неподдерживаемой валютой
    transaction = {"amount": 100, "currency": "GBP"}

    with pytest.raises(Exception, match="Unsupported currency"):
        convert_transaction(transaction)
