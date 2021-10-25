line = "tokyo to piekne miasto ale najdłuższe słowo to konstantynopolitańczykowianeczka"
split_line = line.split()
sorted_length = " ".join(sorted(split_line, key=len))
sorted_alphabetically = " ".join(sorted(split_line))
print("Line posortowane alfabetycznie: " + sorted_alphabetically)
print("Line posortowane długością: " + sorted_length)
