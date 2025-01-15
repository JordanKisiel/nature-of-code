import random
import string

alphabet = list(string.ascii_lowercase)

answer = "cat"
guess = ""

iterations = 0

while guess != answer:
    letter1 = alphabet[random.randint(0, 25)]
    letter2 = alphabet[random.randint(0, 25)]
    letter3 = alphabet[random.randint(0, 25)]

    guess = f"{letter1}{letter2}{letter3}"
    print(f"guess: {guess}")
    iterations += 1

print(f"iterations: {iterations}")
