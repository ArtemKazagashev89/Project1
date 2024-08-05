def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты"""
    if card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    if account_number.isdigit():
        return f"** {account_number[-4:]}"
