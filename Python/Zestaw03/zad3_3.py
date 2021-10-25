def print_except_divisible_by_3(n): # wypisuje liczby od 0 do n niepodzielne przez 3
    for i in range(n+1):
        if i%3 != 0:
            print(i)

print_except_divisible_by_3(30)