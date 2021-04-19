import random
x = random.randint(1, 100)


print("Welcome to the guessing game! Guess a number between 1 and 100:")


E = x
n = int(input("Your Guess:"))
while True:
       if n > E:
        print("That number is too high, try again:")
        if (n - E) <= 10:
            print("Almost")
            n = int(input("Your guess: "))
        else:
            n = int(input("Your guess: "))
       if n < E:
        print("Unforfortunately that is too low, try again: ")
        if (E - n) <= 10:
            print("Almost")
            n = int(input("Your guess: "))
        else:
            n = int(input("Your guess: "))
       if n == E:
        print(f"You guessed the number! It was {x}")
        break
else:
        pass