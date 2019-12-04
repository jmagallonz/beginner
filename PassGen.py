#  The idea is to create a password generator
#  It will include letters (upper and lowercase), numbers and symbols
#  Minimum length will be 6 characters and maximum set to 128 (but this should be easily editable in the code)

import string  # Imports sets of letters, numbers and symbols
import random  # Imports pseudorandom functionality

upper = string.ascii_uppercase  # List of uppercase letters
lower = string.ascii_lowercase  # List of lowercase letters
number = string.digits  # List of numbers
symbol = string.punctuation  # List of symbols

characters_list = [lower, number]  # List of all selected characters; lower case and numbers are pre-selected by default

password = [random.choice(lower), random.choice(number)]  # We make compulsory that the password has at least 1
# lowercase letter and 1 number

# Ask user if she wants to include capitals
case = None
while case not in ("Yes", "yes", "Y", "y", "No", "no", "N", "n"):
    case = input("Do you want to include uppercase letters in your password? Yes/No: ")
    if case not in ("Yes", "yes", "Y", "y", "No", "no", "N", "n"):
        print("Please enter ""Yes"" or ""No""")

case = case.lower()  # Normalise user answer

if (case == "yes") or (case == "y"):  # If answer is yes, upper is included
    password = [random.choice(lower), random.choice(number), random.choice(upper)]
    characters_list.append(upper)

# Ask user if she wants to include symbols
symbols = None
while symbols not in ("Yes", "yes", "Y", "y", "No", "no", "N", "n"):
    symbols = input("Do you want to include symbols in your password? Yes/No: ")
    if symbols not in ("Yes", "yes", "Y", "y", "No", "no", "N", "n"):
        print("Please enter ""Yes"" or ""No""")

symbols = symbols.lower()  # Normalise user answer

if (symbols == "yes") or (symbols == "y"):  # If answer is yes, upper is included
    password.append(random.choice(symbol))
    characters_list.append(symbol)

random.shuffle(password)  # Randomise the order of the user selected characters

#  How many characters should the password have?
min_cha = 6  # Minimum number of characters for the password
max_cha = 128  # Maximum number of characters for the password

print("Please, enter a number between", min_cha, "and", max_cha)
while True:
    try:
        num_cha = int(input("How many characters should the password have? "))
        if num_cha > min_cha and num_cha < max_cha and isinstance(num_cha, int):
            break
    except:
        print("Please, enter a number between", min_cha, "and", max_cha)

characters_str = ''.join(str(e) for e in characters_list)  # Convert character_list into string for random selection

while len(password) < num_cha:  # Add characters up to the number specified by the user
    password.append(random.choice(characters_str))

password = ''.join(str(x) for x in password)  # Transform the list into a string of characters

print("Your password is: ", password)



