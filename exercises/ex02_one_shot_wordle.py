"""EX02 - One-Shot Wordle Loops - A variation of wordle!"""

__author__ = "730652828"

# lines 6-7 are emoji special characters that are going to be used to make the emoji string
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"   
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")   

# the while loop is used to make sure that the secret_word has the same amount of letters as word_guess.
while len(word_guess) != len(secret_word):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
index: int = 0 
emoji_string: str = "" 

# this while loop iterates through the the entire secret_word character by character to see if it matches
while index < len(secret_word):

    # this adds a green_emoji box
    if word_guess[index] == secret_word[index]: 
        emoji_string = f"{emoji_string}{GREEN_BOX}" 
    
    # this else statement is used to figure out whether to add a yellow_emoji or white_emoji
    else:
        character_exists: bool = False
        index_present_in_secret_word: int = 0
        # this conditional checks whether the index is present anywhere else in the string 
        while (not character_exists) and (index_present_in_secret_word < len(secret_word)):
            if word_guess[index] == secret_word[index_present_in_secret_word]:
                # we set the boolean(character_exists) to true and exit out the loop as we found our character
                character_exists = True  
            else:
                index_present_in_secret_word += 1 
        # this iterates the yellow emoji
        if character_exists:
            emoji_string = f"{emoji_string}{YELLOW_BOX}" 
        # this iterates the white emoji
        else:
            emoji_string = f"{emoji_string}{WHITE_BOX}" 
    index += 1

# we finally print the finalized emoji string
print(emoji_string)

# prints a message if the word that we guessed equals the secret_word or not
if word_guess != secret_word:
    print("Not quite. Play again soon!") 
else:
    print("Woo! You got it!")  