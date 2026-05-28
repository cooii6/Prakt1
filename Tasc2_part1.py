import math


def expression(x):
    z = math.exp(math.sqrt(x)) / math.sqrt(1 - math.sqrt(x))
    return z


def product_by_parity(n):
    dob = 1

    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            dob *= i
    else:
        for i in range(2, n + 1, 2):
            dob *= i

    return dob


x = float(input("Введіть значення x: "))

while x < 0 or x >= 1:
    print("Помилка! Для цього виразу x має бути в межах 0 <= x < 1.")
    x = float(input("Введіть значення x ще раз: "))

print("Значення виразу z =", expression(x))

n = int(input("Введіть ціле невід'ємне число N: "))

while n < 0:
    print("Помилка! N має бути невід'ємним числом.")
    n = int(input("Введіть ціле невід'ємне число N ще раз: "))

print("Добуток =", product_by_parity(n))