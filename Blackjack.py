import random

class Cards:
    
    deck = {}
    
    def __init__(self):
        self.create_new_deck()
        self.drawn_cards = []
    
    def create_new_deck(self):
        #Create deck of cards
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

        suits_index = 0
        deck_index = 0
        for i in range(4):
            
            current_suit = suits[suits_index] #Starts with 'Clubs'
            for j in range(13):
                self.deck[deck_index] = (current_suit, j + 1) #use j + 1 for card value since j starts at 0
                deck_index += 1
            
            #increment suit_index to change suit before adding next 13 cards
            suits_index += 1

    def draw_card(self):
        #Get current size of deck
        deck_size = len(self.deck)
        #Get a random number between 0 and deck_size
        random_card_index = random.randint(0,deck_size)
        #keep track of all drawn cards
        while True:
            if random_card_index in self.drawn_cards:
                random_card_index = random.randint(0,deck_size)
            else:
                self.drawn_cards.append(random_card_index)
                break
        #remove dictionary at random index
        random_card = self.deck.pop(random_card_index)
        #return random_card. random_card is a tuple of ('Suit', number)
        return random_card

class Player:

    def __init__(self):
        self.bust = False #Set this true if cards_total_value is greater than 21
        self.black_jack = False #Set this true if cards_total_value is exactly 21
        self.cards_list = []
        self.cards_total_value = 0
        
     
    def hit_me(self, card): #card is a tuple of (str, int). str = suit, int is between 1 and 13
        self.cards_list.append(card)
        #Calculate hand every time you get a new card to see if you busted or hit blackjack
        self.calculate_hand()

    #Loop through self.cards_list and add the cards together
    def calculate_hand(self):
        #Every time this is called, just recalculate the self.cards_total_value instead of trying to just add to the current value
        self.cards_total_value = 0
        for card in self.cards_list:
           temp_card_value = card[1] #get the value from the card tuple
           # If card value is 10,11,12,13, only add 10 to the cards_total_value, else, add card_value
           if temp_card_value in [10,11,12,13]:
               temp_card_value = 10
               #if card value is 1, then count it as Ace = 11
           elif temp_card_value == 1:
               temp_card_value = 11
           self.cards_total_value += temp_card_value

        #After calculating the self.cards_total_value, find out if the player busted, or got blackjack

        if self.cards_total_value > 21:
            self.bust = True
        elif self.cards_total_value == 21:
            self.black_jack = True

class Game:
    def __init__(self):
        self.deck_of_cards = Cards()
        self.deck_of_cards.create_new_deck()

    def play(self):
        

        player1 = Player()
        #Give the player 2 cards from the deck
        player1.hit_me(self.deck_of_cards.draw_card())
        player1.hit_me(self.deck_of_cards.draw_card())

        print(f"Player's hand: {player1.cards_list} ") #list of player's cards
        print(f'Players total: {player1.cards_total_value}') #total value of the player's hand



        dealer = Player()
        dealer.hit_me(self.deck_of_cards.draw_card())
        dealer.hit_me(self.deck_of_cards.draw_card())
        print(f"Dealer's hand: {dealer.cards_list[0]} [(X)]") #list of dealer's cards



        while True:
            if player1.black_jack:
                print(f'BLACK JACK!!! The total was {player1.cards_total_value}.\nYOU WIN!')
                break
            if player1.bust:
                print(f'BUST!!! The total was {player1.cards_total_value}.\nDealer wins!')
                break
            player_input = input('[1]: Hit\n[2]: Stand\n')
            if player_input == '1':
                player1.hit_me(self.deck_of_cards.draw_card())
            elif player_input == '2':
                break
            print(f"Player's hand: {player1.cards_list} ") #list of player's cards
            print(f"Player's total: {player1.cards_total_value}")
        if player1.bust == False and player1.black_jack == False:
            #keep giving the dealer cards until total = 16 or bust
            while True:
                if dealer.bust:
                    print (f"BUST!!! The total was {dealer.cards_total_value}.\nYOU WIN!")
                    print(f'Dealers hand: {dealer.cards_list}') #list of dealer's cards
                    break
                elif dealer.black_jack:
                    print(f"BLACK JACK!!! The total was {dealer.cards_total_value}.\nDEALER WINS!")
                    print(f"Dealer's hand: {dealer.cards_list}") #list of dealer's cards
                    break
                elif dealer.cards_total_value < 16:
                    dealer.hit_me(self.deck_of_cards.draw_card())
                else:
                    if player1.cards_total_value > dealer.cards_total_value:
                        print(f"The player's total is {player1.cards_total_value}. The player wins!")
                    elif dealer.cards_total_value > player1.cards_total_value:
                        print(f"The dealer's total is {dealer.cards_total_value}. The dealer wins!")
                        print(f"Dealer's hand: {dealer.cards_list}") #list of dealer's cards
                    elif player1.cards_total_value == dealer.cards_total_value:
                        print(f"PUSH!!! The dealer's total is {dealer.cards_total_value} and the player's total is {player1.cards_total_value}")
                        print(f"Dealer's hand: {dealer.cards_list}\nplayer's hand: {player1.cards_total_value}")
                    break

run_game = Game()
run_game.play()


