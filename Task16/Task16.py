# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input("Введите размер массива: "))
a = []
for i in range(n):
    a.append(int(input(f"Введите элемент массива [{i + 1}]: ")))
x = int(input("Введите некоторое число: "))

result = a.count(x)

print(f"Число {x} встречается {result} раз в массиве.")