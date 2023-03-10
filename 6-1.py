# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

numbers = input('Введите числа через пробел: ').split()

def get_2digit_number(i):
    if len(i) == 2:
        return True

result = filter(get_2digit_number, numbers)

print(*list(result))
