# To form Pig Latin, you take an English word that begins with a consonant, move that
# consonant to the end, and then add “ay” to the end of the word. If the word begins with
# a vowel, you simply add “way” to the end of the word. One of the most famous Pig Latin
# phrases of all time is “ixnay on the ottenray,” uttered by Marty Feldman in Mel Brooks’s
# comedic masterpiece Young Frankenstein.

# The program will ask the user to insert a word/sentence and the program will "translate" it to Pig Latin
# The program should ignore prepositions, conjunctions, articles, etc.

text = input("Insert text to translate: ")  # What we want to transform to Pig Latin

text = text.split()  # Convert the text string into a list of words
translated = []  # Create a list of translated words

vowels = ["a", "e", "i", "o", "u"]  # List of vowels

no_translate = ["the", "or", "in", "on", "at", "and", "by", "from", "to", "as", "of", "a",
                "an", "with", "is", "what", "when", "how", "who", "which", "with", "why",
                "to", "too", "because", "that", "can", "be", "i", "you", "he", "she", "we"
                "us", "they", "me", "my", "mine", "yours", "hers", "his", "their", "our",
                "have", "can't", "haven't", "not", "yes", "no"]  # List of words not to be translated

for word in text:
    if word.lower() not in no_translate:
        if word[0].lower() in vowels:
            word += "way"
            translated.append(word)
        else:
            word += word[0]  # Copy first letter of each word in text to end of word
            word = word[1:]  # Remove first character of of each word in text
            word += "ay"  # Add "ay" to the end of of each word in text
            translated.append(word)
    else:
        translated.append(word)

translated = " ".join(translated)
print(translated)
