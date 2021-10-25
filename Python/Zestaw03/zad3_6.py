def draw_box(length, width):
    box = []
    base_row_1 = "+" + "---+" * length
    base_row_2 = "|" + "   |" * length
    for i in range(width):
        box.append(base_row_1)
        box.append(base_row_2)
    box.append(base_row_1)
    pretty_box = "\n".join(box)
    print(pretty_box)

width = int(input("Podaj wysokosc prostokata: "))
length = int(input("Podaj dlugosc prostokata: "))
draw_box(length, width)