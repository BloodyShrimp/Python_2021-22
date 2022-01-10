def swap(L, left, right):
    item = L[left]
    L[left] = L[right]
    L[right] = item

def quicksort(L, left, right):
    if left >= right:
        return
    swap(L, left, (left + right) // 2)
    pivot = left
    for i in range(left + 1, right + 1):
        if L[i] < L[left]:
            pivot += 1
            swap(L, pivot, i)
    swap(L, left, pivot)
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)

def mediana_sort(L, left, right):
    if left >= right:
        raise ValueError("Incorrect range.")
    lista = L[left:right + 1]
    length = len(lista)
    quicksort(lista, 0, length - 1)
    if length % 2 == 0:
        return (lista[length // 2 - 1] + lista[length // 2]) / 2
    else:
        return lista[length // 2]

def moda_sort(L, left, right):
    if left+1 > right:
        raise ValueError("Incorrect range.")
    mode = None
    mode_amount = 0
    current = 0
    current_amount = 1
    lista = L[left:right + 1]
    length = len(lista)
    quicksort(lista, 0, length - 1)
    while current < length - 1:
        current += 1
        if lista[current] == lista[current-1]:
            current_amount += 1
            if current_amount > mode_amount:
                mode_amount = current_amount
                mode = current
        else:
            current_amount = 1
    if mode == None:
        return None
    else:
        return lista[mode]