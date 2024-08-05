from masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция маскирует счета и карты"""
    if "Счет" in number:
        return f"{number[0:4]} {get_mask_account(number[-16:])}"
    elif "Visa" or "Master" in number:
        cards = get_mask_card_number(number[-16:])
        new_cards = number.replace(number[-16:], cards)
        return new_cards


print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date: str) -> str:
    """Функция преобразовывает дату"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
