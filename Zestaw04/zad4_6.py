def sum_seq(sequence):
    result = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            result += sum_seq(i)
        else:
            result += i
    
    return result

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
expected = 45
given = sum_seq(seq)
assert expected == given
print(given)