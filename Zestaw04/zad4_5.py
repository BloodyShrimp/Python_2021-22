def odwracanieIterative(L, left, right):
    assert left <= right
    i = (right - left) / 2

    while i > 0:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
        i -= 1
    return L


def odwracanieRecursive(L, left, right):
    if left > right:
        return L
    else:
        L[left], L[right] = L[right], L[left]
        return odwracanieRecursive(L, left + 1, right - 1)
    
L1=["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec", "dziesiec"]
L2=["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec", "dziesiec"]

print(odwracanieIterative(L1, 4, 8))
print(odwracanieRecursive(L2, 7, 9))