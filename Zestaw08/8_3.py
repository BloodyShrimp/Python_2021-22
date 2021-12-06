import random
import math

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo. n oznacza liczbę losowanych punktów."""
    points_hit = 0
    for i in range(0, n):
        x = random.random()
        y = random.random()
        radius = math.sqrt(x**2 + y**2)
        if(radius < 1.0):
            points_hit += 1
    myPi = float(points_hit / n) * 4
    print("Przyblizone pi dla n = " + str(n) + " wynosi: " + str(myPi))

def show_pi_from_10_to_10_pow_n(n):
    for i in range(1, n+1):
        calc_pi(10**i)

show_pi_from_10_to_10_pow_n(7)