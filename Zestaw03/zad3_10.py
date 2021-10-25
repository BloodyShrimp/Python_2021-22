roman_dictionary1 = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100,
                     "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

roman_dictionary2 = {}
roman_dictionary2["M"] = 1000
roman_dictionary2["CM"] = 900
roman_dictionary2["D"] = 500
roman_dictionary2["CD"] = 400
roman_dictionary2["C"] = 100
roman_dictionary2["XC"] = 90
roman_dictionary2["L"] = 50
roman_dictionary2["XL"] = 40
roman_dictionary2["X"] = 10
roman_dictionary2["IX"] = 9
roman_dictionary2["V"] = 5
roman_dictionary2["IV"] = 4
roman_dictionary2["I"] = 1

romans_tuple = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
                ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
roman_dictionary3 = dict(romans_tuple)

def roman2int(roman_number, roman_dictionary):  # zakładam że podana liczba rzymska jest zapisana poprawnie
    roman_number = roman_number.upper()         # sprawdzenie poprawnosci liczby byloby troche meczace a nie wiem czy jest to wymagane
    result = 0

    while roman_number:
        if roman_number[:2] in roman_dictionary:
            result += roman_dictionary[roman_number[:2]]
            roman_number = roman_number[2:]
        elif roman_number[:1] in roman_dictionary:
            result += roman_dictionary[roman_number[:1]]
            roman_number = roman_number[1:]
        else:
            print("W liczbie jest symbol nieuzywany w systemie rzymskim.")
            return
    print("Liczba w systemie arabskim:", result)

roman_numeral = str(input("Podaj liczbe rzymska: "))
roman2int(roman_numeral, roman_dictionary1)