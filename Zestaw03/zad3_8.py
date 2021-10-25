first_sequence = ("Tokyo", 13, "Tokyo", 1, 2, 3, 4, 13, "Kyoto", 2001, 2001, 2001, "Shinjuku", "Hokkaido", "Shikoku", "Shinjuku")
second_sequence = ("Honshu", "Kyushu", "Okinawa", 5, 6, 7, 8, 13, 13, 2001, "Tokyo", "Kyoto", "Akihabara")

first_set = set(first_sequence)
second_set = set(second_sequence)

intersection = list(first_set.intersection(second_set))
print(intersection)

union = list(first_set.union(second_set))
print(union)