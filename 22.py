'''Реализуйте функцию, которая принимает в качестве первого аргумента строку, а затем
любое количество именованных аргументов.
Именованные аргументы представляют собой множества. Принадлежность элемента к
конкретному множеству определяется по первому символу имени аргумента.
Найти объединение, пересечение или симметрическую разность полученных множеств в
зависимости от значения первого аргумента.
Если введено некорректное значение первого аргумента или нет именованных аргументов,
то функция должна вернуть пустое множество'''
def task(meth: str, **rwargs) -> str:
    mn = dict()
    for value in rwargs.values():
        if value[0] not in mn:
            mn[value[0]] = set([int(i) for i in str(value[1:])])
        else:
            mn[value[0]] = set(mn[value[0]]).union([int(i) for i in str(value[1:])])
    if meth == "OR":
        return set.union(*[i for i in list(mn.values())])
    if meth == "AND":
        return set.intersection(*[i for i in list(mn.values())])
    if meth == "NOT":
        return set.difference(*[i for i in list(mn.values())])
resolve = task()
print(task)