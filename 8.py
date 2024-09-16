'''Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в
каждом наборе все кубики различны по цвету. Однажды дети заинтересовались, сколько
существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах. Для этого
они занумеровали все цвета случайными числами от 0 до 10
8
. На этом их энтузиазм иссяк,
поэтому вам предлагается помочь им в оставшейся части.
'''
def task():
    n, m = map(int, input().split())
    set_1 = set()
    set_2 = set()
    for i in range(n+m):
        if i < n:
            set_1.add(input())
        else:
            set_2.add(input())
    all_ = set_1 & set_2
    only_first = set_1 - set_2
    only_second = set_2 - set_1
    print(len(all_), ''join(sorted(all_)), sep="\n")
    # Дописать сортировку
    print(len(only_first), ''join(sorted(only_first)), sep="\n")
    print(len(only_second), ''join(sorted(only_second)), sep="\n")
resolve = task()