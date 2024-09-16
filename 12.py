'''Напишите программу, которая принимает 3 числа - стороны треугольника и проверяет,
является ли треугольник равносторонним ( equilateral ), равнобедренным ( isosceles ) или
общего вида ( scalene ).
'''
def check_sqr(x: int, y: int, z: int) -> str:
    if (x==y==z):
        print("equilateral")
    elif (x==y) or (y==z) or (x==z):
        print("isosceles")
    else:
        print("scalene")
check_sqr(3,4,5)