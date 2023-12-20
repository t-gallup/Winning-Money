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

import random

# Function to create a deck with specified number of decks
def create_deck(num_decks):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    # ranks = [5]
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
def best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money, true_count):
    dealer_value = get_card_value(dealer_hand[0])
    if current_bet + bet_amount > total_money or len(player_hand) > 2:
        double_down_hit = 'hit'
        split_hit = 'hit'
        double_down_stay = 'stay'
    else:
        double_down_hit = 'double down'
        split_hit = 'split'
        double_down_stay = 'double down'
    
    if get_card_value(player_hand[0]) == get_card_value(player_hand[1]) and len(player_hand) == 2:
        dealer_value = get_card_value(dealer_hand[0])
        if 'A' in player_hand:
            return 'split'
        if 10 in player_hand:
            if dealer_hand == 4 and true_count >= 6:
                return 'split'
            elif dealer_hand == 5 and true_count >= 5:
                return 'split'
            elif dealer_hand == 6 and true_count >= 4:
                return 'split'
            else:
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
        if 9 in player_hand:
            return 'stay'
        if 8 in player_hand:
            if dealer_hand == 4 and true_count >= 3:
                return 'hit'
            elif dealer_hand == 5 and true_count >= 1:
                return 'hit'
            elif dealer_hand == 6 and true_count >= 1:
                return 'hit'
            else:
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
            elif dealer_value == 2 and true_count >= 1:
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
    


    if player_value <= 7:
        return 'hit'
    if player_value == 8:
        if dealer_value == 6 and true_count >= 1:
            return double_down_hit
        else:
            return 'hit'
    elif player_value == 9:
        if dealer_value >= 3 and dealer_value <= 6:
            return double_down_hit
        elif dealer_value == 7 and true_count >= 3:
            return double_down_hit
        return 'hit'
    elif player_value == 10:
        if dealer_value <= 9:
            return double_down_hit
        elif dealer_value >= 10 and true_count >= 4:
            return double_down_hit
        else:
            return 'hit'
    elif player_value == 11:
        if dealer_value == 11 and true_count < 1:
            return 'hit'
        return double_down_hit
    elif player_value == 12:
        if dealer_value >= 4 and dealer_value <= 6:
            return 'stay'
        #TODO: Check if next 2 cases switch to stay or double
        elif dealer_value == 2 and true_count >= 3:
            return 'stay'
        elif dealer_value == 3 and true_count >= 2:
            return 'stay'
        elif dealer_value == 4 and true_count <= 0:
            return 'hit'
        else:
            return 'hit'
    elif player_value == 13 or player_value == 14:
        if dealer_value <= 6:
            return 'stay'
        elif dealer_value == 2 and true_count <= -1 and player_value == 13:
            return 'hit'
        else:
            return 'hit'
    elif player_value == 15:
        if dealer_value <= 6:
            return 'stay'
        #TODO: Not sure if this is what chart is saying to deviate here
        elif dealer_value == 9:
            if len(player_hand) == 2 and true_count >= 2:
                return 'surrender'
            else:
                return 'hit'
        elif dealer_value == 10:
            if len(player_hand) == 2 and true_count > 0:
                return 'surrender'
            elif true_count >= 4:
                return 'stay'
            else:
                return 'hit'
        elif dealer_value == 11:
            if len(player_hand) == 2 and true_count >= 2:
                return 'surrender'
            else:
                return 'hit'
        else:
            return 'hit'
    elif player_value == 16:
        if dealer_value <= 6:
            return 'stay'
        elif dealer_value == 7:
            return 'hit'
        elif dealer_value == 8:
            if len(player_hand) == 2 and true_count >= 4:
                return 'surrender'
            else:
                return 'hit'
        # TODO: Not sure on this one either
        elif dealer_value == 9:
            if true_count > -1 and len(player_hand) == 2:
                return 'surrender'
            elif true_count >= 4:
                return 'stay'
            return 'hit'
        elif dealer_value == 10:
            if len(player_hand) == 2:
                return 'surrender'
            elif true_count >= 0:
                return 'stay'
            else:
                return 'hit'
        else:
            if len(player_hand) == 2:
                return 'surrender'
            else:
                return 'hit'
    else:
        return 'stay'
    

def change_running_count(card, curr_running_count):
    value = get_card_value(card)
    if value >= 2 and value <= 6:
        return curr_running_count + 1
    if value == 10 or value == 11:
        return curr_running_count - 1
    if value >= 7 and value <= 9:
        return curr_running_count

# Function to update the amount of each card seen
def update_used_cards(new_cards, used_cards):
    for card in new_cards:
        if card in used_cards:
            used_cards[card] += 1
        else:
            used_cards[card] = 1

