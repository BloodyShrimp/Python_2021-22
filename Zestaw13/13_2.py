# Problem ośmiu hetmanów.
# Znajdowanie jednego rozwiązania.
# Wiersze i kolumny mają zakres od 0 do N-1.

def rysuj():
    for w in range(N):
        print ( " ".join(("H" if x[k] == w else ".") for k in range(N)) )

def dopuszczalny(w, k):
    return a[w] and b[w+k] and c[w-k]

def zapisz(w, k):
    x[k] = w
    a[w] = False
    b[w+k] = False
    c[w-k] = False

def wymaz(w, k):
    a[w] = True
    b[w+k] = True
    c[w-k] = True

def probuj(k):
    for w in range(N):
        if dopuszczalny(w, k):
            zapisz(w, k)
            if k < (N-1):
                probuj(k+1)
            else:
                print("-" * 2 * N)
                rysuj()
            wymaz(w, k)

def checkForSize(size):
    global N
    N = size  # bok szachownicy i jednocześnie liczba hetmanów
    global x
    global a
    global b
    global c
    x = N * [None]
    a = N * [True]
    b = (2*N-1) * [True]
    c = (2*N-1) * [True]
    print("Rozmiar szachownicy: " + str(size))
    probuj(0)

def checkFromTo(start, end):
    for i in range(start, end + 1):
        checkForSize(i)

checkFromTo(6, 6)