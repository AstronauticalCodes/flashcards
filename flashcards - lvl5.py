import json
import math


class TermDefExistingError(Exception):
    def __init__(self, var, type):
        self.var = var
        self.type = type

    def __str__(self):
        return f'The {self.type} "{self.var}" already exists. Try again:'


cardDict = {}


def add():
    global userAction
    global cardDict

    if userAction == 'add':
        term = input('The card:\n')
        if term in cardDict:
            print(TermDefExistingError(term, 'term'))
            while True:
                term = input()
                if term not in cardDict:
                    cardDict.update({term: ''})
                    break
                else:
                    print(TermDefExistingError(term, 'term'))
        else:
            cardDict.update({term: ''})

        definition = input('The definition of the card:\n')
        if definition in cardDict.values():
            print(TermDefExistingError(definition, 'definition'))
            while True:
                definition = input()
                if definition not in cardDict:
                    cardDict.update({term: definition})
                    break
                else:
                    print(TermDefExistingError(definition, 'definition'))
        else:
            cardDict.update({term: definition})

        print(f'The pair ("{term}":"{definition}") has been added.')


def remove():
    global userAction
    global cardDict

    if userAction == 'remove':
        cardName = input('Which card?\n')
        if cardName in cardDict:
            del cardDict[cardName]
            print('The card has been removed.')
        else:
            print(f"Can't remove \"{cardName}\": there is no such card.")


def importAction():
    global userAction
    global cardDict

    if userAction == 'import':
        fileName = input('File name:\n')
        try:
            with open(fileName, 'r') as file:
                jsonData = json.load(file)

            for cardName in jsonData:
                cardDict.update({cardName: jsonData[cardName]})

            print(f'{len(jsonData)} cards have been loaded.')

        except FileNotFoundError:
            print('File not found.')


def export():
    global userAction
    global cardDict

    if userAction == 'export':
        fileName = input('File name:\n')
        try:
            with open(fileName, 'w') as file:
                json.dump(cardDict, file)

            print(f'{len(cardDict)} cards have been saved.')

        except FileNotFoundError:
            print('File not found.')


def ask():
    global userAction
    global cardDict

    if userAction == 'ask':
        askTimes = int(input('How many times to ask?\n'))
        keysList = [x for x in cardDict.keys()]

        if len(cardDict) != 0:
            keyValsList = keysList * math.ceil(askTimes / len(cardDict))
            cardVals = [x for x in cardDict.values()]
            for index in range(askTimes):
                userAnswer = input(f'Print the definition of "{keyValsList[index]}":\n')
                if userAnswer == cardDict[keyValsList[index]]:
                    print('Correct!')
                elif userAnswer in cardDict.values():
                    answerIndex = cardVals.index(userAnswer)
                    print(f'Wrong. The right answer is "{cardDict[keyValsList[index]]}", but your definition is correct for "{keysList[answerIndex]}".')
                else:
                    print(f'Wrong. The right answer is "{cardDict[keyValsList[index]]}".')
        else:
            print('No cards to ask from.')


def exitAction():
    global userAction

    if userAction == 'exit':
        print('Bye bye!')
        exit()


while True:
    userAction = input('Input the action (add, remove, import, export, ask, exit):\n')
    add()
    remove()
    importAction()
    export()
    ask()
    exitAction()
    print()
