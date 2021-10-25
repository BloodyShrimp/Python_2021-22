def draw_n_length_ruler(n):
    ruler = "|"
    segment = ["....|"] * n
    ruler += "".join(segment)
    ruler += "\n0"
    bottom_segment = []
    for i in range(1, n+1):
        numbers_segment = str(i)
        numbers_segment = numbers_segment.rjust(5)
        bottom_segment.append(numbers_segment)
    ruler += "".join(bottom_segment)
    print(ruler)

ruler_length = int(input("Podaj dlugosc miarki: "))
draw_n_length_ruler(ruler_length)
