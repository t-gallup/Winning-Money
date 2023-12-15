"""
Write me a program in python that simulates a game of blackjack. 
The program will first ask for the number of decks being used, the static amount of money the user wants 
to bet for each round, and the amount of money they start off with. The all the cards in the deck will 
be stored in an integer array. 
Cards 2-10 will be represented as an integer, Aces will be A, Jacks will be J, Queens will be Q, 
and Kings will be K. 
The program will then run the first hand. For each hand the following will happen. 
The program will then output for the player each card that they can see, so it will output the dealers 
face up card and the players two cards. 
The program will then give the player the option to stay, double, split, or hit based on the rules 
and continue to give the options until either bust or they choose stay. 
If the player 
If the player hits the program will output all the cards they have on hand.
If the player busts the hand is over. If the player chooses stay the dealer will then play their part of
the hand based on the rules. The program will then determine the payouts and the hand ends. Once the hand ends, 
all the cards that were played in that round are outputted and then put in the discarded cards array. Those cards 
are then deleted from the deck array. The amount of money the player has left is updated and outputted, and then 
the next hand is played.
The game ends when the player is out of money. 

This is an example of what the beginning of the game and the first hand should look like:

Please enter the number of decks: 6
Please enter the amount of money you would like to start with: 100
Please enter the amount of money to bet on each hand: 5

Hand: 1
Dealers face up card: J
Your cards: 5 6

Would you like to hit, stay, or double: hit

Your cards: 5 6 7
Would you like to hit or stay: stay

Dealers cards: J 5
Dealer hits: J 5 7
Dealer busts

Your payout: 5
Your total money: 105

Hand: 2


Problem:
Reshuffle
"""

#Dealer hits on Soft 17
#Reshuffle happens halfway through the deck
#Cannot Double after a split

import random

# Function to create a deck with specified number of decks
def create_deck(num_decks):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    deck = ranks * 4 * num_decks
    random.shuffle(deck)
    return deck

# Function to get the rank of a card
def get_card_rank(card):
    return card

# Function to get the value of a card
def get_card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11  # Returning 11 for Aces by default
    else:
        return card

# Function to adjust the value of the hand based on Aces
def adjust_for_aces(hand):
    hand_values = []
    for card in hand:
        hand_values.append(get_card_value(card))
    while sum(hand_values) > 21 and 11 in hand:
        index = hand_values.index(11)
        hand_values[index] = 1

# Function to check for blackjack
def check_blackjack(hand):
    return get_true_sum(hand) == 21

# Get the number value of a hand
def get_true_sum(hand):
    hand_values = []
    for card in hand:
        hand_values.append(get_card_value(card))
    # Adjust for aces
    while sum(hand_values) > 21 and 11 in hand_values:
        index = hand_values.index(11)
        hand_values[index] = 1
    return sum(hand_values)
    

