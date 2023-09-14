"""EX02 - One-Shot Wordle Loops - A variation of wordle!"""

__author__ = "730652828"


'''
Lines 9 - 11 are a list of emoji characters used for the emoji_string
'''
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


secret_word: str = "python"   #The secret word
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")  #Takes user input 

''' 
Lines 16 and 17 are used to run a while loop to make sure that the computer keeps feeding an input to make
sure the user enters a word that has equivalent length to the secret_word 
'''

while len(word_guess) != len(secret_word):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")
index: int = 0 #this is is used to iterate through the entire word_guess to see how many letters user guessed right
emoji_string: str = "" #empty emoji string
while index < len(secret_word):
    if word_guess[index] == secret_word[index]: #checks if current character in word_guess is equal to current_character in secret_word
        emoji_string = f"{emoji_string}{GREEN_BOX}" #concatenates emoji_string with new emoji character
    #Lines 30 - 41 checks if the character in word_guess is present AT ANY ARBITRARY INDEX in secret_word
    else:
        character_exists: bool = False
        index_present_in_secret_word: int = 0
        while (not character_exists) and (index_present_in_secret_word < len(secret_word)):
            if word_guess[index] == secret_word[index_present_in_secret_word]:
                character_exists = True  #This exits out of the while loop 
            else:
                index_present_in_secret_word += 1 #keeps checking if the character is anywher else in secret_word
        if character_exists:
            emoji_string = f"{emoji_string}{YELLOW_BOX}" #concatenates a yellow emoji
        else:
            emoji_string = f"{emoji_string}{WHITE_BOX}" #concatenates a white emoji
    index += 1
print(emoji_string) #Prints final emoji string
if word_guess != secret_word:
    print("Not quite. Play again soon!") #prints that you DID NOT guess the word on your first try
else:
    print("Woo! You got it!")  #prints that you guessed the word on your first try