def get_running_count(used_cards, deck):
    running_count = 0
    for card in used_cards:
        value = get_card_value(card)
        if value >= 2 and value <= 6:
            running_count += used_cards[card]
        if value == 10 or value == 11:
            running_count -= used_cards[card]
    #Divide the total count by the number of decks left to get the true count
    return running_count // (len(deck) // 52)

# Function to play a hand of blackjack
def play_blackjack(deck, used_cards, bet_amount, total_money):
    # print(running_count)
    player_hand = []
    dealer_hand = []

    # Deal initial cards
    card = deck.pop()
    # running_count = change_running_count(card, running_count)
    player_hand.append(get_card_rank(card))
    update_used_cards([card], used_cards)

    card = deck.pop()
    # running_count = change_running_count(card, running_count)
    dealer_hand.append(get_card_rank(card))
    update_used_cards([card], used_cards)

    card = deck.pop()
    # running_count = change_running_count(card, running_count)
    player_hand.append(get_card_rank(card))
    update_used_cards([card], used_cards)

    dealer_hand.append(get_card_rank(deck.pop()))

    if check_blackjack(player_hand):
        if check_blackjack(dealer_hand):
            # running_count = change_running_count(dealer_hand[1], running_count)
            update_used_cards([dealer_hand[1]], used_cards)
            
            return 0
        else:
            # Dealer card is only shown if they have a 10, face card, or ace
            if get_card_value(dealer_hand[0]) >= 10:
                # running_count = change_running_count(dealer_hand[1], running_count)
                update_used_cards([dealer_hand[1]], used_cards)
            return int(bet_amount * 1.5)

    # Check for if dealer has blackjack in the initial hand
    if check_blackjack(dealer_hand):
        if check_blackjack(player_hand):
            # running_count = change_running_count(dealer_hand[1], running_count)
            update_used_cards([dealer_hand[1]], used_cards)
            return 0
        else:
            # running_count = change_running_count(dealer_hand[1], running_count)
            update_used_cards([dealer_hand[1]], used_cards)
            return -bet_amount

    current_bet = bet_amount
    
    strategy = best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money, get_running_count(used_cards, deck))
    if strategy == 'surrender':
        # Dealer's cards don't get shown if you surrender
        # print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))
        # running_count = change_running_count(dealer_hand[1], running_count)
        # print(f"\nRunning Count: {running_count}")
        return -bet_amount//2
    # Check for pair to enable splitting
    if get_card_value(player_hand[0]) == get_card_value(player_hand[1]):
        strategy = best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money, get_running_count(used_cards, deck))
        if strategy == 'split':
            current_bet += bet_amount
            split_hands = [[player_hand[0]], [player_hand[1]]]
            for i in range(len(split_hands)):
                card = deck.pop()
                # running_count = change_running_count(card, running_count)
                split_hands[i].append(card)
                update_used_cards([card], used_cards)
            hand_count = -1
            split_count = 1
            while hand_count < len(split_hands) - 1:
                hand_count += 1
                if len(split_hands[hand_count]) == 2 and split_hands[hand_count][0] == split_hands[hand_count][1]:
                    strategy = best_strategy(split_hands[hand_count], dealer_hand, current_bet, bet_amount, total_money, get_running_count(used_cards, deck))
                    if strategy == 'split':
                        if split_count < 3:
                            current_bet += bet_amount
                            split_hands.append([split_hands[hand_count][1]])
                            split_hands[hand_count] = [split_hands[hand_count][0]]
                            split_hands[hand_count].append(deck.pop())
                            split_hands[len(split_hands)-1].append(deck.pop())
                            split_count += 1
                            hand_count -= 1
                            continue
                        # Janky error case for trying to split past max splits
                        else:
                            while get_true_sum(split_hands[hand_count]) < 21:
                                if strategy == 'hit':
                                    card = deck.pop()
                                    split_hands[hand_count].append(card)
                                    update_used_cards([card], used_cards)
                                    if get_true_sum(split_hands[hand_count]) > 21:
                                        break
                                elif strategy == 'stay':
                                    break
                                else:
                                    break
                            break

                
                # print(f"\nHand {hand_count + 1}: {' '.join(map(str, split_hands[hand_count]))}")
                strategy = best_strategy(split_hands[hand_count], dealer_hand, current_bet, bet_amount, total_money, get_running_count(used_cards, deck))
                if strategy == 'surrender':
                    split_hands[hand_count] = 'surrender'
                elif strategy == 'double down':
                    bet_amount *= 2
                    card = deck.pop()
                    # running_count = change_running_count(card, running_count)
                    split_hands[hand_count].append(card)
                    update_used_cards([card], used_cards)
                    # adjust_for_aces(split_hands[hand_count])

                    # if sum(split_hands[i]) > 21:
                    #     print("You busted")
                    #     return -bet_amount
                else:
                    while get_true_sum(split_hands[hand_count]) < 21:
                    #     print(f"\nHand {hand_count + 1}: {' '.join(map(str, split_hands[hand_count]))}")
                        strategy = best_strategy(split_hands[hand_count], dealer_hand, current_bet, bet_amount, total_money, get_running_count(used_cards, deck))
                        if strategy == 'hit':
                            card = deck.pop()
                            # running_count = change_running_count(card, running_count)
                            split_hands[hand_count].append(card)
                            update_used_cards([card], used_cards)
                            # adjust_for_aces(split_hands[hand_count])
                            if get_true_sum(split_hands[hand_count]) > 21:
                                break
                        elif strategy == 'stay':
                            break
                        else:
                            print(strategy)
                            print("Your hand: ", split_hands[hand_count])
                            print("Dealer hand: ", dealer_hand)
                            break

            # Dealer's turn
            #Add dealers second card to running count, done here because it isn't shown until now
            # running_count = change_running_count(dealer_hand[1], running_count)
            update_used_cards([dealer_hand[1]], used_cards)
            while ('A' in dealer_hand and get_true_sum == 17) or get_true_sum(dealer_hand) < 18:
                card = deck.pop()
                # running_count = change_running_count(card, running_count)
                dealer_hand.append(card)
                update_used_cards([card], used_cards)
                # adjust_for_aces(dealer_hand)

            # Determine the winner for each split hand
            total_winnings = 0
            for i in range(len(split_hands)):
                if split_hands[i] == 'surrender':
                    total_winnings -= bet_amount//2
                    continue
                player_value = get_true_sum(split_hands[i])
                dealer_value = get_true_sum(dealer_hand)

                if player_value > 21:
                    total_winnings -= bet_amount
                elif dealer_value > 21 or player_value > dealer_value:
                    total_winnings += bet_amount
                elif player_value < dealer_value:
                    total_winnings -= bet_amount

            return total_winnings

    # Player's turn for non-split hand
    strategy = best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money, get_running_count(used_cards, deck))
    if strategy == 'double down':
        current_bet += bet_amount
        bet_amount *= 2
        card = deck.pop()
        # running_count = change_running_count(card, running_count)
        player_hand.append(card)
        update_used_cards([card], used_cards)
        # adjust_for_aces(player_hand)

        if get_true_sum(player_hand) > 21:
            # You don't see dealers hand if you bust
            return -bet_amount
    else:
        while get_true_sum(player_hand) < 21:
            strategy = best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money, get_running_count(used_cards, deck))
            if strategy == 'hit':
                card = deck.pop()
                # running_count = change_running_count(card, running_count)
                player_hand.append(card)
                update_used_cards([card], used_cards)
                # adjust_for_aces(player_hand)
                if get_true_sum(player_hand) > 21:
                    # You don't see dealers hand if you bust
                    return -bet_amount
            elif strategy == 'stay':
                break
            else:
                print(strategy)
                print("Your hand: ", player_hand)
                print("Dealer hand: ", dealer_hand)
                break


    # Dealer's turn
    #Add dealers second card to running count, done here because it isn't shown until now
    # running_count = change_running_count(dealer_hand[1], running_count)
    update_used_cards([dealer_hand[1]], used_cards)
    while ('A' in dealer_hand and get_true_sum == 17) or get_true_sum(dealer_hand) < 18:
        card = deck.pop()
        # running_count = change_running_count(card, running_count)
        dealer_hand.append(card)
        update_used_cards([card], used_cards)
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
    used_cards = {}

    round_number = 1
    penetration = .5
    reshuffle_amount = penetration * len(deck)

    # running_count = 0

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

    # while total_money >= min_bet:
    #     bet_amount = int(input("Please enter the amount of money to bet on this hand (>=" + str(min_bet) + "): "))
    #     if bet_amount < min_bet or bet_amount > total_money:
    #         continue
    #     print(f"\nHand: {round_number}")
    #     result = play_blackjack(deck, used_cards, bet_amount, total_money)
    #     total_money += result
    #     print(f"\nYour total money: {total_money}")
    #     print(f"\nUsed cards: {used_cards}")
    #     round_number += 1
    #     if len(deck) < reshuffle_amount:
    #         print("Reshuffling deck")
    #         deck = create_deck(num_decks)
    #         # running_count = 0
    #         used_cards = {}


    # print("Game over! You're a brokie")

if __name__ == "__main__":
    main()