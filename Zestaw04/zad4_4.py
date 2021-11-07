def fibonacci(n):
    if n < 0:
        raise ValueError("Liczba musi byc nieujemna.")
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

number = int(input("Podaj liczbe nieujemna: "))
number_fib = fibonacci(number)
print(str(number) + " element ciagu Fibonacciego = " + str(number_fib))