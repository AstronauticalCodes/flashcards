# Write your code here
totalCards = -1
cardDict = {}

def readCardNum():
    global totalCards

    totalCards = int(input('Input the number of cards:\n'))


def createCardDict():
    global totalCards

    for cardIndex in range(1, totalCards + 1):
        cardDict.update({cardIndex: {}})

def termDef():
    global totalCards
    global cardDict

    for cardNum in cardDict:
        cardDict[cardNum].update({'Term': input(f'The term for card #{cardNum}:\n')})
        cardDict[cardNum].update({'Definition': input(f'The definition for card #{cardNum}:\n')})


def checkAnswer():
    global cardDict

    for cardNum in cardDict:
        print(f'Wrong. The right answer is {cardDict[cardNum]["Definition"]}' if input(f'Print the definition of "{cardDict[cardNum]["Term"]}":\n') != cardDict[cardNum]["Definition"] else 'Correct!')


def combiner():
    readCardNum()
    createCardDict()
    termDef()
    checkAnswer()


combiner()
