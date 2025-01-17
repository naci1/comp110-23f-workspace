"""EX03 - Structured Wordle - Getting closer to wordle!"""

__author__ = "730652828"


# lines 7-9 are emoji special characters that are going to be used to make the emoji string
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character_to_be_searched: str) -> bool: 
    """This function returns whether or not the character is in the word or not."""
    assert len(character_to_be_searched) == 1
    index: int = 0

    # try to check if a character in the word equals a character to be searched.
    while index < len(word):
        if word[index] == character_to_be_searched:

            # returns a true value if the character is found.
            return True
        index += 1

    # returns a false value if the character is not found.
    return False


def emojified(word_guess: str, secret_word: str) -> str:
    """This function returns the emoji string of the the word you entered and compares it with the secret_word.
       
    It makes use of the contains_char function to see if the word that was guessed is currently present
    in secret_word. If it is present in the same index, then we add a green box to the emoji string.
    If the character is present in the word_guess string but not in the same index, we add a 
    yellow_box. If it's not present at all, we add a white box to the emoji_string.
    """
    assert len(word_guess) == len(secret_word)
    emoji_string: str = ""
    index: int = 0

    # this while loop tries to go through the word_guess and makes an emoji string and appends a green, yellow or white emoji.
    while index < len(secret_word):
        if (contains_char(secret_word, word_guess[index])):
            if word_guess[index] == secret_word[index]:

                # we append a green box if the index is in the same place as secret word
                emoji_string = f"{emoji_string}{GREEN_BOX}"
            else:
                index_present_in_secret_word: int = 0
                found: bool = False
                while (index_present_in_secret_word < len(secret_word)) and (not found):
                    if word_guess[index] == secret_word[index_present_in_secret_word]:
                        found = True
                    else:    
                        index_present_in_secret_word += 1
                if found:

                    # we append a yellow box if the character value is in some other index in word_guess
                    emoji_string = f"{emoji_string}{YELLOW_BOX}"
        else:

            # we append a white box if the character in word_guess is not in secret_word
            emoji_string = f"{emoji_string}{WHITE_BOX}"
        
        # we go to the next index.
        index += 1
    
    # we return the emoji string.
    return emoji_string


def input_guess(expected_length: int) -> str:
    """This function tries to make sure that the word that was entered by the user equals the length of the secret_word. If not, we keep asking the user to input another word equal to word_guess."""
    word_guess: str = input(f"Enter a {expected_length} character word: ")

    # keeps iterating through the while loop to make sure the length of the word_guess is equal to expected_length.
    while len(word_guess) != expected_length:
        word_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return word_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 6
    current_turn: int = 1
    secret_word: str = "codes"
    user_guessed_word: bool = False

    # this allows the user to try up to 6 times to guess the secret_word.
    while current_turn <= turns and (not user_guessed_word):
        print(f"=== Turn {current_turn}/6 ===")
        word_guess: str = input_guess(len(secret_word))
        emoji_string: str = emojified(word_guess, secret_word)
        print(emoji_string)
        if word_guess == secret_word:

            # this boolean allows us to return out of the loop
            user_guessed_word = True
        else:
            current_turn += 1
    
    # prints that we won the world in how many amount of turns.
    if user_guessed_word:
        print(f"You won in {current_turn}/6 turns!")

    # prints that we did not win the worldle.
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    """Used to actually run the program."""
    main()