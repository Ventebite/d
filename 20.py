'''Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё
место в строю. Помогите ему это сделать.
'''
def task():
    heights = map(int, input().split())
    petya = int(input())
    for i, val in enumerate(heights):
        if val < petya:
            print(i + 1)
            break