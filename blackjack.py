import random

suits = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
         'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


# Creating the Cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


# Creating a Deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # Pops out the last card from the deck
    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Creating a hand
class Hand:
    # Show the number of card dealer and player has
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    # Adding a new card to player's or computer's hand
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    # Adjusting the value of Ace to 1 or 11
    def adjust_for_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Creating chips for placing a bet
class Chips:
    # total is initial chips and bet is the number of chips in bet
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Function to accept the bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('\nHow many chips would you like to bet ? : '))
        except ValueError:
            print('Sorry, Please enter your bet in numbers : ')
        else:
            if chips.bet > chips.total:
                print('Your bet cannot exceed 100')
            else:
                break


# Function to hit or draw another card
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()


# Function to ask hit or stand
def hit_or_stand(deck, hand):
    global playing

    while True:
        ask = input("\nWould you like to HIT or STAND ? \n Please enter 'h' or 's' : ")
        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print('Player stands, Dealer is playing ...')
            playing = False
        else:
            print('Sorry I did not get that!. Please try again!')
            continue
        break


# Inital Cards display
def show_some(player, dealer):
    print("\nDealer's Hand : ")
    print(' < card hidden >')
    print('', dealer.cards[1])
    print("\nPlayer's Hand : ", *player.cards, sep='\n ')


# Final Display of Cards, when player stands
def show_all(player, dealer):
    print("\n Dealer's Hand : ", *dealer.cards, sep='\n ')
    print("Dealer's hand = ", dealer.value)
    print("\n Player's Hand : ", *player.cards, sep='\n')
    print("Player's hand = ", player.value)


# Game Endings
def player_busts(player, dealer, chips):
    print('\nPLAYER BUSTS !!!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('\nHOORAY !!, You won')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('\nDEALER BUSTS')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('\nSORRY! DEALER WINS:(')
    chips.lose_bet()


def push(player, dealer):
    print("It's a PUSH, Player and Dealer tie!")


# Setting up Player Chips (Initializing outside because the chips are to carried on the next round, or else it will reassign to 100)
player_chips = Chips()


# GamePlay
while True:
    print('Welcome to BlackJack !')

    # Create a Shuffle Deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    
    # ask player for bet
    take_bet(player_chips)

    # show cards
    show_some(player_hand, dealer_hand)

    while playing:
        # Ask player to hit or stand
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("\nPlayer's winnings stand at : ", player_chips.total)

    new_game = input("\nWould you like to play again ? Enter 'y' or 'n' : ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for Playing .')
        break