# Function to output strategy based on our cards and dealers card
def best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money):
    dealer_value = get_card_value(dealer_hand[0])

    if current_bet + bet_amount > total_money or len(player_hand) > 2:
        double_down_hit = 'hit'
        split_hit = 'hit'
        double_down_stay = 'stay'
    else:
        double_down_hit = 'double down'
        split_hit = 'split'
        double_down_stay = 'double down'
        
    if player_hand[0] == player_hand[1]:
        if 'A' in player_hand:
            return 'split'
        if 10 in player_hand:
            return 'stay'
        if 9 in player_hand:
            if dealer_value == 7 or dealer_value == 10 or dealer_value == 'A':
                return 'stay'
            else:
                return 'split'
        if 8 in player_hand:
            return 'split'
        if 7 in player_hand:
            if dealer_value >= 2 or dealer_value <=7:
                return 'split'
            else:
                return 'hit'
        if 6 in player_hand:
            if dealer_value == 2:
                return split_hit
            if dealer_value >= 3 and dealer_value <= 6:
                return 'split'
            else:
                return 'hit'
        if 5 in player_hand:
            if dealer_value == 10 or dealer_value == 'A':
                return 'hit'
            else:
                return double_down_hit
        if 4 in player_hand:
            if dealer_value == 5 or dealer_value == 6:
                return split_hit
            else:
                return 'hit'
        if 3 in player_hand or 2 in player_hand:
            if dealer_value == 2 or dealer_value == 3:
                return split_hit
            if dealer_value >= 4 or dealer_value <= 7:
                return 'split'
            else:
                return 'hit'
            
    #soft hands
    if 'A' in player_hand:
        if 9 in player_hand or 8 in player_hand:
            return 'stay'
        if 7 in player_hand:
            if dealer_value >= 3 and dealer_value <= 6:
                return double_down_stay
            if dealer_value == 7 or dealer_value == 8 or dealer_value == 2:
                return 'stay'
            else:
                return 'hit'
        if 6 in player_hand:
            if dealer_value >= 3 and dealer_value <= 6:
                return double_down_hit
            else:
                return 'hit'
        if 5 in player_hand or 4 in player_hand:
            if dealer_value >= 4 and dealer_value <= 6:
                return double_down_hit
            else:
                return 'hit'
        if 3 in player_hand or 2 in player_hand:
            if dealer_value == 5 and dealer_value == 6:
                return double_down_hit
            else:
                return 'hit'
    
    player_value = get_true_sum(player_hand)
    


    if player_value <= 8:
        return 'hit'
    elif player_value == 9:
        if dealer_value >= 3 and dealer_value <= 6:
            return double_down_hit
        return 'hit'
    elif player_value == 10:
        if dealer_value <= 9:
            return double_down_hit
        else:
            return 'hit'
    elif player_value == 11:
        return double_down_hit
    elif player_value == 12:
        if dealer_value >= 4 and dealer_value <= 6:
            return 'stay'
        else:
            return 'hit'
    elif player_value == 13 or player_value == 14:
        if dealer_value <= 6:
            return 'stay'
        else:
            return 'hit'
    elif player_value == 15:
        if dealer_value <= 6:
            return 'stay'
        elif dealer_value == 10 and len(player_hand) <= 2:
            return 'surrender'
        else:
            return 'hit'
    elif player_value == 16:
        if dealer_value <= 6:
            return 'stay'
        elif dealer_value >= 9 and len(player_hand) <= 2:
            return 'surrender'
        else:
            return 'hit'
    else:
        return 'stay'
    

