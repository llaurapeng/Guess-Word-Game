'''
Description:
        You must create a Guess the Word game that
        allows the user to play and guess a secret word.
        See the assignment description for details.

@author: Laura Peng, lp244
'''

import random

#returns which mode the user wants

def handleUserInputDebugMode():
    mode = input("Which mode do you want: (d)ebug or (p)lay: ")

    if mode == "d":
        return True

    return False


#allows the user to pick a length for words in the text file
def handleUserInputWordLength():
    val = input("How many letters in the word you'll guess: ")

    return int(val)


def handleUserInputDifficulty():
    '''
    This function asks the user if they would like
    to play the game in (h)ard or (e)asy mode,
    then returns the corresponding number of misses
    allowed for the game.
    '''

    print("How many misses do you want?")
    mode = input("(h)ard or (e)asy> ")

    if (mode == "h"):
        return 8
    else:
        return 12


def createDisplayString(lettersGuessed, missesLeft, guessedWordAsList):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''

    ind = 0
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alpha = alpha.split(" ")

    for x in lettersGuessed:
        if x in alpha:
            ind = alpha.index(x)
            alpha[ind] = " "
        ind += 1

    ret = ""
    for x in alpha:
        ret += x

    '''
    print( "letters not yet guessed: "+ret)


    print ("misses remaining = " + str (missesLeft))
    print (guessedWordAsList)

    '''
    lettersGuessed = sorted (lettersGuessed)

    newRet = ""
    for x in lettersGuessed:
        newRet+=x +" "


    #print( "letters not yet guessed: "+ret)

    #print ("misses remaining = " + str (missesLeft))
    #print (guessedWordAsList)

    newStr = ""

    for x in guessedWordAsList:
        newStr+=x+" "


    return "letters not yet guessed: "+ret+"\n"+"misses remaining = "+ str (missesLeft)+"\n"+newStr.strip()


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''

    guess = input("letter> ")

    while (guess in lettersGuessed):
        print("you already guessed that")
        guess = input("letter> ")

    return guess


def createTemplate(currTemplate, letterGuess, word):
    index = []
    num = 0

    if letterGuess in word:
        for x in word:
            if x == letterGuess:
                index.append(num)
            num += 1

    # turns currTemplate into a list
    templateLst = []

    currTemplate = "".join(currTemplate)

    for x in currTemplate:
        templateLst.append(x)

    for x in index:
        templateLst[x] = letterGuess

    # print ("".join (templateLst))

    return "".join(templateLst)

#returns the longest template and the list of words that fit in that template which are in alphabetical order
def getNewWordList(currTemplate, letterGuess, wordList, debug):

    words = []
    ret = {}
    val = ""
    wordsDict = {}
    ind = []
    count = 0

    yes = 0
    ret["".join(currTemplate)] = 0
    wordsDict["".join(currTemplate)] = ""

    strCurr = currTemplate

    for x in strCurr:
        if x != "_":
            ind.append(count)
        count += 1

    for x in wordList:

        val = createTemplate(currTemplate, letterGuess, x)
        for y in ind:
            if val[y] == strCurr[y]:
                yes += 1

        '''no = 0
        for x in letterGuess:
            if x in val:
                no =1

        '''

        if val == "".join(currTemplate):
            ret["".join(currTemplate)] += 1
            '''print (x)
            print (wordsDict)
            '''
            wordsDict["".join(currTemplate)] += x + " "

        if val not in ret and letterGuess in x and yes == len(ind):
            ret[val] = 1
            wordsDict[val] = x + " "
        elif letterGuess in x and yes == len(ind):
            ret[val] += 1
            wordsDict[val] += x + " "

    key = list(ret.keys())
    values = list(ret.values())
    maxV = max(ret.values())
    wordsLst = list(wordsDict.values())
    ind = values.index(maxV)
    wordsLst = wordsLst[ind].strip()
    wordsLst = wordsLst.split(" ")

    ret = sorted(ret.items(), key=lambda x: x[0], reverse=False)
    ret = dict(ret)

    ret = dict(ret)


    if debug == True:
        for (x, y) in ret.items():
            print(x, ":", y)

        print ("# keys = " + str (len(ret.keys())))
    return (key[ind], wordsLst)

#updates the value of misses left and if the user guessed wrong
def processUserGuessClever(guessedLetter, guessedWordAsList, missesLeft):
    val = True
    if guessedLetter not in guessedWordAsList:
        missesLeft -= 1
        val = False

    return (missesLeft, val)


