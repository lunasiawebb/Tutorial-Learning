import random as rand
import timeit

class Tarot:
    majorArcana=["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", 
                 "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man",
                 "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]
    suits=["Wands", "Cups", "Swords", "Pentacles"]
    ranks=["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight","Queen", "King"]
    direction=["Up", "Down"]

    def getCard(self):
        randomNum = rand.randint(1,78)
        cardDirection = rand.choice(self.direction)

        if randomNum <= 22:
            card = rand.choice(self.majorArcana)
        else:
            randomSuit = rand.choice(self.suits)
            randomRank = rand.choice(self.ranks)
            card = randomRank + " of " + randomSuit

        return card + " facing " + cardDirection

def drawdeck(size):


if __name__=="__main__":
    cards = Tarot()
    print(cards.getCard())
