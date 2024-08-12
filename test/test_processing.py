import pytest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4, "state": "PENDING"},
    ]

    # Тестируем фильтрацию по состоянию "EXECUTED"
    result = filter_by_state(data, "EXECUTED")
    expected = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    assert result == expected

    # Тестируем фильтрацию по состоянию "CANCELED"
    result = filter_by_state(data, "CANCELED")
    expected = [
        {"id": 2, "state": "CANCELED"},
    ]
    assert result == expected

    # Тестируем фильтрацию по состоянию, которого нет в данных
    result = filter_by_state(data, "COMPLETED")
    expected = []
    assert result == expected

    # Тестируем фильтрацию без указания состояния (по умолчанию "EXECUTED")
    result = filter_by_state(data)
    expected = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 3, "state": "EXECUTED"},
    ]
    assert result == expected

# Тесты для sort_by_date
def test_sort_by_date_ascending():
    data = [
        {"date": "2023-01-03", "state": "EXECUTED"},
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "PENDING"},
    ]
    expected = [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "PENDING"},
        {"date": "2023-01-03", "state": "EXECUTED"},
    ]
    result = sort_by_date(data, reverse_list=False)
    assert result == expected

def test_sort_by_date_descending():
    data = [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "PENDING"},
        {"date": "2023-01-03", "state": "EXECUTED"},
    ]
    expected = [
        {"date": "2023-01-03", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "PENDING"},
        {"date": "2023-01-01", "state": "EXECUTED"},
    ]
    result = sort_by_date(data)
    assert result == expected

def test_sort_by_date_same_dates():
    data = [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-01", "state": "PENDING"},
        {"date": "2023-01-02", "state": "EXECUTED"},
    ]
    expected = [
        {"date": "2023-01-02", "state": "EXECUTED"},
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-01", "state": "PENDING"},
    ]
    result = sort_by_date(data)
    assert result == expected

