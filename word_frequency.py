#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# Get and validate the sentence input from the user
def get_sentence():
    while True:
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. Must start with with capital letter, contain at least one word, and end with a punctuation mark.")

#Function to calculate word frequencies
def calculate_frequencies(sentence)
    words = []
    frequencies = []

    cleaned_sentence = re.sub(r'[^\w\s\']', '', sentence).lower()
    word_list = cleaned_sentence.split()

    for word in word_list:
        if word in words:
            index = words.index(word)
            frequencies[index] += 1
        else:
            words.append(word)
            frequencies.append(1)

    return words, frequencies

# Function to print the word frequencies
def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")

# Main function
def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

# Call the main function
if __name__ == "__main__":
    main()
        
