'''Напишите программу для проверки корректности пароля введенного пользователем.
Пароль должен иметь следующие свойства:'''
import re
def task(): 
    password = input()
    if not re.match(r"^(?=*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$", password):
        print('Password is not valid')
    else:
        print('Password is valid')