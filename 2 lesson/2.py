# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

digit = int(input('Введите число: '))

digits = []
mult = 1


for i in range(1, digit+1):
    mult*=i
    digits.append(mult)


print(digits)