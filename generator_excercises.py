# Generator Excercises

# Problem 1
# Create a generator, primes_gen that generates prime numbers starting from 2.

def primes_gen():
    for num in range(20000):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num


# gen = primes_gen()
# for _ in range(10):
#     print(next(gen), end=' ')


# Expected output
# 2 3 5 7 11 13 17 19 23 29
# ----------------------------------------------------------------------------

# Problem 2
# Create a generator, unique_letters that generates unique letters from
# the input string. It should generate the letters in the same order as
# from the input string.

def unique_letters(inputStr):
    usedChars = set()
    for i in range(len(inputStr)):
        if not inputStr[i] in usedChars:
            usedChars.add(inputStr[i])
            yield inputStr[i]


for letter in unique_letters('hello'):
    print(letter, end=' ')
# Expected output
# h e l o
