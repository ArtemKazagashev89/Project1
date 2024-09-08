import pytest
import json
import os
from src.utils import get_transactions_info_json


@pytest.fixture
def create_temp_json_file(tmp_path):
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    json_file = tmp_path / "test_operations.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return json_file


def test_get_transactions_info_json_valid(create_temp_json_file):
    result = get_transactions_info_json(str(create_temp_json_file))
    expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    assert result == expected


def test_get_transactions_info_json_empty_file(tmp_path):
    empty_file = tmp_path / "empty.json"
    with open(empty_file, "w", encoding="utf-8") as f:
        f.write("")
    result = get_transactions_info_json(str(empty_file))
    assert result == []


def test_get_transactions_info_json_invalid_file(tmp_path):
    invalid_file = tmp_path / "invalid.json"
    with open(invalid_file, "w", encoding="utf-8") as f:
        f.write("Not a JSON")
    result = get_transactions_info_json(str(invalid_file))
    assert result == []
