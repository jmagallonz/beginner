# Guess the Number
# The idea is to generate a random number between 0 and 20 both included
# The user will enter a integer in the range and the program will tell if the number entered is too high, too low
# or the right number.

import random

Number = random.randrange(0, 21)  # Generates a randon number between 0 and 20 both included
# print(Number) #Prints the randomly generated number. Uncomment this line to check that the program works

print("This is a simple game to 'Guess a number'")
print("The computer has randomly generated a number between 0 and 20, both included, and you have to guess it")

count = 1  # Attempt counter
while True:
    try:
        Guess = int(input("Just enter a number between 0 and 20: "))  # User input integer and only an integer
        if Guess > 20 or Guess < 0:  # Check if the integer falls between 0 and 20 both included
            print("Your number is out of bounds. Please enter a number between 0 and 20")
        else:
            break  # Exit while loop when user has entered an integer between 0 and 20

    except:
        print("Please enter a number in numeric format like 5 or 13")
    count += 1

while Number != Guess:  # Guess loop while guess is different from number
    if Number > Guess:
        print("Your Guess is too low")
        while True:
            try:
                Guess = int(input("Enter another number between 0 and 20: "))  # User input integer and only an integer
                if Guess > 20 or Guess < 0:
                    print("Your number is out of bounds. Please enter another number between 0 and 20")
                    count += 1
                else:
                    break
            except:
                print("Please enter a number in numeric format like 5 or 13")
                count += 1
        count += 1
    if Number < Guess:
        print("Your guess is too high")
        while True:
            try:
                Guess = int(input("Enter another number between 0 and 20: "))  # User input integer and only an integer
                if Guess > 20 or Guess < 0:
                    print("Your number is out of bounds. Please enter another number between 0 and 20")
                    count += 1
                else:
                    break
            except:
                print("Please enter a number in numeric format like 5 or 13")
                count += 1
        count += 1

if Number == Guess:  # If you guessed right then...
    print("You guessed right!")
if count == 1:  # ...depending on the number of attempts you get a message or another
    print("WOW! You only needed", count, "attempt! That was lucky!")
if 4 > count > 1:
    print("WOW! You only needed", count, "attempts! Well done!")
if count > 10:
    print("You needed", count, "attempts")
    print("Maybe", count, "attempts are too many!")
if 3 < count <= 10:
    print("You needed", count, "attempts")
