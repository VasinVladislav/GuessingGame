from random import randint


def rnd(start, finish):
    return randint(start, finish)


# Функция проверки корректности введенных данных
def is_valid(input, start, finish):
    return input.isdigit() and start <= int(input) <= finish


# Цикл получения числа от пользователя
def main(start, finish):
    while True:
        s = input(f"Введите целое число от {start} до {finish}\n")
        if is_valid(s, start, finish):
            return int(s)
        else:
            print(f"А может быть все-таки введем целое число {start} до {finish}?")


# Основной цикл программы
def game():
    start = int(input("Укажите пределы случайного числа, от ... "))
    finish = int(input("Укажите пределы случайного числа, до ... "))
    rnd_num = rnd(start, finish)
    try_cnt = 0
    while True:
        guess = main(start, finish)
        try_cnt += 1
        if guess < rnd_num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif guess > rnd_num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print(f"Вы угадали с {try_cnt} попытки, поздравляем!")
            if input('Нажмите "Y" если хотите сыграть ещё раз\n').lower() == "y":
                game()
            break


print("Добро пожаловать в числовую угадайку")
game()
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
