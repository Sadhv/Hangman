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
import random
import string

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
        if char in letters_guessed: 
            return True
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    string = ""
    for i in secret_word:
        if i in letters_guessed:
            string += i
        else:
            string += "_"
    return string

    
            



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    string = "abcdefghijklmnopqrstuvwxyz"
    not_used = ""
    for char in string:
        if char not in letters_guessed:
            not_used += char
    return not_used
    
    

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
    print('Welcome to the game Hangman!')
    length_of_letter = len(secret_word)

    print( 'I am thinking of a word that is', length_of_letter, 'letters long.' )

    left_num_guesses, left_num_worning = 6, 3
    letters_guessed,list1 = [], ['a', 'i', 'u', 'e', 'o']
    num_of_try = 0
    num_of_secretword = len(secret_word)
    
    print('----------')

    while left_num_guesses > 0:
        print( 'You have', left_num_guesses, 'guesses left.' )
        print( 'Available letters:', ''.join(get_available_letters(letters_guessed)) )

        input_letter_all = str(input('Please guess a letter:'))
        input_letter = input_letter_all.lower()

        available_list = get_available_letters(letters_guessed)

        if input_letter in available_list :
            if input_letter in list(secret_word):
                letters_guessed.append(input_letter)
                print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            else :
                letters_guessed.append(input_letter)
                print('Oops! That letter is not in my word: ', 
                    get_guessed_word(secret_word, letters_guessed))
                if input_letter in list1 :
                    left_num_guesses -= 2
                else :
                    left_num_guesses -= 1

        elif input_letter in letters_guessed :
            letters_guessed.append(input_letter)
            if left_num_worning > 0 :
                left_num_worning -= 1
                print("Oops! You've already guessed that letter. You now have", left_num_worning,
                "warnings:", get_guessed_word(secret_word, letters_guessed))
            else :
                left_num_guesses -=1
                print("Oops! You've already guessed that letter. You now have", left_num_guesses, 
                "gueses:", get_guessed_word(secret_word, letters_guessed))   

        else :
            letters_guessed.append(input_letter)
            if left_num_worning > 0 :
                left_num_worning -= 1
                print('Oops! That is not a valid letter. You have', left_num_worning, 
                'warning(s) left: ', get_guessed_word(secret_word, letters_guessed))
            else :
                left_num_guesses -= 1
                print('Oops! That is not a valid letter. You have', left_num_guesses, 
                'guesses left: ', get_guessed_word(secret_word, letters_guessed))

        num_of_try += 1
        
        comparison = len((get_guessed_word(secret_word, letters_guessed))) - (get_guessed_word(secret_word, letters_guessed)).count("_") - (get_guessed_word(secret_word, letters_guessed)).count(" ")

        if comparison == num_of_secretword :
            print('Congratulations, you are a winner! '
            'Your total score for this game is: ', num_of_try)
            break

        print('----------')
    
    if left_num_guesses == 0 :
        print("YOU lost!")

    return



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
    string = my_word.replace(' ', '')
    used = string.replace('_', '')

    for a, b in zip(string, other_word):
        if (a != '_' and a != b) or (a == '_' and b in used):
            return False
    return True



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
    matches = ''
    for word in wordlist: 
        if match_with_gaps(my_word, word): 
            matches += word 
            matches += ' '
    if matches == '':  
        print('No matches found.')
    else: 
        print('Possible word matches are: '+ str (matches))




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
    hangman_with_hints(secret_word)
