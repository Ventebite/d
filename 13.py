'''Напишите программу, которая принимает на вход 2 числа a и b и выводит все числа в
диапазоне от [a;b], в которых каждая цифра является четной. Полученные числа вывести
через запятую.
'''
def task():
    a,b = map(int, input().split())
    nums = list()
    for i in range(a,b+1):
        if i % 2 == 0:
            nums.append(i)
    print(', 'join(list(map(str, nums))))