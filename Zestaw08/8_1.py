def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 and c == 0:
        print("x = R, y = R")
    elif a == 0 and b == 0:
        print("brak rozwiazan")
    elif a == 0:
        print("x = R, y = " + str(-c / b))
    elif b == 0:
        print("x = " + str(-c / a) + ", y = R")
    else:
        if(c > 0):
            print("y = (" + str(-a) + "x - " + str(c) + ") / " + str(b))
        else:
            print("y = (" + str(-a) + "x + " + str(-c) + ") / " + str(b))

solve1(0, 0, 0) 
solve1(0, 0, 7) 
solve1(0, 13, 7) 
solve1(13, 0, 7) 
solve1(13, 3, 7) 