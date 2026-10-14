def filter_by_state(
    data: list[dict[str, int | str]],
    state: str = "EXECUTED",
) -> list[dict[str, int | str]]:
    """Фильтрует список словарей по значению ключа state.

    Args:
        data: Список словарей с данными операций.
        state: Статус для фильтрации. По умолчанию EXECUTED.

    Returns:
        Список словарей с указанным статусом.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(
    data: list[dict[str, int | str]],
    reverse: bool = True,
) -> list[dict[str, int | str]]:
    """Сортирует список словарей по ключу date.

    Args:
        data: Список словарей с данными операций.
        reverse: Порядок сортировки. True — от новых к старым.

    Returns:
        Отсортированный список словарей.
    """
    return sorted(data, key=lambda item: item["date"], reverse=reverse)


if __name__ == "__main__":
    operations: list[dict[str, int | str]] = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]
    print(filter_by_state(operations, "EXECUTED"))
    print(filter_by_state(operations, "CANCELED"))
    print(filter_by_state(operations))
    print(sort_by_date(operations))
    print(sort_by_date(operations, False))
