def count_words(text):
    count = len(text.split())
    print("Podany napis:\n" + text)
    print("Ilosc słów w napisie to: " + str(count))


file_path = input("Podaj nazwę pliku: ")

with open(file_path) as f:
    line = f.read()

count_words(line)
