from src.masks import get_mask_account, get_mask_card_number

card = input("Enter your card type and number: ")

print(get_mask_card_number(card))
print(get_mask_account(card))