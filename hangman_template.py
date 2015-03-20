### GAME OF HANGMAN ###
# wordsEn.txt ile originally sourced from: http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt

# Replace your name here.
__author__ = 'Alpita Masurkar'

# Modules to be imported for this code
import sys
import random
import re

# Algorithm for hangman
#####
# NOTE:
# There are elaborate step by step instructions for each function
# in docstrings that look like this: """ Your code goes here..."""
# When you write your code, remove these steps for a cleaner looking
# code.

"""
Step 1: Read the file
Step 2: Create a list of words out of that file
Step 3: Select length of word based on difficulty
Step 4: Randomly select a word from the list based on output of Step 3
Step 5: At the same time use output of step 3 to create a string/list of "_"
Step 6: Loop till count > 0 or you complete all characters
Step 6a: Get the input from the user
Step 6b: Check for correctness of input (null, len > 1 etc)
Step 6c: Check if this character is in the string selected from step 4
Step 6d: There can be three outcomes of step 8.
     1: If the letter exists & not guessed before ----> replace "_" at the specific position
     2: If letter does not exist then decrement count
     3: else letter is a repeat and print appropriate message. (Make sure you create a list
        of guessed letters so that we can use it for later reference
Step 7: Print appropriate message

"""

# Stores all the possible words from the text file
WORDLIST = []
GUESS_LIST = []
LETTERS_GUESSED = set() # Set is a type of container for data, similar to lists
                        # It does not store repeats
TURNS = 5

### Leave this code here ###
# It populates list from the accompanying word file
def populate_word_file(path_to_file):
    """
    Reads the input file and populates the words list from
    the given file
    :param path_to_file:
    :return:
    """
    with open(path_to_file) as inputfile:
        for line in inputfile:
            WORDLIST.append(line.strip()) # Adds every word from the file to this list


# Helper function to get difficulty level and update game data
def get_difficulty_level():
    """
    Select level of difficulty that
    you want to play with for the game
    :return:
    """
    length_of_word = 0
    while True:
        """
        Your code goes here
        
        Goal is Step 3 from above
        1) Input statement to determine difficulty Easy, Medium, Hard. Also include Quit as an option
        2) if-else to check if input is one of the above
        3) if quit is selected:
        3a) print(Appropriate statement)
        3b) sys.exit() in the next line to terminate code
        4) Else for every difficulty level:
        4a) determine length of word to be guessed
        4b) Update number of turns, use TURNS variable
        5) Other handy keywords in this loop: break/ continue
        """
        
        break # Remove break when you write your code

    return length_of_word


# Helper function that reduces the size of the list from which a random
# word is to be selected for the game
def filter_words(difficulty):
    """

    :param difficulty:
    :return:
    """
    filtered_words = []
    
    """
    Your code goes here.
    
    1) Write a for loop that iterates over wordlist
    2) if length of word in wordlist is equal to return
    value of difficulty level, add it to filtered words list
    """
    
    pass # Remove pass when you write your code
#    return filtered_words # Uncomment return when you write your code


### Leave this code here ###
# This function calls filter_words function above.
# Input given to function is output(return) of get_difficulty_level
def word_selector(difficulty):
    """

    :param difficulty:
    :return:
    """
    pass # Remove pass
    #return random.choice(filter_words(difficulty)) # Uncomment Return

# Helper function that keeps a check on the status of the game
def is_game_complete():
    """

    :param:
    :return:
    """
    game_complete = False
    
    """
    Your code goes here.
    
    Goal: Check Game complete conditions. Game is over when word is guessed
    or when we don't have turns left.
    
    1) Check if "_" is there in GUESS_LIST
    2) If it's not there, that means that we've guessed the word
    2a) game_complete = True
    2b) print appropriate message
    3) Use TURNS variable to check turns
    3a) If no more turns, game_complete = True
    3b) print appropriate message
    4) Check if the user wants to play again or exit when game_complete is True
    4a) If play again, call main()
    4b) If exit, call sys.exit()
    """
    pass

    #return game_complete


# The main logic of the game
def play_game(game_word, level):
    """

    :param game_word, level:
    :return:
    """
    global TURNS, GUESS_LIST # global allows us to use updated results of
                             # common variables from within a function.
                             # Useful when constantly updating a variable inside a function

    while not is_game_complete():        
        guess = get_and_verify_input()
        
        """
        Your code goes here.
        Goal: Check if input letter is in our game word.
        If it is, update the _ _ _ _ _ list with the guessed letter.
        Print this update as a string eg. _ _ a _ _ .
        Also print number of turns remaining.
        
        If it is not, deduct a turn
        At the same time, maintain a list of letters already guessed:
            Use LETTERS_GUESSED to update letter guessed
        If player guesses a letter that is already in guessed list, do
        not deduct a turn, player gets to try again
        
        1) Check if guess in game_word
        1a) If it is, check if it is in guessed letters list.
        If it is not, add the guess to this list
        1b) If letter in guessed list, print appropriate message stating
        letter guessed and number of turns remaining
        2) If guess in word:
        2a) Print all occurrences of the guess in the word. Use this code
        since we have not talked about "re" module
        if guess in game_word:
            occurrences = [m.start() for m in re.finditer(guess, game_word)]
            for i in occurrences:
                GUESS_LIST[i] = guess
                
        Alternatively, you can try something else that has the same end result
        2b i) If guess not in game word and also not in guessed letters,
        deduct a turn. Add guess to letters guessed.
        Print message to let player know input is incorrect
        2b ii) If gueess not in game word but in guessed letters,
        don't deduct a turn, print appropriate message.
        3) Use (" ").join(GUESS_LIST) to print guess list as a string
        """
        break

def get_and_verify_input():
    """

    :param guess:
    :return:
    """

    guess = raw_input("Guess a letter or Press * to exit the game: \n ").lower()
    
    """
    Your code goes here.
    1) If guess is *, print appropriate message and sys.exit() to exit
    2) Check if user input is one character long
    3) If it's not, keep asking above question
    """
    pass
#    return guess

### Leave this code here ###
# Update file path to the Words file

def main():
    global GUESS_LIST
    
    # Add appropriate path to the word file here.
    # wordsEn.txt ile originally sourced from: http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt

    
    #path_to_file = "/Users/Folder_name/Folder_name/Folder_name/wordsEn.txt"
    #populate_word_file(path_to_file)

    level = get_difficulty_level()

    game_word = word_selector(level)
    # Uncomment the following statement to see hangman game word
    # print("The word that was selected is", game_word)

    GUESS_LIST = list(level * "_")
    print((" ").join(GUESS_LIST))

    play_game(game_word, level)

main()
