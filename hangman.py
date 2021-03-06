# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import string
import random

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
        else:
            return True


    # FILL IN YOUR CODE HERE AND DELETE "pass"




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    to_be_filled = ''
    for letter in secret_word:
        if letter in letters_guessed:
            to_be_filled = to_be_filled + letter
        else:
            to_be_filled = to_be_filled + '_ '

    return to_be_filled






def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    avalable_letters = string.ascii_lowercase
    remain_letter = " "
    for letter in avalable_letters:
        if letter not in letters_guessed:
            remain_letter = remain_letter+letter


    return remain_letter
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remained_guess = 6
    remained_warning = 3
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %s letters long" % (len(secret_word)))
    while True:


        print("You have %s guesses left" % remained_guess)
        print("You have %s warnings left" % remained_warning)
        print("Available letters: %s" % get_available_letters(letters_guessed))


        one_guessed_letter = input("Please enter a letter: ").lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if one_guessed_letter.isalpha():
            if one_guessed_letter not in letters_guessed:
                letters_guessed.append(one_guessed_letter)
                guessed_word = get_guessed_word(secret_word,letters_guessed)

                if one_guessed_letter in secret_word:
                    print("Good guess: %s," %guessed_word)
                else:
                    if one_guessed_letter in 'aeiou':
                        remained_guess -= 2
                    else:
                        remained_guess -=1

            else:
                if remained_warning > 0:
                    remained_warning -=1
                    print('Oops! You have already guessed this letter. You now have %s warnings and %s guesses' %(remained_warning,  remained_guess))
                else:
                    remained_guess -= 1
                    print('Oops! You have already guessed this letter. You now have %s warnings and %s guesses' %(remained_warning,  remained_guess))

        else:
            if remained_warning>0:
                remained_warning-=1
                print('Oops! This is not valid letter. You now have %s warnings and %s guesses'%(remained_warning,  remained_guess))
            else:
                remained_guess -=1
                print('Oops! This is not valid letter. You now have %s warnings and %s guesses' %(remained_warning,  remained_guess))

        if is_word_guessed(secret_word,letters_guessed):
            unique_letters_in_secret_word = []
            for char in secret_word:
                if char not in unique_letters_in_secret_word:
                    unique_letters_in_secret_word.append(char)

            print("Congrats! you won!!")

        if remained_guess<=0:
            print("You lose and the secret word is %s" %secret_word)
            break








# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
