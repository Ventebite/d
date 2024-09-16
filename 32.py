'''Дана строка, в которой буква h встречается как минимум два раза. Разверните
последовательность символов, заключенную между первым и последним появлением буквы
h , в противоположном порядке'''
def task():
    str_for_valid = input()
    start_index = str_for_valid.find('h')
    end_index = - str_for_valid[::-1].find('h')
    reverse_str_start_end = str_for_valid[start_index + 1: end_index][::-1]
    complete = str_for_valid[:start_index] + reverse_str_start_end + str_for_valid[end_index-1::+1]
    return complete
    
result = task()
print(result)

#-------------

def task():
    text = input()
    first_h = text.index('h')
    last_h = len(text) - text[::-1].index('h')
    return (text[0:first_h+1], text[last_h-2:first_h:-1], text[last_h:len(text)], sep='') #print
