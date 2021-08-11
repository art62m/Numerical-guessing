from random import *

#Функция для проверки корректности введенных данных
def is_valid(num, right_num): 
    if 1 <= int(num) <= right_num:
        return True
    else:
        return False

attempts = 0
repeat = "y"
print("Добро пожаловать в числовую угадайку")

#Основной цикл программы
while repeat == "y":
    print("Введите правую границу  диапазона:")
    right_bord = int(input())
    rand_num = randint(1, right_bord)
    while True:
        print("Какое число я загадал?")
        user_num = input()
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
                break
    print(f"Количество попыток: {attempts}")
    print("Введите 'y', если хотите повторить, и 'n', если хотите закончить")
    repeat = input()
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
