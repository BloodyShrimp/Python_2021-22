def split_underscore(text):
    print("_".join(text))


file_path = input("Podaj nazwę pliku: ")

with open(file_path) as f:
    word = f.read()

split_underscore(word)
