# Hangman game
import random

WORDLIST_FILENAME = "C:/hangman/words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = loadWords()
def hangman(secretWord):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")
    
    guessesLeft = 8
    lettersGuessed = []
    
    while guessesLeft > 0:
        print("You have " + str(guessesLeft) + " guesses left.")
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: " + availableLetters)
        
        word = input("Please guess a letter: ").lower()
        
        if len(word) != 1 or not word.isalpha():
            print("Please enter a single letter.")
            continue
        
        if word in lettersGuessed:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        elif word in secretWord:
            lettersGuessed.append(word)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(word)
            guessesLeft -= 1
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
        
        print("-----------")
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            return  # End the game
    
    print("Sorry, you ran out of guesses. The word was " + secretWord)

def isWordGuessed(secretWord, lettersGuessed):
    return all(char in lettersGuessed for char in secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    return ''.join(char if char in lettersGuessed else '_' for char in secretWord)

def getAvailableLetters(lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return ''.join(letter for letter in alphabet if letter not in lettersGuessed)    

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
