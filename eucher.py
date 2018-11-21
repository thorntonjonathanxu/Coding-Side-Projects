import random
import operator

#adding a 

suit_name = ['Clubs', 'Diamonds' ,'Hearts', 'Spades']
usuit_name = [u'\u2663', u'\u2666' ,u'\u2665', u'\u2660']
number_rank = ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

class Card(object):

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        if(len(number_rank[self.number])== 1 or len(number_rank[self.number])> 2):
            return "%s%s" % (number_rank[self.number][0],usuit_name[self.suit])
        else:
            return "%s%s" % (number_rank[self.number],usuit_name[self.suit])

    def getSuit(self):
        return self.suit

    def getNumber(self):
        return self.number

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for number in range(8,14):
                card = Card(suit, number)
                self.cards.append(card)

    def print_deck(self):
        for card in self.cards:
            print(card)
    
    def getDeckSize(self):
        print('The Deck has %s cards' % len(self.cards))
    
    def addCard(self,Card):
        new_card = Card
        return self.cards.append(new_card)

    def removeCard(self,Card):
        return self.cards.pop()

    def shuffle(self):
        return random.shuffle(self.cards)

    def dealCard(self,Hand,Card):
        Hand.addCard(Card)
        return self.removeCard(Card)

class Hand(object):
    def __init__(self):
        self.cards = []

    def addCard(self,Card):
        new_card = Card
        self.cards.append(new_card)

    def removeCard(self,Card):
        self.cards.pop(Card)

    def printHand(self):
        print(self.cards)
    
    def getHandSize(self):
        print('The Hand has %s cards' % len(self.cards))

    def sortHand(self):
        self.cards = sorted(self.cards, key=operator.attrgetter('suit','number'),reverse = False)


# class Game(object):
#     def __init__(self, Deck, ):
#         self.


def main():
    d = Deck()
    d.getDeckSize()
    # Dynamic player count based on input
    # player_count = int(input('How many players are there?'))



    #Defines the each player in the game. Each player has a unique hand that they use during the game.
    player_list = []
    player_count = 4
    for player in range(player_count):
        player = Hand()
        player_list.append(player)

    print("Dealing Cards")
    d.shuffle()
    while(len(d.cards)!=0):
        for players in player_list:
            if(len(d.cards) == 0):
                break
            else:
                d.dealCard(players,d.cards[len(d.cards)-1])
    count = 1
    for players in player_list:
        print('Player {0}'.format(count))
        players.sortHand()
        players.printHand()
        count += 1

    d.print_deck()

main()