import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("string, expected_result", [
    ("7158300734726758", "7158 30** **** 6758"),
    ("7158300734726759", "7158 30** **** 6759"),
])
def test_get_mask_card_number(string, expected_result):
    assert get_mask_card_number(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [
    ("12345678901234567340", "** 7340"),
    ("12345678901234567890", "** 7890"),
])
def test_get_mask_account(string, expected_result):
    assert get_mask_account(string) == expected_result
