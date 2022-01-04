def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item

def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        item = L[k]
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item

def bubblesort(L, left, right):
    for i in range(left, right):
        for j in range(left, right):
            if L[j] > L[j+1]:
                swap(L, j+1, j)

def quicksort(L, left, right):
    if left >= right:
        return
    swap(L, left, (left + right) // 2)   # element podziału
    pivot = left                      # przesuń do L[left]
    for i in range(left + 1, right + 1):   # podział
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def mergesort(L, left, right):
    """Sortowanie przez scalanie."""
    if left < right:
        middle = (left + right) // 2   # wyznaczanie środka 
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie

def merge(L, left, middle, right):
    """Łączenie posortowanych sekwencji z wartownikami."""
    n1 = middle - left + 1
    n2 = right - middle
    A = [None] * (n1 + 1)   # o jeden więcej
    B = [None] * (n2 + 1)   # o jeden więcej
    for i in range(n1):
        A[i] = L[left + i]
    for i in range(n2):
        B[i] = L[middle + 1 + i]
    A[n1] = float("inf")   # wartownik
    B[n2] = float("inf")   # wartownik
    i, j = 0, 0
    for k in range(left, right+1):
        if A[i] <= B[j]:
            L[k] = A[i]
            i += 1
        else:
            L[k] = B[j]
            j += 1