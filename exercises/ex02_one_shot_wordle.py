"""EX02 - One-Shot Wordle Loops - A variation of wordle!"""

__author__ = "730652828"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"   
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")   

while len(word_guess) != len(secret_word):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
index: int = 0 
emoji_string: str = "" 
while index < len(secret_word):
    if word_guess[index] == secret_word[index]: 
        emoji_string = f"{emoji_string}{GREEN_BOX}" 
    
    else:
        character_exists: bool = False
        index_present_in_secret_word: int = 0
        while (not character_exists) and (index_present_in_secret_word < len(secret_word)):
            if word_guess[index] == secret_word[index_present_in_secret_word]:
                character_exists = True  
            else:
                index_present_in_secret_word += 1 
        if character_exists:
            emoji_string = f"{emoji_string}{YELLOW_BOX}" 
        else:
            emoji_string = f"{emoji_string}{WHITE_BOX}" 
    index += 1
print(emoji_string) 
if word_guess != secret_word:
    print("Not quite. Play again soon!") 
else:
    print("Woo! You got it!")  