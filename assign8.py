"""
Hasana Parker
CS51A: Assignment 8
March 28th, 2022

For Extra Credit, I changed the guessed letters to be formatted differently.
"""

from movies import *
from random import choice


class LabeledExample:
    """
    Example Class
    """

    def __init__(self, line, boolean):
        """
        The Constructor for the class
        :param line: (str) represents ta line of text.
        :param boolean: (bool) indicates whether the example is positive or negative.
        """
        self.line = line
        self.boolean = boolean

    def is_positive(self):
        """
        This function shows whether the line of text is positive or negative
        :return: The boolean inputted in the parameters.
        """
        return self.boolean

    def lowercase(self):
        """
        This function makes the line of text lowercase
        :return:(str) lower case version of the line
        """
        self.line = self.line.lower()

    def get_words(self):
        """
        This function makes the line of text, a list of each word in the line.
        :return: (list) a list of words.
        """
        list_of_words = self.line.split()
        return list_of_words

    def contains_word(self, word):
        """
        This function returns whether the word is in the list of words.
        :param word: (str) a word
        :return: a list of words from the line parameter.
        """
        return word in self.line.split()

    def __str__(self):
        """
        This function makes a string that contains the sentiment of the sentence inputted.
        :return: The string version of the line and it's sentiment
        """
        if not self.boolean:
            sentiment = "negative"
        else:
            sentiment = "positive"

        return self.line + "\t" + sentiment

# Hangman revisited


def generate_underscore(movie):
    """
    Generates a list of dashes corresponding to the movie title
    :param movie: (str) title of movie
    :return: (list) list of dashes
    """

    list_of_dashes = []
    # appends either a space or a dash corresponding to the characters in the movie title to a list
    for char in movie:
        if char == " ":
            list_of_dashes.append(" ")
        else:
            list_of_dashes.append("-")
    return list_of_dashes


class Hangman:
    """
    Hangman Game
    """
    def __init__(self, movie_title):
        """
        This is the constructor function
        :param movie_title: title of the movie
        """
        self.movie_title = movie_title
        self.current = generate_underscore(movie_title)
        self.guessed = []

    def current_state_to_string(self):
        """
        This function changes a list to a string
        :return: (str) the string version
        """
        string = ""
        # concatenates every element in the list and a space to an empty string
        for element in self.current:
            string += element + " "

        return string

    def guess(self, letter):
        """
        This function updates the state of the game as a letter is guessed, and it updates the guessed letters.
        :param letter: Checking the letter inputted as a parameter
        :return: none
        """

        for i in range(len(self.movie_title)):
            if self.movie_title[i] == letter:
                new_letter = letter.upper()
                self.current[i] = new_letter

        if letter not in self.guessed:
            self.guessed.append(letter)
            self.guessed.sort()
        else:
            print("You already guessed this letter!")

    def has_won(self):
        """
        This function checks to see if the user has guessed all the letters in the movie title, and returns a boolean.
        :return: (bool) True or false if the user has won.
        """
        return "-" not in self.current

    def guessed_letters(self):
        """
        This function is the extra credit problem, and it changes the look of the guessed letters to capital and not
        a list with quotation marks.
        :return: (str) the guessed letters as a string
        """
        guess_str = ""
        for alphabet in self.guessed:
            alphabet = alphabet.upper()
            guess_str += alphabet + " "

        return guess_str

    def __str__(self):
        """
        This returns a string that shows the guessed letters and the current movie state.
        :return: (str) with guessed letters and the current state of the game
        """
        return "\n___________________\n" + \
               "Guessed letters: " + \
               self.guessed_letters() + "\n" + \
               "Movie: " + self.current_state_to_string()        


def play_hangman():
    """
    Play the hangman game.    
    """    
    # pick a movie for this game
    (movie, description, year) = choice(get_movies())
    print(movie)

    hangman = Hangman(movie)

    print("*** Movie Hangman ***")
    print("Year: " + str(year))
    print(description)
    
    # keep playing until they've won
    while not hangman.has_won():
        # print out the state of the game
        print(hangman)

        letter = input("Guess a letter: ")
        letter = letter.lower()
        
        # update the state of the game based on the letter
        hangman.guess(letter)

    print("___________________")
    print("You win!")
    print("The movie was: " + movie)
