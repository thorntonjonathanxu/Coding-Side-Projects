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
        self.suitCount = [0,0,0,0]          #Clubs, Diamonds, Hearts, Spades

    def addCard(self,Card):
        new_card = Card
        self.cards.append(new_card)
        self.incrementSuit(Card)

    def removeCard(self,param_Card):
        self.cards.pop(param_Card)
        # self.decrementSuit(param_Card)

    def printHand(self):
        return self.cards
    
    def getHandSize(self):
        print('The Hand has %s cards' % len(self.cards))

    def sortHand(self):
        self.cards = sorted(self.cards, key=operator.attrgetter('suit','number'),reverse = False)

    def incrementSuit(self,param_Card):
        self.suitCount[param_Card.suit] += 1
    
    def decrementSuit(self,param_Card):
        self.suitCount[param_Card.suit] = self.suitCount[param_Card.suit] - 1


# class Game(object):
#     def __init__(self, Deck, ):
#         self.

def main():
    d = Deck()
    d.getDeckSize()
    d.shuffle()
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

    #Dealing cards for the current game. Each player is dealt 5 cards, leaving the deck with 4 cards. 
    #The 
    print("Dealing Cards")
    while(len(d.cards)!=4):
        for players in player_list:
            if(len(d.cards) == 0):
                break
            else:
                d.dealCard(players,d.cards[len(d.cards)-1])
    trump = d.cards[0].suit

    #Outputs current player hands:
    for players in player_list:
        players.sortHand()
        print('Player {0}: {1}'.format(players.player_num,players.printHand()))

    print('Trump: {0}'.format(d.cards[0]))
    print('Trump: {0}'.format(suit_name[d.cards[0].suit]))

    currentPlayer = 0
    #This loop represents a single game played. Each player will play their entire hand and the score would be calculated based on the total number of sets collected.
    for set in range(5):
        current_set = {}
        #This loop represnts a single set. Each play would play a card and the game would calculate the winner for the given set.
        leadingPlay = 0
        for i in range(4):
            print('Current Suits {0}'.format(player_list[currentPlayer].suitCount))
            played_Card = 10            #Used 10 as a number larger than 5
            played_Card = int(input('Player {0}: Which card do you want to remove?\n{1}\n'.format(player_list[currentPlayer].player_num,player_list[currentPlayer].cards)))

            #User input check conditions:
            input_Validitiy = False
            while(input_Validitiy == False):
                if 0 <= played_Card <= len(player_list[currentPlayer].cards):
                    #If it's the first player, suit is set for that set and user input is accepted
                    if(len(current_set) == 0):
                        set_suit = player_list[currentPlayer].cards[played_Card].suit
                        break
                    #Validates that the player isn't playing a card that is out of suit
                    elif(player_list[currentPlayer].suitCount[set_suit] == 0):
                        break
                    elif(player_list[currentPlayer].cards[played_Card].suit == set_suit):
                        break
                    #Throws an error since a player holds a card that matches the current suit but failed to select that option
                    else:
                        played_Card = int(input('You must play a card that matches the current suit. Please chose a {0} in your hand. \nCurrent Hand: {1}\n'.format(suit_name[set_suit],player_list[currentPlayer].cards)))
                #First player slected an input out of range
                elif(len(current_set) == 0):
                    played_Card = int(input('Sorry that was an invalid input. Please choose a number between 0-{0}. \nCurrent Hand: {1}\n'.format(len(player_list[currentPlayer].cards)-1,player_list[currentPlayer].cards)))
                #Second-Forth player selected an input out of range
                else:
                    played_Card = int(input('Sorry that was an invalid input. Please choose a number between 0-{0}. {1} is the current suit for this set. \nCurrent Hand: {2}\n'.format(len(player_list[currentPlayer].cards)-1, suit_name[set_suit],player_list[currentPlayer].cards)))   
            current_set.update({currentPlayer : player_list[currentPlayer].cards[played_Card]})
            player_list[currentPlayer].removeCard(played_Card)

            print('New Hand for: Player {0}: {1}'.format(player_list[currentPlayer].player_num,player_list[currentPlayer].cards))
            

            #If the first player, we assume that the leading play is the first player. 
            if(len(current_set) == 1):
                leadingPlay = current_set[0]
                print(leadingPlay)
            # elif()


            #Assigns the next player in the list
            if(currentPlayer == 3):
                currentPlayer = 0
            else:
                currentPlayer += 1
            print('Current Set: {0}'.format(current_set))
        #Calculates the winner for the current set. 
        
        #
        # winner = 0
        # if(winner % 2 == 0):
    #Calculate the score of the winning team in the game.
    #If Score is 4-1 or 3-2 then increment the winning score by 1
    #If Score is 5-0 increment the winning score by 2
    # print('Team One Score: {0}'.format())
    # print('Team Two Score: {0}'.format())



main()