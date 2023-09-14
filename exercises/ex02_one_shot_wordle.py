"""EX02 - One-Shot Wordle Loops - A variation of wordle!"""

__author__ = "730652828"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


secret_word : str = "python"
word_guess : str = input("What is your 6-letter guess? ")
while len(word_guess)!= len(secret_word) :
    next_guess : str = input("That was not 6 letters! Try again: ")
index : int = 0
emoji_string : str = ""
while index < len(word_guess):
    if word_guess[index] == secret_word[index]:
        print(f"{GREEN_BOX}")
    else:
        print(f"{WHITE_BOX}")
    index +=1

if word_guess != secret_word:
    print("Not quite. Play again soon!")
else :
    print("Woo! You got it!")
        
