import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_number, expected_output",
    [
        ("Счет 72645194281643232984", "Счет ** 2984"),
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("Master 9876543210987654", "Master 9876 54** **** 7654"),
    ],
)
def test_mask_account_card_valid(input_number, expected_output):
    assert mask_account_card(input_number) == expected_output


def test_mask_account_card_invalid():
    assert mask_account_card("Некорректный ввод") == "Некорректный ввод"


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2023-10-15", "15.10.2023"),
        ("2021-01-01", "01.01.2021"),
        ("2000-12-31", "31.12.2000"),
    ],
)
def test_get_date_valid(input_date, expected_output):
    assert get_date(input_date) == expected_output


def test_get_date_valid():
    assert get_date("2023-10-05") == "05.10.2023"
    assert get_date("2000-01-01") == "01.01.2000"
    assert get_date("1999-12-31") == "31.12.1999"


def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        get_date("05-10-2023")  # Неверный формат
    with pytest.raises(ValueError):
        get_date("2023/10/05")  # Неверный формат


def test_get_date_invalid_date():
    with pytest.raises(ValueError):
        get_date("2023-02-30")  # Неверная дата (30 февраля не существует)
