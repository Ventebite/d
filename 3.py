'''В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один
родитель.
В генеалогическом древе определите для двух элементов их наименьшего общего предка
(Lowest Common Ancestor). Наименьшим общим предком элементов A и B является такой
элемент C, что С является предком A, C является предком B, при этом глубина C является
наибольшей из возможных. При этом элемент считается своим собственным предком.
Не работает '''
def ancestors(child, parent):
    result = []
    result.append(child)
    while child in parent:
        child = parent[child]
        result.append(child)
    return result
def task(): #
    parent = dict() 
    n = int(input())
    for i in range(n - 1):
        child, parent = input().split()
        parent[child] = parent
    m = int(input())
    for i in range(m):
        child_1, child_2 = input().split()
        ancestors_for_1 = set(ancestors(child_1, parent))
        for ancestor in ancestors(child_2, parent):
            if ancestor in ancestors_for_1:
                print(ancestor)
                break
resolve = task()
print(resolve)