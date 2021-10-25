from typing import final


L = [1, 12, 123, 7, 13, 213, 4, 56, 365]
new_L = [str(x).zfill(3) for x in L]
final_L = " ".join(new_L)
print(final_L)
