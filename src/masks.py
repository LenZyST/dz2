def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты.

    Args:
        card_number: Номер карты в виде строки.

    Returns:
        Маскированный номер карты.
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета.

    Args:
        account_number: Номер счета в виде строки.

    Returns:
        Маскированный номер счета.
    """
    return f"**{account_number[-4:]}"
