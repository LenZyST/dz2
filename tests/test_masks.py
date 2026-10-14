import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize(
    "account_number, expected",
    [
        # обычный счёт (длинный номер)
        ("73654108430135874305", "**4305"),
        # другая длина, но последних 4 символа те же по логике функции
        ("1234567890", "**7890"),
        # короче ожидаемого — функция всё равно берёт [-4:]
        ("123", "**123"),
        ("12", "**12"),
        ("1", "**1"),
        ("", "**"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected