def find_words_length(text):
    words = text.split()
    length = len("".join(words))
    print("Podany napis: " + text)
    print("Łączna długośc wyrazów = " + str(length))


file_path = input("Podaj nazwę pliku: ")

with open(file_path) as f:
    line = f.read()

find_words_length(line)
