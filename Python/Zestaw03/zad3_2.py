L = [3, 5, 4] ; L = L.sort()
# metoda sort zwraca None tracimy naszą listę

x, y = 1, 2, 3
# przypisujemy elementy krotki 3-elementowej do 2 zmiennych nie wiadomo gdzie przypisać ostatni element krotki

X = 1, 2, 3 ; X[1] = 4
# nie można zmieniać zawartości krotki

X = [1, 2, 3] ; X[3] = 4
# lista nie ma pozycji na indeksie 3

X = "abc" ; X.append("d")
# append to metoda listy a nie stringa

L = list(map(pow, range(8)))
# nie podajemy argumentu exponent dla funkcji pow()