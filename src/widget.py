from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(info_string: str) -> str:
    parts = info_string.split()

    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"

def get_date(date_string: str) -> str:
    year = date_string[:4]
    month = date_string[5:7]
    day = date_string[8:10]

    return f"{day}.{month}.{year}"

def mask_account_number():
    account = input("Enter your account number: ")
    print(get_mask_account(account))

def mask_card_number():
    card = input("Enter your card number: ")
    print(get_mask_card_number(card))

# примеры
if __name__ == "__main__":
    print(mask_account_card("visa classic 293923923902")) 
    print(get_date("2026-01-01")) 