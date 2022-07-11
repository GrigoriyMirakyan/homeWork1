# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math  # Я честно не знаю как корень взять без этого =)


def InputNumbers(inputText):  # метод ввода и проверки числа
    number = input(f"{inputText}")
    while type(number) != int:
        try:
            number = int(number)
        except ValueError:
            print("Это не число! Введите число")
            number = input(f"{inputText}")
    return number


x1 = InputNumbers("Введите x1 : ")
y1 = InputNumbers("Введите y1 : ")
x2 = InputNumbers("Введите x2 : ")
y2 = InputNumbers("Введите y2 : ")

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(
    f"Расстояние между точками ({x1},{y1}) и  ({x2},{y2}) - > {distance:.2f}")
