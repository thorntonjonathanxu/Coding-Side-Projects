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
        return self.cards
    
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
    def __init__(self,player_num):
        self.cards = []
        self.score = 0
        self.player_num = player_num

    def addCard(self,Card):
        new_card = Card
        self.cards.append(new_card)

    def removeCard(self,Card):
        self.cards.pop(Card)

    def printHand(self):
        return self.cards
    
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
    player_list = list()
    player_count = 4
    team_One = list()
    team_Two = list()
    count = 1
    for player in range(player_count):
        player = Hand(count)
        if(count % 2 != 0):
            team_One.append(player)
        else:
            team_Two.append(player)
        count += 1
        player_list.append(player)
    print('Team One: {0} \nTeam Two: {1}'.format(team_One,team_Two))

    print("Dealing Cards")
    while(len(d.cards)!=4):
        for players in player_list:
            if(len(d.cards) == 0):
                break
            else:
                d.dealCard(players,d.cards[len(d.cards)-1])

    #Outputs current player hands:
    for players in player_list:
        players.sortHand()
        print('Player {0}: {1}'.format(players.player_num,players.printHand()))
        
    print('Trump: {0}'.format(d.cards[0]))

    currentPlayer = 3

    for set in range(5):
        current_set = {}
        for i in range(4):
            trump = d.cards[0].suit
            played_Card = 10
            played_Card = int(input('Player {0}: Which card do you want to remove?\n{1}\n'.format(player_list[currentPlayer].player_num,player_list[currentPlayer].cards)))

            #Error checking for current player input to validate it is in range
            while(played_Card >= len(player_list[currentPlayer].cards)):
                played_Card = int(input('Sorry that was an invalid input. Please choose a number between 0-{0}. \nCurrent Hand: {1}\n'.format(len(player_list[currentPlayer].cards)-1,player_list[currentPlayer].cards)))
            current_set.update({currentPlayer : player_list[currentPlayer].cards[played_Card]})
            player_list[currentPlayer].removeCard(played_Card)

            print('Player {0}: {1}'.format(player_list[currentPlayer].player_num,player_list[currentPlayer].cards))
            if(currentPlayer == 3):
                currentPlayer = 0
            else:
                currentPlayer += 1
            print('Current Set: {0}'.format(current_set))
        #Calculates the current winner
        # Code goes here
        #
        # winner = 0
        # if(winner % 2 == 0):
            


main()