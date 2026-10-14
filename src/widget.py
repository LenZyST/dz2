from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Маскирует номер карты или счета, сохраняя название.

    Args:
        info_string: Строка с названием и номером карты или счета.

    Returns:
        Строка с названием и замаскированным номером.
    """
    parts = info_string.split()

    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразует дату из ISO-формата в ДД.ММ.ГГГГ.

    Args:
        date_string: Дата в формате ГГГГ-ММ-ДД...

    Returns:
        Дата в формате ДД.ММ.ГГГГ.
    """
    year = date_string[:4]
    month = date_string[5:7]
    day = date_string[8:10]

    return f"{day}.{month}.{year}"


def mask_account_number() -> None:
    """Запрашивает номер счета и выводит его в маскированном виде."""
    account = input("Enter your account number: ")
    print(get_mask_account(account))


def mask_card_number() -> None:
    """Запрашивает номер карты и выводит его в маскированном виде."""
    card = input("Enter your card number: ")
    print(get_mask_card_number(card))


if __name__ == "__main__":
    print(mask_account_card("visa classic 293923923902"))
    print(get_date("2026-01-01"))
