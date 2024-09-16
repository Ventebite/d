'''Дана база данных о продажах некоторого интернет-магазина. Каждая строка входных
данных представляет собой запись вида Покупатель товар количество , где Покупатель —
имя покупателя (строка без пробелов), товар — название товара (строка без пробелов),
количество — количество приобретенных единиц товара'''
def task():
    n = int(input())
    customers = dict()
    for i in range(n):
        name, item, count = input().split()
    if name not in customers:
        customers[name] = {item: int(count)}
    elif item not in customers[name]:
        customers[name][item] = int(count)
    else:
        customers[name][item] += int(count)
    return customers
result = task()
print(result)
