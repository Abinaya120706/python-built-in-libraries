import random

# Get player names
name1 = input("Enter Player 1 Name: ")
name2 = input("Enter Player 2 Name: ")

# Generate random numbers
d1 = random.randint(1, 25)
d2 = random.randint(1, 25)

# Count number of guesses
count1 = 0
count2 = 0

print("\n______", name1, "______")

# Player 1 guessing
while True:
    g = int(input("Enter your guess: "))
    count1 += 1

    if d1 == g:
        print("Correct! You guessed the number.")
        break
    elif g < d1:
        print("Your guess is low")
    else:
        print("Your guess is high")


print("\n______", name2, "______")

# Player 2 guessing
while True:
    g = int(input("Enter your guess: "))
    count2 += 1

    if d2 == g:
        print("Correct! You guessed the number.")
        break
    elif g < d2:
        print("Your guess is low")
    else:
        print("Your guess is high")


# Decide winner (less guesses = winner)
print("\n______ RESULT ______")

if count1 < count2:
    print(name1, "wins! 🎉")
elif count2 < count1:
    print(name2, "wins! 🎉")
else:
    print("It's a tie! 🤝")
