# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = float(input('Input your number: '))


while round(num) != num:
    num *= 10
sum = 0


while num > 0:
    sum += num % 10
    num //= 10


print('Sum is:', round(sum))