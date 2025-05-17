from random import randint
import FreeSimpleGUI as sg

rnd_num = 0
try_cnt = 0
current_min, current_max = None, None


# Функция создаёт рандомное число в заданных пределах
def rnd(start, finish):
    return randint(start, finish)


# Функция проверки корректности введенных данных
def is_valid(input, start, finish):
    return input.isdigit() and start <= int(input) <= finish


# Функция проверки корректности введёных границ рандома
def limit_check(start, finish):
    return start < finish


def game(num_try, rnd_num):
    global try_cnt, current_min, current_max
    try_cnt += 1
    guess = int(num_try)
    if (
        rnd_num == 0
    ):  # Если пользователь начнёт угадывать число до того как определит границы рандомного числа
        return "Нажмите Новое число."
    elif guess < rnd_num:
        # Обновляем минимальную границу
        if guess > current_min:
            current_min = guess
        window["-range-"].update(f"от {current_min} до {current_max}")
        return "Ваше число меньше загаданного, попробуйте еще разок"
    elif guess > rnd_num:
        # Обновляем максимальную границу
        if guess < current_max:
            current_max = guess
        window["-range-"].update(f"от {current_min} до {current_max}")
        return "Ваше число больше загаданного, попробуйте еще разок"
    else:
        message = f"Вы угадали с {try_cnt} попытки, поздравляем!"
        return message


def main(values):
    global try_cnt
    start = int(values["-input_left_limit-"])
    finish = int(values["-input_right_limit-"])
    num_try = values["-enter_rnd_num-"]
    text_elem = window["-text-"]

    if is_valid(num_try, start, finish):
        message = game(num_try, rnd_num)
        text_elem.update(message)
    elif limit_check(start, finish) == False:
        window["-text-"].update(
            "Введите корректные пределы нахождения случайного числа"
        )
    else:
        text_elem.update(
            f"А может быть все-таки введем целое число от {start} до {finish}?"
        )


# Создаем окно
layout = [
    [sg.Text("Добро пожаловать в числовую угадайку", font="Helvetica 16")],
    [
        sg.Text("Укажите пределы случайного числа, от:"),
        sg.InputText(key="-input_left_limit-", size=(10, 1)),
        sg.Text("до:"),
        sg.InputText(key="-input_right_limit-", size=(10, 1)),
    ],
    [
        sg.Text("Введите целое число", font="Helvetica 16"),
        sg.Button(
            "Новое число", enable_events=True, key="-NEW_RND-", font="Helvetica 16"
        ),
    ],
    [
        sg.InputText(key="-enter_rnd_num-", size=(10, 1)),
        sg.Button("Ввод", enable_events=True, key="-TRY_SEARCH-", font="Helvetica 16"),
        sg.Text(key="-range-", font="Helvetica 16"),
    ],
    [sg.Text(key="-text-", font="Helvetica 10")],
]

window = sg.Window("Числовая угадайка", layout)


while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Exit"):
        break

    if event == "-NEW_RND-":
        # Генерируем новое число и сбрасываем счетчик попыток
        start = int(values["-input_left_limit-"])
        finish = int(values["-input_right_limit-"])
        if limit_check(start, finish):
            rnd_num = rnd(start, finish)
            try_cnt = 0
            current_min = start
            current_max = finish
            window["-range-"].update(f" от {start} до {finish}")
            window["-text-"].update(
                f"Загадано новое число от {start} до {finish}. Попробуйте угадать!"
            )
        else:
            window["-text-"].update(
                "Введите корректные пределы нахождения случайного числа"
            )

    elif event == "-TRY_SEARCH-":
        # Используем существующее загаданное число
        main(values)

window.close()
