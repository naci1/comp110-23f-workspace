"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730652828"

five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word)!= 5:
  print("Error: Word must contain 5 characters")
  exit()
single_char: str = input("Enter a single character: ")
if len(single_char)!= 1:
  print("Error: Character must be a single character.")
  exit()
print("Searching for " + single_char + " in " + five_char_word)
character_counter: int = 0
char_index = 0
while char_index < 5:
  if five_char_word[char_index] == "e":
    print(single_char + "found at index" + str(char_index + 1))
    character_counter = character_counter + 1
    char_index = char_index + 1
if character_counter == 0:
  print("No instances of " + single_char + " found in " + five_char_word)
elif character_counter == 1:
  print(str(character_counter) + " instance of " + single_char + " found in " + five_char_word)
else:
  print(str(character_counter) + " instances of " + single_char + " found in " + five_char_word)




