'''
This module is for you to use to test your implemention of the functions in GuessWord.py

@author: rodger
'''

import GuessWord


if __name__ == '__main__':
    print('Testing createDisplayString')
    lettersGuessed = ['a', 'e', 'i', 'o', 's', 'u']
    misses = 4
    guessedWordAsList = list('s___oo_')
    s = GuessWord.createDisplayString(lettersGuessed, misses, guessedWordAsList)
    print(s)
    print()

    print('Testing updateGuessedWordAsList')
    guessedLetter = 'a'
    secretWord = 'cat'
    guessedWordAsList = ['c', '_', '_']
    expected = ['c', 'a', '_']
    print('Next line should be: ' + str(expected))
    print(GuessWord.updateGuessedWordAsList(guessedLetter, secretWord,
                                    guessedWordAsList))
