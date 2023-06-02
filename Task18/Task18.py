# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

sizeArray = int(input("Введите размер массива: "))
array = []
for i in range(sizeArray):
    array.append(int(input(f"Введите элемент массива A[{i + 1}]: ")))
x = int(input("Введите X: "))

result = array[0]
min = abs(x - array[0])
for i in range(1, sizeArray):
    distance = abs(x - array[i])
    if min > distance:
        result = array[i]

print(f"Cамый близкий по величине элемент к числу {x} в массиве {array} - это {result}")