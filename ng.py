from random import *

#Функция для проверки корректности введенных данных
def is_valid(num, right_num): 
    if num.isdigit():
        if 1 <= int(num) <= right_num:
            return True
        else:
            return False
    else:
        return False        

repeat = "y"
print("Добро пожаловать в числовую угадайку")

#Основной цикл программы
while repeat == "y":
    attempts = 0
    right_bord = input("Введите правую границу  диапазона: ")
    if not right_bord.isdigit():
        print("Правая граница должна быть числом!")
        continue
    right_bord = int(right_bord)
    rand_num = randint(1, right_bord)
    while True:
        user_num = input("Какое число я загадал? ")
        if not is_valid(user_num, right_bord):
            print(f"А может быть все-таки введем целое число от 1 до {right_bord}?")
        else:
            user_num = int(user_num)
            if user_num < rand_num:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                attempts += 1
            elif user_num > rand_num:
                print("Ваше число больше загаданного, попробуйте еще разок")
                attempts += 1
            else:
                print("Вы угадали, поздравляем!")
                attempts += 1
                break
    print(f"Количество попыток: {attempts}")
    repeat = input("Введите 'y', если хотите повторить, и любой символ, если хотите закончить: ")
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
