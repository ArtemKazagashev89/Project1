from src.masks import get_mask_account, get_mask_card_number

from datetime import datetime


def mask_account_card(number: str) -> str:
    """Функция маскирует счета и карты"""
    if "Счет" in number:
        return f"{number[0:4]} {get_mask_account(number[-16:])}"
    elif "Visa" in number or "Master" in number:
        cards = get_mask_card_number(number[-16:])
        new_cards = number.replace(number[-16:], cards)
        return new_cards
    else:
        return "Некорректный ввод"





def get_date(date: str) -> str:
    """Функция преобразовывает дату"""
    dt = datetime.strptime(date, "%Y-%m-%d")
    return dt.strftime("%d.%m.%Y")

