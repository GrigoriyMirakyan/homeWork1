# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

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


print('Введите координаты точки:')
x = InputNumbers("x = ")
y = InputNumbers('y = ')

if x > 0 and y > 0:
    print("Точка находится в I четверти")
elif x < 0 and y > 0:
    print("Точка находится во II четверти")
elif x > 0 and y < 0:
    print("Точка находится в III четверти")
elif x < 0 and y < 0:
    print("Точка находится в IV четверти")
elif x == 0 and y == 0:
    print("Точка находится в центре координат")
elif x == 0:
    print('Точка находится на оси X')
elif y == 0:
    print('Точка находится на оси Y')
