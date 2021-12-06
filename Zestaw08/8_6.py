import time

tab = {(0, 0): 0.5, (1, 0): 0.0, (0, 1): 1.0}

def P_dynamic(i, j):
    if (i, j) in tab:
        return tab[(i, j)]
    if i > 0 and j == 0:
        tab[(i, j)] = 0.0
        return tab[(i, j)]
    elif i == 0 and j > 0:
        tab[(i, j)] = 1.0
        return tab[(i, j)]
    else:
        tab[(i, j)] = 0.5 * (P_dynamic(i-1, j) + P_dynamic(i, j-1))
        return tab[(i, j)]


def P_recursion(i, j):
    if i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    else:
        return 0.5 * (P_recursion(i-1, j) + P_recursion(i, j-1))


dt0 = time.time()
print(P_dynamic(13, 15))
dt1 = time.time()
print("Dynamicznie czas wykonania: " + str(dt1 - dt0) + "s")
rt0 = time.time()
print(P_recursion(13, 15))
rt1 = time.time()
print("Rekurencja czas wykonania: " + str(rt1 - rt0) + "s")
