'''Дана строка. Замените в этой строке все цифры 1 на слово one .'''
def one() -> str:
    x = input()
    return(x.replace('1','one'))
    

result = one()
print(result)

#print(input().replace('1', 'one'))