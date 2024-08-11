from masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскирует счета и карты"""
    if "Счет" in number:
        return f"{number[0:4]} {get_mask_account(number[-16:])}"
    elif "Visa" or "Master" in number:
        cards = get_mask_card_number(number[-16:])
        new_cards = number.replace(number[-16:], cards)
        return new_cards




def get_date(date: str) -> str:
    """Функция преобразовывает дату"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"



