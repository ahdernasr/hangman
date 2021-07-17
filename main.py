import wordList
import random


def main():
    introduce()
    play()


def introduce():
    print("Welcome to Hangman - made with python")
    print("Picking a new word...")


def play():
    triesLeft = 5
    newWord = random.choice(wordList.word_list)
    print(newWord)
    print(len(newWord), " letter word:")
    hiddenString = ""
    possibleInputs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                      "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alreadyTried = []
    for i in range(len(newWord)):
        hiddenString += "_ "
    print (hiddenString)
    while(gameIsWon(hiddenString) == False and triesLeft > 0):
        letter = input("Take a guess... ")

        if (letter not in possibleInputs):
            print("Invalid input try again with a letter")
        elif (letter in alreadyTried):
            print("You've already tried that, try again")
        elif (hiddenString == updateString(letter, newWord, hiddenString)):
            triesLeft -= 1
            print('Wrong! tries left: ', triesLeft)
            alreadyTried += letter
        else:
            hiddenString = updateString(letter, newWord, hiddenString)
            print("Correct!")
            print(hiddenString)
            alreadyTried += letter
    if triesLeft > 0:
        print("Well done, you won!")
        print("Word was: ", newWord)
    else:
        print("You lose!")

    tryAgainPrompt()


def tryAgainPrompt():
    playAgain = ""
    playAgain = input("Play again? yes/no ")
    if playAgain == "yes":
        print("Ok, playing again... ")
        play()
    elif playAgain == "no":
        print("Ok, ending... ")
    else:
        print("Invalid input")
        tryAgainPrompt()


def gameIsWon(string):
    stillHidden = False
    for i in range(len(string)):
        if string[i] == "_":
            stillHidden = True
    return not stillHidden


def updateString(letter, word, hiddenString):
    for i in range(len(word)):
        if letter == word[i]:
            hiddenList = list(hiddenString)
            hiddenList[i*2] = letter
            hiddenString = "".join(hiddenList)
    return hiddenString


main()