def runGame(filename):
    # createTemplate ("____", "O","OBOE")

    # print (getNewWordList("____", "O", ["NOON", "ROOM", "HOOP","OBOE", "ODOR","SOLO", "GOTO"], True))

    '''This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''

    # Your Code Here
    words = open(filename, "r")
    words = words.read()

    miss = 0

    mode = handleUserInputDebugMode()
    leng = handleUserInputWordLength()
    misses = handleUserInputDifficulty()
    guesses = []

    print("letters not yet guessed: ")
    print("abcdefghijklmnopkrstuvwxyz")

    print("misses remaining= " + str(misses))

    wordsLst = []

    for x in words.split():
        if len(x) == int(leng):
            wordsLst.append(x)

    output = ""
    for x in range(int(leng)):
        output += "_"

    randN = random.randint(0, len(wordsLst) - 1)
    secretW = wordsLst[randN]

    output = output.split()

    guessNum = 0
    win = 0
    loss = 0
    stop = "y"
    count = 0

    while (stop == "y"):
        output = "".join(output)

        if mode == True:
            print("(word is " + secretW + ")")
            print("# possible words: " + str(len(wordsLst)))
        else:
            mode = False

        guess = handleUserInputLetterGuess(guesses, output)

        guesses.append(guess)

        newWord = getNewWordList(output, guess, wordsLst, mode)
        output = newWord[0]
        wordsLst = newWord[1]

        randN = random.randint(0, len(newWord[1]) - 1)
        secretW = newWord[1][randN]

        values = processUserGuessClever(guess, output, misses)
        misses = values[0]

        if values[1] == False:
            print("you missed: " + guess + " not in word")
            count+=1

        out = createDisplayString(guesses, misses, output)
        print (out)
        '''
        out = out [0:out.find (",")]

        print ("letters not yet guessed: "+out)
        out = out[out.rfind (","):]
        print("misses remaining = " + str(misses))
        print(output)
        '''

        guessNum += 1
        if misses == 0:
            print("you're hung!!")
            print("word was " + secretW)
            loss += 1

            print("you made " + str(guessNum) + " guesses with " + str(count) + " misses")
            stop = input("Do you want to play again? y or n>")
            if stop == "y":
                mode = handleUserInputDebugMode()
                leng = handleUserInputWordLength()
                strength = handleUserInputDifficulty()
                guesses = []
                count = 0

                print("letters not yet guessed: ")
                print("abcdefghijklmnopkrstuvwxyz")

                if strength == "h":
                    misses = 8
                else:
                    misses = 12
                print("misses remaining= " + str(misses))

                wordsLst = []

                for x in words.split():
                    if len(x) == int(leng):
                        wordsLst.append(x)

                output = ""
                for x in range(int(leng)):
                    output += "_"

                randN = random.randint(0, len(wordsLst) - 1)
                secretW = wordsLst[randN]

                output = output.split()

                guess = 0


        if output.count("_") == 0 and misses > 0:
            print("you win!!")
            print("word was " + secretW)
            print("you made " + str(guessNum) + " guesses with " + str(count) + " misses")
            win += 1
            stop = input("Do you want to play again? y or n>")

            if stop == "y":
                count = 0
                mode = handleUserInputDebugMode()
                leng = handleUserInputWordLength()
                strength = handleUserInputDifficulty()
                guesses = []

                print("letters not yet guessed: ")
                print("abcdefghijklmnopkrstuvwxyz")

                if strength == "h":
                    misses = 8
                else:
                    misses = 12
                print("misses remaining= " + str(misses))

                wordsLst = []

                for x in words.split():
                    if len(x) == int(leng):
                        wordsLst.append(x)

                output = ""
                for x in range(int(leng)):
                    output += "_"

                randN = random.randint(0, len(wordsLst) - 1)
                secretW = wordsLst[randN]

                output = "".join(output)

                guess = 0
            else:
                print ("you won "+str (win)+" games(s) and lost "+str (loss))

    if (win > loss):
        return True
    else:
        return False

    '''
    guess = " "

    count = 0
    miss = 0
    stop = "y"

    miss = 0
    win = 0
    loss = 0

    while (stop == "y"):

        newGuess = handleUserInputLetterGuess(guess, createDisplayString(guess, mode, guessedWord))
        gussedWord = updateGuessedWordAsList(newGuess, secret, guessedWord)

        value = processUserGuess(newGuess, secret, guessedWord, mode)
        mode = value[1]
        gussedWord = value[0]
        guess += newGuess
        count += 1

        if value[2] == False:
            print("you missed: " + newGuess + " not in word")
            miss += 1

        if (guessedWord.count("_") == 0):
            print("you guessed the word: " + secret)
            print("you made " + str(count) + " guesses with " + str(miss) + " misses")
            count = 0
            miss = 0
            win += 1

        if (mode == 0):
            print("you're hung!!")
            print("word is " + secret)
            print("you made " + str(count) + " guesses with " + str(miss) + " misses")
            count = 0
            miss = 0
            loss += 1

        if (guessedWord.count("_") == 0 or mode == 0):
            stop = input("Do you want to play again? y or n>")
            print("You won " + str(win) + " game(s) and lost " + str(loss))

            if (stop == "y"):
                mode = handleUserInputDifficulty()
                secret = getWord(f, random.randint(5, 10))

                lettersGuessed = []
                lettersGuessedStr = ""

                guessedWord = []

                for x in range(len(secret)):
                    guessedWord.append("_")
                    lettersGuessedStr += "_"

                print(secret)
                guess = " "

                count = 0
                miss = 0
                stop = "y"

    if (win > loss):
        return True
    else:
        return False

    '''


if __name__ == "__main__":
    '''
    Running GuessWord.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    runGame('lowerwords.txt')



