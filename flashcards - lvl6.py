import json
import math


class TermDefExistingError(Exception):
    def __init__(self, var, type):
        self.var = var
        self.type = type

    def __str__(self):
        return f'The {self.type} "{self.var}" already exists. Try again:'


cardDict = {}
errorDict = {}
interactionList = []


def add():
    global userAction
    global cardDict

    if userAction == 'add':
        interactionList.append('add')
        term = input('The card:\n')
        interactionList.append('The card:')
        interactionList.append(term)
        if term in cardDict:
            print(TermDefExistingError(term, 'term'))
            interactionList.append(TermDefExistingError(term, 'term'))
            while True:
                term = input()
                interactionList.append(term)
                if term not in cardDict:
                    cardDict.update({term: ''})
                    break
                else:
                    print(TermDefExistingError(term, 'term'))
                    interactionList.append(TermDefExistingError(term, 'term'))
        else:
            cardDict.update({term: ''})

        definition = input('The definition of the card:\n')
        interactionList.append('The definition of the card:')
        interactionList.append(definition)
        if definition in cardDict.values():
            print(TermDefExistingError(definition, 'definition'))
            interactionList.append(TermDefExistingError(definition, 'definition'))
            while True:
                definition = input()
                interactionList.append(definition)
                if definition not in cardDict:
                    cardDict.update({term: definition})
                    break
                else:
                    print(TermDefExistingError(definition, 'definition'))
                    interactionList.append(TermDefExistingError(definition, 'definition'))
        else:
            cardDict.update({term: definition})

        print(f'The pair ("{term}":"{definition}") has been added.')
        interactionList.append(f'The pair ("{term}":"{definition}") has been added.')
        errorDict.update({term: 0})


def remove():
    global userAction
    global cardDict

    if userAction == 'remove':
        interactionList.append('remove')
        cardName = input('Which card?\n')
        interactionList.append('Which card?')
        interactionList.append(cardName)
        if cardName in cardDict:
            del cardDict[cardName]
            print('The card has been removed.')
            interactionList.append('The card has been removed.')
        else:
            print(f"Can't remove \"{cardName}\": there is no such card.")
            interactionList.append(f"Can't remove \"{cardName}\": there is no such card.")

def importAction():
    global userAction
    global cardDict

    if userAction == 'import':
        interactionList.append(userAction)
        fileName = input('File name:\n')
        interactionList.append('File name:')
        interactionList.append(fileName)
        try:
            with open(fileName, 'r') as file:
                jsonData = json.load(file)

            errorDict.update(jsonData["errors"])
            del jsonData['errors']
            cardDict.update(jsonData)
            # for cardName in jsonData:
            #     cardDict.update({cardName: jsonData[cardName]})

            print(f'{len(jsonData)} cards have been loaded.')
            interactionList.append(f'{len(jsonData)} cards have been loaded.')

        except FileNotFoundError:
            print('File not found.')
            interactionList.append('File not found.')


def export():
    global userAction
    global cardDict

    if userAction == 'export':
        interactionList.append(userAction)
        fileName = input('File name:\n')
        interactionList.append('File name:')
        interactionList.append(fileName)
        try:
            with open(fileName, 'w') as file:
                print(f'{len(cardDict)} cards have been saved.')
                interactionList.append(f'{len(cardDict)} cards have been saved.')
                updatedCardDict = cardDict.update({'errors': errorDict})
                json.dump(cardDict, file)

            del cardDict['errors']

        except FileNotFoundError:
            print('File not found.')
            interactionList.append('File not found.')


def ask():
    global userAction
    global cardDict

    if userAction == 'ask':
        interactionList.append(userAction)
        askTimes = int(input('How many times to ask?\n'))
        interactionList.append('How many times to ask?')
        interactionList.append(str(askTimes))
        keysList = [x for x in cardDict.keys()]

        if len(cardDict) != 0:
            keyValsList = keysList * math.ceil(askTimes / len(cardDict))
            cardVals = [x for x in cardDict.values()]
            for index in range(askTimes):
                userAnswer = input(f'Print the definition of "{keyValsList[index]}":\n')
                interactionList.append(f'Print the definition of "{keyValsList[index]}":')
                interactionList.append(userAnswer)
                if userAnswer == cardDict[keyValsList[index]]:
                    print('Correct!')
                    interactionList.append('Correct!')
                elif userAnswer in cardDict.values():
                    answerIndex = cardVals.index(userAnswer)
                    print(f'Wrong. The right answer is "{cardDict[keyValsList[index]]}", but your definition is correct for "{keysList[answerIndex]}".')
                    interactionList.append(f'Wrong. The right answer is "{cardDict[keyValsList[index]]}", but your definition is correct for "{keysList[answerIndex]}".')
                    errorDict[keyValsList[index]] += 1
                else:
                    print(f'Wrong. The right answer is "{cardDict[keyValsList[index]]}".')
                    interactionList.append(f'Wrong. The right answer is "{cardDict[keyValsList[index]]}".')
                    errorDict[keyValsList[index]] += 1
        else:
            print('No cards to ask from.')
            interactionList.append('No cards to ask from.')


def log():
    global userAction
    global interactionList

    if userAction == 'log':
        interactionList.append(userAction)
        fileName = input('File name:\n')
        interactionList.append('File name:')
        interactionList.append(fileName)
        # print(interactionList)
        joinLst = ' '.join(map(str,interactionList))
        with open(fileName, 'w') as logFile:
            logFile.write(joinLst)

        interactionList.append('The log has been saved.')
        print('The log has been saved.')


def hardestCard():
    global userAction
    global errorDict
    global interactionList

    if userAction == 'hardest card':
        interactionList.append(userAction)
        errorDictVals = [x for x in errorDict.values() if x != 0]
        if len(errorDictVals) > 0:
            maxVal = max(errorDictVals)
            maxValCount = errorDictVals.count(maxVal)
            maxIndices = [index for index, val in enumerate(errorDictVals) if val == maxVal]
            errorKeys = ', '.join(['"' + key + '"' for index, key in enumerate(errorDict.keys()) if index in maxIndices])
            if maxValCount > 1:
                print(f'The hardest cards are {errorKeys}. You have {maxVal} errors answering them.')
                interactionList.append(f'The hardest cards are {errorKeys}. You have {maxVal} errors answering them.')
            else:
                print(f'The hardest card is {errorKeys}. You have {maxVal} errors answering it.')
                interactionList.append(f'The hardest card is {errorKeys}. You have {maxVal} errors answering it.')
        else:
            print('There are no cards with errors.')
            interactionList.append('There are no cards with errors.')


def resetStats():
    global userAction
    global errorDict

    if userAction == 'reset stats':
        interactionList.append(userAction)
        errorDict = {}
        print('Card statistics have been reset.')
        interactionList.append('Card statistics have been reset.')


def exitAction():
    global userAction

    if userAction == 'exit':
        interactionList.append(userAction)
        print('Bye bye!')
        interactionList.append('Bye bye!')
        exit()


while True:
    userAction = input('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')
    interactionList.append('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
    add()
    remove()
    importAction()
    export()
    ask()
    log()
    exitAction()
    hardestCard()
    resetStats()
    print()
