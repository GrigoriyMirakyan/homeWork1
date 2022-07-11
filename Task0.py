# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# 6 -> да
# 7 -> да
# 1 -> нет

def InputNumbers(inputText):  # метод ввода и проверки числа
    number = input(f"{inputText}")
    while type(number) != int:
        try:
            number = int(number)
        except ValueError:
            print("Это не число! Введите число")
            number = input(f"{inputText}")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Да, это выходной!")
    elif 0 < num < 6:
        print("Нет, это не выходной.")
    else:
        print("Такого дня недели нет!")


num = InputNumbers("Введите номер дня недели 1-7\n ")
checkNumber(num)
