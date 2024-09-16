'''Каждый из некоторого множества школьников некоторой школы знает некоторое количество
языков. Нужно определить сколько языков знают все школьники, и сколько языков знает
хотя бы один из школьников.'''
def task():
    n = int(input())
    lang = list()
    same = list()
    max = 0
    ind_max = 0
    for i in range(n):
        tmp = list()
        k = int(input())
        if k > max:
            max = k
            ind_max = i
        for i in range(k):
            tmp.append(input())
        lang.append(set(tmp))
    for i in range(1, len(lang)):
        same.append(lang[0]. intersection(lang[i]))
    print(len(same[-1]), *[i for i in sorted(same[-1])], sep="\n")
    print(max, *[i for i in sorted(lang[and_max])], sep="\n")