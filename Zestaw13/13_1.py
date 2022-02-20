# Problem drogi skoczka na kwadratowej szachownicy o boku N.
# Współrzędne planszy x i y mają zakres od 0 do N-1.

from tracemalloc import start


def rysuj():
    for i in range(N):
        print(" ".join("{0:2d}".format(plansza[i, j]) for j in range(N)))


def dopuszczalny(x, y):
    return 0 <= x < N and 0 <= y < N and plansza[x, y] == 0


def zapisz(krok, x, y):
    plansza[x, y] = krok  # zapis ruchu


def wymaz(x, y):
    plansza[x, y] = 0


def probuj(krok, x, y):
    # krok - nr kolejnego kroku do zrobienia
    # x, y - pozycja startowa skoczka
    # Funkcja zwraca bool True/False (czy udany ruch).
    udany = False
    kandydat = 0  # numery od 0 do RUCHY_SKOCZKA-1
    while (not udany) and (kandydat < RUCHY_SKOCZKA):
        u = x + delta_x[kandydat]  # wybieramy kandydata
        v = y + delta_y[kandydat]
        if dopuszczalny(u, v):
            zapisz(krok, u, v)
            if krok < N * N:  # warunek końca rekurencji
                udany = probuj(krok + 1, u, v)
                if not udany:
                    wymaz(u, v)
            else:
                udany = True
        kandydat += 1
    return udany


RUCHY_SKOCZKA = 8


# . 2 . 1 .   kolejne możliwe ruchy skoczka
# 3 . . . 0
# . . x . .
# 4 . . . 7
# . 5 . 6 .

delta_x = [2, 1, -1, -2, -2, -1, 1, 2]  # różnica współrzędnej x
delta_y = [1, 2, 2, 1, -1, -2, -2, -1]  # różnica współrzędnej y

def checkSolution(rozmiar, start_x, start_y):
    global N
    N = rozmiar  # bok szachownicy

    # Inicjalizacja pustej planszy.
    global plansza
    plansza = {}
    for i in range(N):
        for j in range(N):
            plansza[i, j] = 0

    zapisz(1, start_x, start_y)

    if probuj(2, start_x, start_y):
        print("Mamy rozwiązanie " + str((start_x, start_y)) + "\n")
        rysuj()
    else:
        print("Nie istnieje rozwiązanie " + str((start_x, start_y)) + "\n")

def checkAllForBoard(rozmiar):
    for i in range(0, rozmiar):
        for j in range(0, rozmiar):
            checkSolution(rozmiar, i, j)

for i in range(3, 7):
    print("Rozwiązania dla rozmiaru " + str(i) + "x" + str(i) + "\n")
    checkAllForBoard(i)
    print("========================================================\n\n")