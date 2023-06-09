import os
os.system("clear")

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def get_sum(a: int, b: int) -> int:
    if b == 0:
        return a
    return get_sum(a + 1, b - 1)


print(get_sum(3, 6))

def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)


n, m = (int(i) for i in input("Введите два целых числа: ").split())

result = sum(n, m)

print(f"{n} + {m} = {result}")
