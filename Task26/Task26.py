import os
os.system("clear")

# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def PowerAB(a, b):
    if b == 0:
        return 1
    return a * PowerAB(a, b - 1)
A, B = (int(i) for i in input('Введите A и B: ').split())

print(f'A = {A}; B = {B} -> {PowerAB(A,B)}')
