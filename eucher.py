import random

class Card(object):

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __repr__(self):
        return "%s of %s" % (self.suit, self.number)


class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for number in range(6):
                card = Card(suit, number)
                self.cards.append(card)

    def print_deck(self):
        for card in self.cards:
            print(card)
        print('The Deck has %s cards' % len(self.cards))
    
    def add_card(self,Card):
        new_card = Card
        return self.cards.append(new_card)

    def remove_card(self,Card):
        return self.cards.pop()

    def shuffle(self):
        return random.shuffle(self.cards)

    def deal_card(self,hand,Card):
        hand.add_card(Card)
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
        for card in self.cards:
            print(card)
        print('The Hand has %s cards' % len(self.cards))

def main():
    d = Deck()
    d.print_deck()
    player1 = Hand()
    player2 = Hand()
    player3 = Hand()
    player4 = Hand()
    print("Dealing Cards")
    d.shuffle()
    while(len(d.cards)!=0):
        d.deal_card(player1,d.cards[len(d.cards)-1])
        d.deal_card(player2,d.cards[len(d.cards)-2])
        # d.deal_card(player3,d.cards[len(d.cards)-3])
        # d.deal_card(player4,d.cards[len(d.cards)-4])
    print('Player 1:')
    player1.print_hand()
    print('Player 2:')
    player2.print_hand()
    # print('Player 3:')
    # player3.print_hand()
    # print('Player 4:')
    # player4.print_hand()
    d.print_deck()

main()