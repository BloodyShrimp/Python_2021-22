def split_first_char(text):
    words = text.split()
    letters = [c[0] for c in words]
    print("Słowo z pierwszych liter: " + "".join(letters))


def split_last_char(text):
    words = text.split()
    letters = [c[-1] for c in words]
    print("Słowo z ostatnich liter:" + "".join(letters))


file_path = input("Podaj nazwę pliku: ")

with open(file_path) as f:
    line = f.read()

split_first_char(line)
split_last_char(line)
