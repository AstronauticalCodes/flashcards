class FlashCard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def play(self, answer, term=''):
        if answer == self.definition:
            return f'Correct!'
        elif term != '':
            return f'Wrong. The correct answer is "{self.definition}", but your definition is correct for "{term}".'
        else:
            return f'Wrong. The correct answer is "{self.definition}".'


cardDict = {}


class DictCards:

    def __init__(self, totalCards):
        self.totalCards = totalCards
        self.cardList = self.CreateCardDict()

    def CreateCardDict(self):
        global cardDict

        cardList = []
        for cardNum in range(1, self.totalCards + 1):
            term = input(f'The term for card #{cardNum}:\n')
            if term in cardDict:
                while True:
                    reTerm = input(f'The term "{term}" already exists. Try again:\n')
                    term = reTerm
                    if reTerm not in cardDict:
                        cardDict.update({reTerm: ''})
                        break
            else:
                cardDict.update({term: ''})

            definition = input(f'The definition for card #{cardNum}:\n')
            if definition in cardDict.values():

                while True:
                    reDef = input(f'The definition "{definition}" already exists. Try again:\n')
                    definition = reDef
                    if reDef not in cardDict.values():
                        cardDict.update({term: reDef})
                        break
            else:
                cardDict.update({term: definition})

            cardList.append(FlashCard(term, definition))
        return cardList


    def ShowCards(self):
        valList = [x for x in cardDict.values()]
        for card in self.cardList:
            userDef = input(f'Print the definition of "{card.term}":\n')
            if userDef == card.definition:
                print(card.play(userDef))
            elif userDef in cardDict.values():
                index = valList.index(userDef)
                print(card.play(userDef, term=self.cardList[index].term))
            else:
                print(card.play(userDef))


def main():
    user = int(input('Input the number of cards:\n'))
    userCards = DictCards(user)
    userCards.ShowCards()

if __name__ == '__main__':
    main()
