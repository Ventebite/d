'''Последовательность состоит из натуральных чисел и завершается числом 0. Определите
значение наибольшего элемента последовательности'''
def task():
    x = int(input())
    max_ = x
    while True:
        x = int(input())
        if x == 0:
            break
        if max_ < x:
            max_ = x
    return max_
resolve = task()
print(resolve)