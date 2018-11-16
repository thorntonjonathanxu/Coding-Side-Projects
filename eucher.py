import random


suit_name = ['Clubs', 'Diamonds' ,'Hearts', 'Spades']
usuit_name = ['\023143', '\023146' ,'\023145', '\023140']
number_rank = ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

class Card(object):

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        if(len(number_rank[self.number])== 1):
            return "%s%s" % (number_rank[self.number][0],suit_name[self.suit][0])
        else:
            return "%s%s" % (number_rank[self.number],suit_name[self.suit][0])

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for number in range(13):
                card = Card(suit, number)
                self.cards.append(card)

    def print_deck(self):
        for card in self.cards:
            print(card)
    
    def getDeckSize(self):
        print('The Deck has %s cards' % len(self.cards))
    
    def add_card(self,Card):
        new_card = Card
        return self.cards.append(new_card)

    def remove_card(self,Card):
        return self.cards.pop()

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal_card(self,Hand,Card):
        Hand.add_card(Card)
        return self.remove_card(Card)

class Hand(object):
    def __init__(self):
        self.cards = []

    def add_card(self,Card):
        new_card = Card
        self.cards.append(new_card)

    def remove_card(self,Card):
        self.cards.pop(Card)

    def print_hand(self):
        temp_hand = ''
        for card in self.cards:
            temp_hand += str(card) + ', '
        print(temp_hand)
    
    def getHandSize(self):
        print('The Hand has %s cards' % len(self.cards))

def main():
    d = Deck()
    d.getDeckSize()
    for n in usuit_name:
        print(n)
    player_count = 3
    game = []
    for player in range(player_count):
        player = Hand()
        game.append(player)

    print("Dealing Cards")
    # d.shuffle()
    while(len(d.cards)!=0):
        for players in game:
            if(len(d.cards) == 0):
                break
            else:
                d.deal_card(players,d.cards[len(d.cards)-1])
    count = 1
    for players in game:
        print('Player {0}'.format(count))
        count += 1
        players.print_hand()

    d.print_deck()

main()