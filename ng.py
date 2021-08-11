from random import *

#Функция для проверки корректности введенных данных
def is_valid(user_num): 
    if 1 <= int(user_num) <= 100:
        return True
    else:
        return False

rand_num = randint(1,100)
print("Добро пожаловать в числовую угадайку")