def make_n_length_ruler(n):
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
    return ruler


def make_box(length, width):
    box = []
    base_row_1 = "+" + "---+" * length
    base_row_2 = "|" + "   |" * length
    for i in range(width):
        box.append(base_row_1)
        box.append(base_row_2)
    box.append(base_row_1)
    pretty_box = "\n".join(box)
    return pretty_box


ruler_length = int(input("Podaj dlugosc miarki: "))
print(make_n_length_ruler(ruler_length))


width = int(input("Podaj wysokosc prostokata: "))
length = int(input("Podaj dlugosc prostokata: "))
print(make_box(length, width))
