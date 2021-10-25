def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    longest_word_length = len(longest_word)
    print("Podany napis: " + text)
    print("Najdłuższy wyraz: " + longest_word)
    print("Długość najdłuższego wyrazu = " + str(longest_word_length))


file_path = input("Podaj nazwę pliku: ")

with open(file_path) as f:
    line = f.read()

find_longest_word(line)
