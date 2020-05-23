# This is a simplified BlackJack Game with a Computer vs AI coded under Object-Oriented Programming.

# Creating card variables of suits ranks values of the deck.

import random
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

StopDealerFunction = False
GameRunning = True

class Player:
    # This class will define the player characteristics.
    def __init__(self, player):
        # Player's name
        self.player = player
        pass

    def __str__(self):
        # Will return Player's name as a a String
        return self.player

class Card:

    # This class will define the specific Card
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{}{}".format(self.rank, self.suit)

class Deck:
    # This class will define the characteristics of the Deck

    def __init__(self):
        self.deckarray = []
        for suit in suits:
            for rank in ranks:
                New_Card = Card(suit, rank)
                self.deckarray.append(New_Card)
        # Starts with an empty list that will be appended
        pass

    def __str__(self):
        for card in self.deckarray:
            print(card)
        return ""
        pass

    def shuffle(self):
        # Shuffles the Deck Randomly
        random.shuffle(self.deckarray)

    def deal(self):
        single_card = self.deckarray.pop()
        return single_card
        pass

class Hand:

    # This Class will keep tracking of the Player's and Dealer's Hands

    def __init__(self):
        self.cards = [] # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self,cards):
        self.cards.append(cards)
        self.value += values[cards.rank]
        if cards.rank == "Ace":
            self.aces += 1 #adds to self.aces
        pass

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        pass

class Chips:

    # This Class will keep track of the Player's and Dealer's Bets

    def __init__(self):
        # This can be set to a default value or supplied by a user input
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        pass

    def lose_bet(self):
        self.total -= self.bet
        pass


# FUNCTIONS DEFINITIONS FOR THE BELOW:

def Take_Bet(Chips):
    print("\nYou currently have: ${}".format(Chips.total))
    Chips.bet = int(input("How much money are you willing to place the initial bet? \n"))
    if Chips.bet > Chips.total or Chips.bet < 0:
        print("You trying to break my code on purpose? Try again!")
        Take_Bet(Chips)


def hit(deck,Hand):
    Hand.add_card(deck.deal())
    Hand.adjust_for_ace()

def hit_stand(deck,Hand,Chips):

    # The Player's hit and stand function.

    global HumanPlaying
    HumanPlaying = True
    global StopDealerFunction
    StopDealerFunction = False

    while HumanPlaying:
        command = input("\nWould you like to Hit or Stand? Enter 'Hit' or 'Stand'. ")
        print("Player's Cards: ")
        if command == "Hit" or command == 'hit':
            hit(deck,Hand)
            for cards in Hand.cards:
                print(cards, end=' ',)

            if Hand.value > 21:
                player_busts(Chips)
                StopDealerFunction = True
                HumanPlaying = False
                break

            if Hand.value == 21:
                player_wins(Chips)
                StopDealerFunction = True
                HumanPlaying = False
                break

        elif command == "Stand" or command == 'stand':
            for cards in Hand.cards:
                print(cards, end=' ',)
            HumanPlaying=False

        else:
            print("Sorry, please try again")
            continue

def dealer_play(deck,Hand,Chips):
    # The dealer will continue to hit until he reaches 17.

    global DealerPlaying
    DealerPlaying = True
    print("\nDealer Cards: ")

    while DealerPlaying:
        if Hand.value < 17:
            hit(deck,Hand)

        elif Hand.value >= 17 and Hand.value <= 21:
            DealerPlaying = False

            if Hand.value == 21:
                DealerPlaying = False
                Chips.lose_bet()

        else:
            if Hand.value > 21:
                DealerPlaying = False
                Chips.win_bet()
                break

    for cards in Hand.cards:
        print(cards, end=' ', )

# These are all the possible win conditions for BlackJack.

def player_busts(Chips):
    HumanPlaying = False
    print("\nPlayer Busts")
    Chips.lose_bet()
    pass


def player_wins(Chips):
    HumanPlaying = False
    print("\nPlayer Wins")
    Chips.win_bet()
    pass


def dealer_busts(Chips):
    HumanPlaying = False
    print("\nDealer Busts")
    Chips.win_bet()
    pass

def dealer_wins(Chips):
    HumanPlaying = False
    print("\nDealer Wins")
    Chips.lose_bet()
    pass

def push():
    print("It's a Draw!")
    pass

def Introduction():
    #Name Formalities and Introduction to the game.
    name = str(input("What is your Name? \n"))

    Player1 = Player(name)

    print("Hello {}".format(Player1))
    print("You've been playing games with people's lives but tonight you will play a game for your life.")
    print("The Game will be BlackJack, you will start of with $100, if you reach $200, you will live with your organs intact, otherwise, if you lose your money, your organs will be "
            "harvested.")
    print("Let the Games begin Bitch \n")
    global Human_Chips
    Human_Chips = Chips()

def main():

    Random_Deck = Deck()
    Random_Deck.shuffle()

    # Activating the Chips Class to keep track of the Player's total and bets.

    Take_Bet(Human_Chips)

    print("Round Begins! \n")

    # Activating the Hand Class to see what deck the player has
    Human = Hand()
    Human.add_card(Random_Deck.deal())
    Human.add_card(Random_Deck.deal())

    Dealer = Hand()
    Dealer.add_card(Random_Deck.deal())
    Dealer.add_card(Random_Deck.deal())

    #Prints out the Player's current hand
    print("Player's Cards: ")
    print(Human.cards[0], Human.cards[1])

    print("\nDealer's Cards: ")
    print("HiddenCard", Dealer.cards[1])

    #Checks the first win conditions to see if either the player or dealer has won!

    if Human.value == 21:
        player_wins(Human_Chips)
        time.sleep(2)
        main()

    elif Dealer.value == 21:
        print(Dealer.cards[0], Dealer.cards[1])
        dealer_wins(Human_Chips)
        time.sleep(2)
        main()

    elif Dealer.value == 21 and Human.value == 21:
        push()
        time.sleep(2)
        main()

    #Ask's the player whether they want to Hit or Stay:
    hit_stand(Random_Deck,Human, Human_Chips)


    #The Dealer will play
    if StopDealerFunction == False:
        dealer_play(Random_Deck,Dealer,Human_Chips)

    #The winning conditions of BlackJack!
    if Human.value > 21:
        print("\nYou have Busted!")

    elif Dealer.value > 21:
        print("\nDealer has Busted!")

    elif Human.value == 21:
        print("\nYou have BlackJacked!")

    elif Dealer.value == 21:
        print("\nDealer has BlackJacked!")

    elif Human.value > Dealer.value and Human.value < 21 and Dealer.value < 21:
        print ("\nPlayer had the higher value, Player Wins!")
        Human_Chips.win_bet()

    elif Dealer.value > Human.value and Dealer.value < 21 and Human.value < 21:
        print ("\nDealer had the higher value, Dealer Wins!")
        Human_Chips.lose_bet()

    elif Human.value == Dealer.value:
        print("\nThis is a Draw!")


    if 200 > Human_Chips.total > 0:
        time.sleep(2)
        main()

    elif Human_Chips.total >= 200:
        print("\nCongratulations, you get to Keep your organs, you piece of shit")
        exit()

    elif Human_Chips.total <= 0:
        print("\n""You Lose! your organs are mine now bitch, see you in hell!")
        exit()

if __name__ == "__main__":
    Introduction()
    main()

