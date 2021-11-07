def flatten(sequence):
    L = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            L.extend(flatten(i))
        else:
            L.append(i)

    return L

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
given = flatten(seq)
assert expected == given
print(given)