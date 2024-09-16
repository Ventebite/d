'''Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n . Беатриса
пытается угадать это число, для этого она называет некоторые множества натуральных
чисел. Август отвечает Беатрисе YES , если среди названных ей чисел есть задуманное или
NO в противном случае. После нескольких заданных вопросов Беатриса запуталась в том,
какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить,
какие числа мог задумать Август.'''
def task():
    n = int(input())
    a = set(range(1, n + 1))
    for i in range(n):
        try:
            z = set([int(i) for i in input().split()])
            b = input()
        except ValueError:
            break
        if b == 'YES':
            a &= z
        else:
            a -= Z
    return print(*sorted(a))
resolve = task()
print(resolve)