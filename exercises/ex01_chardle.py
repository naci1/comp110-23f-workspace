"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730652828"

five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_char: str = input("Enter a single character: ")
if len(single_char) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_char + " in " + five_char_word)
single_char_counter: int = 0
char_index: int = 0
while char_index < 5:
    if five_char_word[char_index] == single_char:
        print(single_char + " found at index " + str(char_index))
        single_char_counter = single_char_counter + 1
    char_index = char_index + 1
if single_char_counter == 0:
    print("No instances of " + single_char + " found in " + five_char_word)
elif single_char_counter == 1:
    print(str(single_char_counter) + " instance of " + single_char + " found in " + five_char_word)
else:
    print(str(single_char_counter) + " instances of " + single_char + " found in " + five_char_word)