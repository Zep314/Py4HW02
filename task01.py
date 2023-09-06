# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.


def my_hex(n: int) -> str:  # Моя функция перевода десятичного числа в шестнадцатеричное представление
    hex_string = "0123456789ABCDEF"
    ret = "" if n != 0 else "0"
    while n > 0:
        ret = hex_string[n % 16] + ret  # строку формируем справа на лево
        n = n // 16
    ret = ret.zfill(4)                  # добавляем ведущие нули (если надо)
    return "".join(["0x", ret])         # красиво отдаем результат


if __name__ == '__main__':
    a = int(input("Введите целое неотрицательное число: "))
    if a >= 0:
        print(f"Шестнадцатеричное представление десятичного числа {a} будет {my_hex(a)}, проверка: {hex(a)}")
    else:
        print("Ошибка ввода!")

# Результат работы программы:
# C:\Work\python\dz4\Py4HW02\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW02/task01.py
# Введите целое неотрицательное число: 65521
# Шестнадцатеричное представление десятичного числа 65521 будет 0xFFF1, проверка: 0xfff1
#
# C:\Work\python\dz4\Py4HW02\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW02/task01.py
# Введите целое неотрицательное число: 0
# Шестнадцатеричное представление десятичного числа 0 будет 0x0000, проверка: 0x0
#
# C:\Work\python\dz4\Py4HW02\venv\Scripts\python.exe C:/Work/python/dz4/Py4HW02/task01.py
# Введите целое неотрицательное число: 33
# Шестнадцатеричное представление десятичного числа 33 будет 0x0021, проверка: 0x21
#
# Process finished with exit code 0
