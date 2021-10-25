while True:
    x = input("Podaj liczbe typu float, aby zakonczyc wpisz \"stop\": ")
    try:
        if x == "stop":
            break
        number = float(x)
    except ValueError:
        print("Nie podano liczby typu float.")
    print("x =", number, "\nx^3 =", pow(number, 3))
