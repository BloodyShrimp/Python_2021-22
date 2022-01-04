import sorting_algorithms
import generator
import matplotlib.pyplot as plt
import time

iterations = [10**2, 10**3, 10**4, 10**5 // 2]
random_integers = []
# almost_sorted_integers = []
# reversed_almost_sorted_integers = []
# random_gauss = []
# repeated_integers = []

timing = {}
names_of_sorts = {0: "selectsort", 1: "bubblesort",
                  2: "quicksort", 3: "mergesort"}


for n in iterations:
    random_integers.append(generator.randIntegers(n))
    # almost_sorted_integers.append(generator.almostSortedIntegers(n))
    # reversed_almost_sorted_integers.append(
    #     generator.reversedAlmostSoretdIntegers(n))
    # random_gauss.append(generator.randomGauss(n))
    # repeated_integers.append(generator.repeatedIntegers(n))

all_lists = {"random_integers": random_integers}
#  "almost_sorted_integers": almost_sorted_integers,
#  "reversed_almost_sorted_integers": reversed_almost_sorted_integers,
#  "random_gauss": random_gauss,
#  "repeated_integers": repeated_integers}

for i in range(4):
    for name, values in all_lists.items():
        for list_of_numbers in values:
            numbers = list_of_numbers
            t0 = time.time()
            if i == 0:
                sorting_algorithms.selectsort(numbers, 0, len(numbers) - 1)
            elif i == 1:
                sorting_algorithms.bubblesort(numbers, 0, len(numbers) - 1)
            elif i == 2:
                sorting_algorithms.quicksort(numbers, 0, len(numbers) - 1)
            elif i == 3:
                sorting_algorithms.mergesort(numbers, 0, len(numbers) - 1)
            t1 = time.time()
            timing[len(numbers)] = t1 - t0
        x, y = zip(*timing.items())
        plt.plot(x, y, label=names_of_sorts[i], linestyle = 'dashed', marker = 'o', linewidth = 1)

plt.xscale('log')
plt.xlabel("N")
plt.ylabel("Czas [s]")
plt.legend()
plt.title("Czas sortowania")
plt.savefig("sort_time.png")
plt.savefig("sort_time.svg")
