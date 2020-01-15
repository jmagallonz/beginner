#  Program to count number of letters in a text.
#  Create a poor's man bar chart of the letters used in the text.

import string  # To import ascii lowercase letters

text = input("Enter text to count letters: ").lower()
print("\n")  # Simply add a break line
letters = string.ascii_lowercase  # String of low case letters
letters_list = list(letters)  # Transform it in a list
letter = []  # Create an empty list to fill later

text_str = "".join(sorted(text.replace(" ", "")))  # Change the text to a string and remove spaces

counter_count = 0
for i in letters_list:  # Loop to count how many times each letter appears and create sublists of letters
    letter.append(list(i * text_str.count(i)))
    counter_count += 1

counter_chart = 0
for i in letters_list:  # # Loop create the charts with the added count of letters
    print(letters_list[counter_chart], " = ",text_str.count(i), " ", letter[counter_chart])
    counter_chart += 1

