x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# poprawny

for i in "qwerty": if ord(i) < 100: print (i)
# niepoprawny ciało pętli (jeżeli nie jest instrukcją prostą) musi być w nowej linii poprzedzonej 4 spacjami

for i in "axby": print (ord(i) if ord(i) < 100 else i)
# poprawny ciało pętli to instrukcja prosta