def filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    return [item for item in data if item.get('state') == state]

oper = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]
print(filter_by_state(oper, 'EXECUTED'))
print(filter_by_state(oper, 'CANCELED'))
#по умолчанию executed
print(filter_by_state(oper))


#    Сортирует список словарей по ключу 'date'.
def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    return sorted(data, key=lambda item: item['date'], reverse=reverse)

print(sort_by_date(oper))
print(sort_by_date(oper, False))