# Function to play a hand of blackjack
def play_blackjack(deck, used_cards, bet_amount, total_money):
    player_hand = []
    dealer_hand = []

    # Deal initial cards
    player_hand.append(get_card_rank(deck.pop()))
    dealer_hand.append(get_card_rank(deck.pop()))
    player_hand.append(get_card_rank(deck.pop()))
    dealer_hand.append(get_card_rank(deck.pop()))


    if check_blackjack(player_hand):
        if check_blackjack(dealer_hand):
            return 0
        else:
            return int(bet_amount * 1.5)

    # Check for if dealer has blackjack in the initial hand
    if check_blackjack(dealer_hand):
        if check_blackjack(player_hand):
            return 0
        else:
            return -bet_amount

    current_bet = bet_amount
    # Check for pair to enable splitting
    strategy = best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money)
    if strategy == 'surrender':
        return -bet_amount//2
    if player_hand[0] == player_hand[1]:
        if strategy == 'split':
            current_bet += bet_amount
            split_hands = [[player_hand[0]], [player_hand[1]]]
            for i in range(len(split_hands)):
                split_hands[i].append(deck.pop())
            hand_count = -1
            while hand_count < len(split_hands) - 1:
                hand_count += 1
                strategy = best_strategy(split_hands[hand_count], dealer_hand, current_bet, bet_amount, total_money)
                # if len(split_hands[hand_count]) == 2 and split_hands[hand_count][0] == split_hands[hand_count][1]:
                  
                if strategy == 'split':
                    current_bet += bet_amount
                    split_hands.append([split_hands[hand_count][1]])
                    split_hands[hand_count] = [split_hands[hand_count][0]]
                    split_hands[hand_count].append(deck.pop())
                    split_hands[len(split_hands)-1].append(deck.pop())
                if strategy == 'surrender':
                    split_hands[hand_count] = [0, 0]
                elif strategy == 'double down':
                    bet_amount *= 2
                    card = deck.pop()
                    split_hands[hand_count].append(card)
                    used_cards.append(card)
                    # adjust_for_aces(split_hands[hand_count])

                else:
                    while get_true_sum(split_hands[hand_count]) < 21:
                        strategy = best_strategy(split_hands[hand_count], dealer_hand, current_bet, bet_amount, total_money)
                        if strategy == 'hit':
                            card = deck.pop()
                            split_hands[hand_count].append(card)
                            used_cards.append(card)
                            # adjust_for_aces(split_hands[hand_count])
                            if get_true_sum(split_hands[hand_count]) > 21:
                                break
                        elif strategy == 'stay':
                            break
                        else:
                            print(strategy)
                            print(split_hands)
                            print(dealer_hand)
                            break

            # Dealer's turn
            while ('A' in dealer_hand and get_true_sum == 17) or get_true_sum(dealer_hand) < 18:
                card = deck.pop()
                dealer_hand.append(card)
                used_cards.append(card)
                # adjust_for_aces(dealer_hand)

            # Determine the winner for each split hand
            total_winnings = 0
            for i in range(len(split_hands)):
                player_value = get_true_sum(split_hands[i])
                dealer_value = get_true_sum(dealer_hand)

                if player_value == 0:
                    total_winnings -= bet_amount//2
                elif player_value > 21:
                    total_winnings -= bet_amount
                elif dealer_value > 21 or player_value > dealer_value:
                    total_winnings += bet_amount
                elif player_value < dealer_value:
                    total_winnings -= bet_amount
                

            return total_winnings

    # Player's turn for non-split hand
    if strategy == 'double down':
        current_bet += bet_amount
        bet_amount *= 2
        card = deck.pop()
        player_hand.append(card)
        used_cards.append(card)
        # adjust_for_aces(player_hand)

        if get_true_sum(player_hand) > 21:
            return -bet_amount
    else:
        while get_true_sum(player_hand) < 21:
            strategy = best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money)
            if strategy == 'hit':
                card = deck.pop()
                player_hand.append(card)
                used_cards.append(card)
                # adjust_for_aces(player_hand)
                if get_true_sum(player_hand) > 21:
                    return -bet_amount
            elif strategy == 'stay':
                break
            else:
                print(strategy)
                print(player_hand)
                print(dealer_hand)
                break

    # Dealer's turn
    while ('A' in dealer_hand and get_true_sum == 17) or get_true_sum(dealer_hand) < 18:
        card = deck.pop()
        dealer_hand.append(card)
        used_cards.append(card)
        # adjust_for_aces(dealer_hand)

    # Determine the winner for the non-split hand
    player_value = get_true_sum(player_hand)
    dealer_value = get_true_sum(dealer_hand)

    if player_value > 21:
        return -bet_amount
    elif dealer_value > 21 or player_value > dealer_value:
        return bet_amount
    elif player_value < dealer_value:
        return -bet_amount
    else:
        return 0

# Main game loop
def main():
    num_decks = 6
    total_money = 100
    min_bet = 10
    overall_winnings = 0

    deck = create_deck(num_decks)
    used_cards = []

    round_number = 1
    penetration = .5
    reshuffle_amount = penetration * len(deck)
    wins = 0
    losses = 0

    num_games = int(input("Enter number of simulations: "))
    curr_game = 0
    while curr_game < num_games:

        while total_money >= min_bet:
            # TODO: Change bet amount for different counts
            if curr_game >= num_games:
                break
            bet_amount = 10
            if bet_amount < min_bet or bet_amount > total_money:
                continue
            result = play_blackjack(deck, used_cards, bet_amount, total_money)
            curr_game += 1
            if result > 0:
                wins += 1
            if result < 0: 
                losses += 1
            overall_winnings += result
            total_money += result
            round_number += 1
            if len(deck) < reshuffle_amount:
                deck = create_deck(num_decks)
        total_money = 100
    print("Win %: ", wins/(wins + losses))
    print("Total winnings: ", overall_winnings)


if __name__ == "__main__":
    main()
