def product_by_parity(n):
    dob = 1

    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            dob *= i
    else:
        for i in range(2, n + 1, 2):
            dob *= i

    return dob