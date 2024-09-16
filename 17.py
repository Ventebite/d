'''Определите среднее значение всех элементов последовательности, завершающейся
числом 0.
'''
def task():
    num_for_append = float(input())
    list_for_execute = []    
    while num_for_append != 0:
        list_for_execute.append(num_for_append)
        num_for_append = float(input())
    if sum(list_for_execute) == 0:
        return 0
    return float(sum(list_for_execute) / len(list_for_execute))

result = task()
print(result)