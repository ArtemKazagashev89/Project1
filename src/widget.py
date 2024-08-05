from masks import get_mask_card_number, get_mask_account


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