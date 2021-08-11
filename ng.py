from random import *
from typing import ItemsView

#Функция для проверки корректности введенных данных
def is_valid(num): 
    if 1 <= num <= 100:
        return True
    else:
        return False

rand_num = randint(1,100)
print("Добро пожаловать в числовую угадайку")

#Основной цикл программы
while True:
    user_num = int(input())
    if not is_valid(user_num):
        print("А может быть все-таки введем целое число от 1 до 100?")
    else:
        if user_num < rand_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif user_num > rand_num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print("Вы угадали, поздравляем!")
            break
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")