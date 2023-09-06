# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте
# модуль fractions.

from fractions import Fraction
import re


def summ_frac(p1, p2):  # функция сложения двух дробей
    return [p1[0] * p2[1] + p2[0] * p1[1], p1[1] * p2[1]]


def mult_frac(p1, p2):  # функция умножения двух дробей
    return [p1[0] * p2[0], p1[1] * p2[1]]


if __name__ == '__main__':

    print("Вводите дроби в формате 'a/b'")
    a = input("Введите первую дробь: ")
    b = input("Введите вторую дробь: ")

    # Выкинуть из строки все цифры
    # и знаки / и -
    if (len(re.sub(r"[\d+/\-]", "", a)) > 0) or (len(re.sub(r"[\d+/\-]", "", b)) > 0):
        print("Ошибка! Неверный формат дроби!")
    else:
        parts_a = list(map(int, a.split("/")))
        parts_b = list(map(int, b.split("/")))

        print(f"Складываем и умножаем два дробных числа: {a} и {b}")
        print(f'Сумма двух дробей {a} и {b} равна {"/".join(list(map(str, summ_frac(parts_a, parts_b))))}')
        print(f'Произведение двух дробей {a} и {b} равна {"/".join(list(map(str, mult_frac(parts_a, parts_b))))}')

        print(f"---=== Проверка: ===---")
        print(f"Сума дробей: {Fraction(parts_a[0], parts_a[1]) + Fraction(parts_b[0], parts_b[1])}")
        print(f"Произведение дробей: {Fraction(parts_a[0], parts_a[1]) * Fraction(parts_b[0], parts_b[1])}")

# Результат работы:
# C:\Work\python\dz4\Py4HW02\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW02/task02.py
# Вводите дроби в формате 'a/b'
# Введите первую дробь: 6/7
# Введите вторую дробь: -3/7
# Складываем и умножаем два дробных числа: 6/7 и -3/7
# Сумма двух дробей 6/7 и -3/7 равна 21/49
# Произведение двух дробей 6/7 и -3/7 равна -18/49
# ---=== Проверка: ===---
# Сума дробей: 3/7
# Произведение дробей: -18/49
#
# C:\Work\python\dz4\Py4HW02\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW02/task02.py
# Вводите дроби в формате 'a/b'
# Введите первую дробь: q1/3
# Введите вторую дробь: 15/16
# Ошибка! Неверный формат дроби!
#
# Process finished with exit code 0
