import math

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru Herona. Długości boków trójkąta wynoszą a, b, c."""
    if (not a < b + c) or (not b < a + c) or (not c < b + a):
        raise ValueError("(" + str(a) + ", " + str(b) + ", " + str(c) + ") " + "Taki trojkat nie istnieje.")
    p = (a + b + c) / 2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

try:
    print(heron(3, 5, 8))
except(ValueError) as E:
    print(E)

try:
    print(heron(4, 9, 6))
except(ValueError) as E:
    print(E)

try:
    print(heron(11, 1, 3))
except(ValueError) as E:
    print(E)

try:
    print(heron(3, 4, 5))
except(ValueError) as E:
    print(E)

try:
    print(heron(15, 9, 12))
except(ValueError) as E:
    print(E)