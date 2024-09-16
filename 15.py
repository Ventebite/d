'''Определите сумму всех элементов последовательности, завершающейся числом 0
'''
def task():
    sum_ = 0
    while True:
        n = int(input())
        if n == 0:
            break
        sum_+=n
    return(sum_)
resolve = task()
print(resolve)