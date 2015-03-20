# 4 questions in this assignment.

# Note: When guessing output, try not to print before guessing
# This will help you understand the logic behind the code

# Question 1
"""
Guess the output for the following program
"""

common_passwords = ["123456", "qwerty", "forgot"]
password = "password"
if password in common_passwords:
    print password, "in the list"
else:
    print password, "not in the list"
    
"""
Now substitute "password" in password with a raw_input statement.
User tests three types of input:
    1) "qwerty"
    2) "letmein"
    3) Hit Enter key (Do not enter anything ie.- string length = 0)
Think of cases 2 and 3, write an if-else loop inside the else loop above.
(Hint: Use len(string) to handle the cases.)
Handle input a) if length of input is 6 char long b) if it's not 6 char long
Print appropriate message and also handle the case where
The code should be able to print a statement for any of the three cases
above.

"""

# Once you have a working code, test your new code in the following function
# Remember to comment out input statement
# Follow indentation 4- spaces when pasting if-else loop here.

common_passwords = ["123456", "qwerty", "forgot"]

def password_checker(password):
    """
    New code goes here
    """
    pass  # Remove pass when you test your code

password_checker("qwerty")
password_checker("letmein")
password_checker("")


# Question 2

"""
Guess the output for the following program
"""
first_list = ["apple", "out", "ore"]
second_list = []

for word in first_list:
    print word

first_list.append("uggle")
print first_list

new_list = ["are", "iff", "ail", "acks"]
first_list[3] = new_list[2]
print first_list

"""
Goal: Create a second list that looks like this: [snapple, snout, snore, snail, snare]
1) Add "are" to the first_list
2) Write a for loop that iterates over the first list
3) Create a new word that matches the condition seen in the second list
4) Now add new word to this list
5) Print a list that looks like the Goal above
"""

# Once you have a working code, test your new code in the following function

first_list = ["apple", "out", "ore"]
first_list.append("ail")

def list_tester(lst):
    """
    New code goes here
    """
    pass  # Remove pass when you test your code
    #return second_list # Uncomment return statement when you test your code
    
print list_tester(first_list)

# Question 3
"""
Guess the output for the following program
"""
game_over = False
turns = 5

while not game_over:
    ask_input = raw_input("Enter a letter: \n")
    print "You entered", ask_input
    turns -= 1
    if turns == 0:
        game_over = True
        print "No more turns. Game Over."
    
"""
Use the code logic given above
1) Print Number of turns remaining in the same line as you entered, word
2) new_string is another variable that forms a strings out of words we enter
2a) After the print statement, write code that adds our input word to this string
eg. if I enter words "Betty", "is", "a", "great", "singer" one at a time as input,
new string should look like this after every turn: a) Betty b) Betty is c) Betty is a
d) Betty is a great e) Betty is a great singer
"""
# Once you have a working code, test your new code in the following function

turns = 5

def game_over_check():
    global turns
    game_over = False
    new_string = ""
    
    while not game_over:
        word = string_maker() # Gets input from string_maker
        
        """
        New code goes here
        """
        break  # Remove break when you test your code here
#    return new_string # Uncomment return when you write your code

def string_maker():
    ask_input = raw_input("Enter a word: \n")
    return ask_input

print game_over_check()
