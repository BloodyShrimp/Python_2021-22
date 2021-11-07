import math

def factorial(n):
    result = 1
    if n > 1:
        for i in range(1, n + 1):
            result *= i
        return result
    elif n == 0:
        return 1
    else:
        raise ValueError("Liczba musi byc nieujemna.")

number = int(input("Podaj liczbe nieujemna: "))
number_fac = factorial(number)
assert number_fac == math.factorial(number)
print(str(number) + "! = " + str(number_fac))