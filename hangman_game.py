__author__ = 'Alpita Masurkar'
# Word file for this game sourced from http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt
# Built in Python 3. Syntaxes may be slightly different (input instead of raw_input). The rest will work with Python 2

import sys
import random
import re

# Algorithm for hangman

"""
Step 1: Read the file
Step 2: Create a list of words out of that file
Step 3: Select difficulty based on length of the word
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
LETTERS_GUESSED = set()
TURNS = 5

def populate_word_file(path_to_file):
    """
    Reads the input file and populates the words list from
    the given file
    :param path_to_file:
    :return:
    """
    with open(path_to_file) as inputfile:
        for line in inputfile:
            WORDLIST.append(line.strip())

def get_difficulty_level():
    """
    Select level of difficulty that
    you want to play with for the game
    :return:
    """
    length_of_word = 0
    while True:
        difficulty = input("Easy, Medium, Hard or QUIT ? E / M / H / Q? \n ").lower()
        if difficulty not in ['e', 'm', 'h', 'q']:
            continue
        else:
            if difficulty == 'q':
                print("Game Over")
                sys.exit()

            if difficulty == 'e':
                length_of_word = 6
                TURNS = 8
            elif difficulty == 'm':
                length_of_word = 7
                TURNS = 7
            else:
                length_of_word = 8
                TURNS = 6

            break

    return length_of_word

def filter_words(difficulty):
    """

    :param difficulty:
    :return:
    """
    filtered_words = []
    for word in WORDLIST:
         if len(word) == difficulty:
             filtered_words.append(word)

    return filtered_words

def word_selector(difficulty):
    """

    :param difficulty:
    :return:
    """
    return random.choice(filter_words(difficulty))

def is_game_complete():
    """

    :param GUESS_LIST:
    :return:
    """
    game_complete = False
    if "_" not in GUESS_LIST:
        game_complete = True
        print("You are Victorious!")
    elif TURNS == 0:
        game_complete = True
        print("No more turns. Game Over")
    if game_complete:
        decision = input("Play again. Press Y to play or any other letter to Exit: \n").lower()
        if decision == "y":
            main()
        else:
            sys.exit(0)

    return game_complete

def play_game(game_word, level):
    """

    :param game_word:
    :return:
    """
    global TURNS, GUESS_LIST

    while not is_game_complete():

        guess = get_and_verify_input()
        # Check if guess is not in already guessed list and in the game word
        if guess in game_word:
            if guess not in LETTERS_GUESSED:
                # Add to the already guessed list
                LETTERS_GUESSED.add(guess)
            else:
                print("You have already guessed this letter. Enter another guess")
                print("Number of turns remaining", TURNS)
                continue

        # If guess in game word
        if guess in game_word:
            occurrences = [m.start() for m in re.finditer(guess, game_word)]
            for i in occurrences:
                GUESS_LIST[i] = guess
        else:
            if guess not in LETTERS_GUESSED:
                TURNS -= 1
                LETTERS_GUESSED.add(guess)
            else:
                print("You have already guessed this letter. Enter another guess")
                print("Number of turns remaining", TURNS)
                continue

            print("Incorrect input..")

        print((" ").join(GUESS_LIST))
        print("Number of turns remaining", TURNS)



def get_and_verify_input():
    """

    :param guess:
    :return:
    """
    guess = input("Guess a letter or Press * to exit the game: \n ").lower()
    while len(guess) != 1:
        print("Enter only a single alphabet")
        guess = input("Guess a letter or Press * to exit the game: \n ").lower()
    if guess == "*":
        print("Game Over")
        sys.exit()

    return guess


def main():
    global GUESS_LIST
    # Give path to where the word file is located
    
    #path_to_file = "/Users/Folder_Name/Folder_Name/Folder_Name/wordsEn.txt"
    populate_word_file(path_to_file)

    level = get_difficulty_level()

    game_word = word_selector(level)
    print("The word that was selected is", game_word)

    GUESS_LIST = list(level * "_")
    print((" ").join(GUESS_LIST))

    play_game(game_word, level)

main()
