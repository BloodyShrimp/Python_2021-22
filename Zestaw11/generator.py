import math
import random
import matplotlib.pyplot as plt

def randIntegers(N):
    numbers = list(range(N))
    random.shuffle(numbers)
    return numbers

def almostSortedIntegers(N):
    numbers = list(range(N))
    displacement = 2
    for i in range(N // 3):
        random_index = random.randint(displacement, N-1)
        temp = numbers[random_index]
        numbers[random_index] = numbers[random_index - displacement]
        numbers[random_index - displacement] = temp
    return numbers

def reversedAlmostSoretdIntegers(N):
    numbers = almostSortedIntegers(N)
    return list(reversed(numbers))

def randomGauss(N):
    numbers = []
    for i in range(N):
        numbers.append(random.gauss(13, 2))
    # plt.plot(numbers)
    # plt.savefig('gaussNumbers.png')
    # plt.clf()
    # plt.hist(numbers, bins = 200)
    # plt.savefig('gauss.png')
    return numbers

def repeatedIntegers(N):
    numbers = []
    for i in range(N):
        numbers.append(random.randint(0, math.floor(math.sqrt(N))))
    return numbers


# N = 100

# with open("RandomIntegers.txt", "w") as output:
#     print(randIntegers(N), file = output)

# with open("AlmostSortedIntegers.txt", "w") as output:
#     print(almostSortedIntegers(N), file = output)
#     # print(list(range(N)), file = output)

# with open("ReversedAlmostSortedIntegers.txt", "w") as output:
#     print(reversedAlmostSoretdIntegers(N), file = output)
#     # print(list(range(N)), file = output)

# with open("Gauss.txt", "w") as output:
#     print(randomGauss(N), file = output)

# with open("RepeatedIntegers.txt", "w") as output:
#     print(repeatedIntegers(N), file = output)
