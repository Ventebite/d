'''Напишите программу, которая принимает на вход последовательность 4-х значных двоичных
чисел и выводит на экран числа, делящиеся на 5.
'''
def task():
    nums = map(int, input().split(','))
    for i in nums:
        if int(str(i), 2)%5 == 0:
            print(i)