'''Реализуйте класс стек. Класс должен иметь следующий функционал:
В данном задании необходимо только реализовать класс стек. Считывать и выводить
ничего не надо.
Примеры
Входные данные Выходные данные
push - добавление элемента в стек
pop - удаление элемента из стека. Если в стеке нет элементов вернуть None
измерение длины стека стандартным методом (функция len )
проверка вхождения объекта в стек
должна быть возможность итерироваться по стеку, получая элементы по порядку
начиная с вершины
строковое представление стека в формате q0<-q1<-q2<-q3<-q4<-... , где q0 элемент
на вершине стека
должен быть ограничен доступ к приватному атрибуту __stack , содержащему в себе
элементы стека
реализовать свойство stack , возвращающее содержимое стека в виде списка, но без
возможности изменения содержимого'''
class Stack:
    def __init__(self) -> None:
        self.__stack = list()
    def push(self, value) -> None:
        self.__stack.append(value)
    def pop(self) -> None:
        if len(self.__stack) == 0:
            return None
        return self.__stack.pop()
    def __len__(self) -> int:
        return len(self.__stack)
    def __contains__(self, value) -> bool:
        return value in self.__stack
    def __iter__(self):
        return iter(self.__stack)
    def __str__(self) -> str:
        return ', '.join(list(map(str, self.__stack[::-1])))
    def stack(self) -> list:
        return self.__stack