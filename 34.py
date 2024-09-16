'''Дана строка. Замените в этой строке все появления буквы  h  на букву  H , кроме первого и
последнего вхождения.
'''
def task():
    text = input()
    first_h = text.index('h')
    last_h = len(text) - text[::-1].index('h')
    return (text[0:first_h+1], text[first_h+1:last_h-1].replace('h', 'H'), text[last_h-1:], sep='') #print.]