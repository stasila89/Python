# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет 
# с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.
# *Пример:*

# 385916 -> yes
# 123456 -> no


ticketNumber = int(input("Введите номер билета: "))

firstPartTicket = ticketNumber // 1000
secondPartTicket = ticketNumber % 1000

firstPartSum = firstPartTicket // 100 + firstPartTicket // 10 % 10 + firstPartTicket % 10
secondPartSum = secondPartTicket // 100 + secondPartTicket // 10 % 10 + secondPartTicket % 10

if firstPartSum == secondPartSum:
    print(f"{ticketNumber} является счастливым")
else:
    print(f"{ticketNumber} не является счастливым")

