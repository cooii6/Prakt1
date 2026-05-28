from mod import product_by_parity


n = int(input("Введіть ціле невід'ємне число N: "))

while n < 0:
    print("Помилка! N має бути невід'ємним числом.")
    n = int(input("Введіть ціле невід'ємне число N ще раз: "))

print("Добуток =", product_by_parity(n))