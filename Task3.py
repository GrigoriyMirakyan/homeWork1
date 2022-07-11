# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

#            y|
#             |
#             |
#      II     |     I
#             |             x
# -------------------------->
#             |
#     III     |     IV
#             |
#             |
#             |


def InputNumbers(inputText):  # метод ввода и проверки числа
    number = input(f"{inputText}")
    while type(number) != int:
        try:
            number = int(number)
        except ValueError:
            print("Это не число! Введите число")
            number = input(f"{inputText}")
    return number


quarter = InputNumbers('Введите номер четверти (1-4):')

while 4 < quarter or quarter < 0:
    quarter = InputNumbers(
        'Введен некоректный номер четверти \nПожалуйста повторите ввод (1-4):')
if quarter == 1:
    print(
        f"диапазон возможных координат в 1 четверти \nx = {[i+1 for i in range(10)]}\ny = {[i+1 for i in range(10)]} ")
elif quarter == 2:
    print(
        f"диапазон возможных координат вo 2 четверти \nx = {[i for i in range(-10,0)]}\ny = {[i+1 for i in range(10)]} ")
elif quarter == 3:
    print(
        f"диапазон возможных координат в 3 четверти \nx = {[i for i in range(-10,0)]}\ny = {[i for i in range(-10,0)]} ")
elif quarter == 4:
    print(
        f"диапазон возможных координат в 4 четверти \nx = {[i+1 for i in range(10)]}\ny = {[i for i in range(-10,0)]} ")

# Решение для целых чисел в границах таблицы координат 10, -10
