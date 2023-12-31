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
def best_strategy(player_hand, dealer_hand, current_bet, bet_amount, total_money):
    if current_bet + bet_amount > total_money or len(player_hand) > 2:
        double_down_hit = 'hit'
        split_hit = 'hit'
        double_down_stay = 'stay'
    else:
        double_down_hit = 'double down'
        split_hit = 'split'
        double_down_stay = 'double_down'
    
    if get_card_value(player_hand[0]) == get_card_value(player_hand[1]):
        dealer_value = get_card_value(dealer_hand[0])
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
        elif dealer_value == 10:
            return 'surrender'
        else:
            return 'hit'
    elif player_value == 16:
        if dealer_value <= 6:
            return 'stay'
        elif dealer_value <= 8:
            return 'hit'
        else:
            return 'surrender'
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

def get_running_count(used_cards):
    running_count = 0
    for card in used_cards:
        value = get_card_value(card)
        if value >= 2 and value <= 6:
            running_count += used_cards[card]
        if value == 10 or value == 11:
            running_count -= used_cards[card]
    return running_count

# Function to play a hand of blackjack
def play_blackjack(deck, used_cards, bet_amount, total_money):
    print("Current Count: ", get_running_count(used_cards))
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

    print("\nYour cards:", ' '.join(map(str, player_hand)))
    print("Dealer's face up card:", dealer_hand[0])

    if check_blackjack(player_hand):
        if check_blackjack(dealer_hand):
            print("Player and dealer both have blackjack. It's a tie.")
            # running_count = change_running_count(dealer_hand[1], running_count)
            update_used_cards([dealer_hand[1]], used_cards)
            print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))
            print(f"\nRunning Count: {get_running_count(used_cards)}")
            
            return 0
        else:
            print("Player has blackjack! You win 3:2")
            # Dealer card is only shown if they have a 10, face card, or ace
            if get_card_value(dealer_hand[0]) >= 10:
                # running_count = change_running_count(dealer_hand[1], running_count)
                print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))
                update_used_cards([dealer_hand[1]], used_cards)
            print(f"\nRunning Count: {get_running_count(used_cards)}")
            return int(bet_amount * 1.5)

    # Check for if dealer has blackjack in the initial hand
    if check_blackjack(dealer_hand):
        if check_blackjack(player_hand):
            print("Player and dealer both have blackjack. It's a tie.")
            # running_count = change_running_count(dealer_hand[1], running_count)
            update_used_cards([dealer_hand[1]], used_cards)
            print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))
            print(f"\nRunning Count: {get_running_count(used_cards)}")
            return 0
        else:
            print("Dealer has Blackjack! You lose!")
            # running_count = change_running_count(dealer_hand[1], running_count)
            update_used_cards([dealer_hand[1]], used_cards)
            print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))
            print(f"\nRunning Count: {get_running_count(used_cards)}")
            return -bet_amount

    current_bet = bet_amount
    
    surrender = input('Would you like to surrender? (yes/no): ')
    if surrender == 'yes':
        # Dealer's cards don't get shown if you surrender
        # print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))
        # running_count = change_running_count(dealer_hand[1], running_count)
        # print(f"\nRunning Count: {running_count}")
        return -bet_amount//2
    # Check for pair to enable splitting
    if get_card_value(player_hand[0]) == get_card_value(player_hand[1]):
        if current_bet + bet_amount > total_money:
            print("You can't split because you're broke")
            split = 'no'
        else:
            split = input("Would you like to split? (yes/no): ").lower()
        if split == 'yes':
            current_bet += bet_amount
            split_hands = [[player_hand[0]], [player_hand[1]]]
            for i in range(len(split_hands)):
                card = deck.pop()
                # running_count = change_running_count(card, running_count)
                split_hands[i].append(card)
                update_used_cards([split_hands[i]], used_cards)
            hand_count = -1
            split_count = 1
            while hand_count < len(split_hands) - 1:
                hand_count += 1
                print(f"\nHand {hand_count + 1}: {' '.join(map(str, split_hands[hand_count]))}")
                if len(split_hands[hand_count]) == 2 and split_hands[hand_count][0] == split_hands[hand_count][1]:
                    if split_count == 3:
                        print("You can't split because you've gone past the max number of splits")
                        split = 'no'
                    elif current_bet + bet_amount > total_money:
                        print("You can't split because you're broke")
                        split = 'no'
                    else:
                        split = input("Would you like to split? (yes/no): ").lower()
                    if split == 'yes':
                        current_bet += bet_amount
                        split_hands.append([split_hands[hand_count][1]])
                        split_hands[hand_count] = [split_hands[hand_count][0]]
                        split_hands[hand_count].append(deck.pop())
                        split_hands[len(split_hands)-1].append(deck.pop())
                        split_count += 1
                
                # print(f"\nHand {hand_count + 1}: {' '.join(map(str, split_hands[hand_count]))}")
                if current_bet + bet_amount > total_money:
                    print("You can't double down because you're broke")
                    double_down = 'no'
                else:
                    double_down = input("Would you like to double down? (yes/no): ").lower()
                if double_down == 'yes':
                    bet_amount *= 2
                    card = deck.pop()
                    # running_count = change_running_count(card, running_count)
                    split_hands[hand_count].append(card)
                    update_used_cards([card], used_cards)
                    print("Your cards:", ' '.join(map(str, split_hands[hand_count])))
                    # adjust_for_aces(split_hands[hand_count])

                    # if sum(split_hands[i]) > 21:
                    #     print("You busted")
                    #     return -bet_amount
                else:
                    while get_true_sum(split_hands[hand_count]) < 21:
                    #     print(f"\nHand {hand_count + 1}: {' '.join(map(str, split_hands[hand_count]))}")
                        action = input("Would you like to hit or stay: ").lower()
                        if action == 'hit':
                            card = deck.pop()
                            # running_count = change_running_count(card, running_count)
                            split_hands[hand_count].append(card)
                            print(f"Hand {hand_count + 1}: {' '.join(map(str, split_hands[hand_count]))}")
                            update_used_cards([card], used_cards)
                            # adjust_for_aces(split_hands[hand_count])
                            if get_true_sum(split_hands[hand_count]) > 21:
                                print(f"Hand {hand_count + 1} busted")
                                break
                        elif action == 'stay':
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

            print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))

            # Determine the winner for each split hand
            total_winnings = 0
            for i in range(len(split_hands)):
                player_value = get_true_sum(split_hands[i])
                dealer_value = get_true_sum(dealer_hand)

                if player_value > 21:
                    print(f"Hand {i + 1} busts. Dealer wins")
                    total_winnings -= bet_amount
                elif dealer_value > 21 or player_value > dealer_value:
                    print(f"Hand {i + 1} wins")
                    total_winnings += bet_amount
                elif player_value < dealer_value:
                    print(f"Hand {i + 1} loses")
                    total_winnings -= bet_amount
                else:
                    print(f"Hand {i + 1} ties with the dealer")

            return total_winnings

    # Player's turn for non-split hand
    if current_bet + bet_amount > total_money:
        print("You can't double down because you're broke")
        double_down = 'no'
    else:
        double_down = input("Would you like to double down? (yes/no): ").lower()
    if double_down == 'yes':
        current_bet += bet_amount
        bet_amount *= 2
        card = deck.pop()
        # running_count = change_running_count(card, running_count)
        player_hand.append(card)
        update_used_cards([card], used_cards)
        print("Your cards:", ' '.join(map(str, player_hand)))
        # adjust_for_aces(player_hand)

        if get_true_sum(player_hand) > 21:
            # You don't see dealers hand if you bust
            print("You busted")
            # running_count = change_running_count(dealer_hand[1], running_count)
            print(f"\nRunning Count: {get_running_count(used_cards)}")
            return -bet_amount
    else:
        while get_true_sum(player_hand) < 21:
            action = input("Would you like to hit or stay: ").lower()
            if action == 'hit':
                card = deck.pop()
                # running_count = change_running_count(card, running_count)
                player_hand.append(card)
                update_used_cards([card], used_cards)
                print("Your cards:", ' '.join(map(str, player_hand)))
                # adjust_for_aces(player_hand)
                if get_true_sum(player_hand) > 21:
                    # You don't see dealers hand if you bust
                    print("You busted")
                    # running_count = change_running_count(dealer_hand[1], running_count)
                    print(f"\nRunning Count: {get_running_count(used_cards)}")
                    return -bet_amount
            elif action == 'stay':
                break

    # Dealer's turn
    #Add dealers second card to running count, done here because it isn't shown until now
    # running_count = change_running_count(dealer_hand[1], running_count)
    update_used_cards([dealer_hand[1]], used_cards)
    while ('A' in dealer_hand and get_true_sum == 17) or get_true_sum(dealer_hand) < 17:
        card = deck.pop()
        # running_count = change_running_count(card, running_count)
        dealer_hand.append(card)
        update_used_cards([card], used_cards)
        # adjust_for_aces(dealer_hand)

    print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))

    # Determine the winner for the non-split hand
    player_value = get_true_sum(player_hand)
    dealer_value = get_true_sum(dealer_hand)

    if player_value > 21:
        print("Player busts. Dealer wins")
        print(f"\nRunning Count: {get_running_count(used_cards)}")
        return -bet_amount
    elif dealer_value > 21 or player_value > dealer_value:
        print("Player wins")
        print(f"\nRunning Count: {get_running_count(used_cards)}")
        return bet_amount
    elif player_value < dealer_value:
        print("Dealer wins")
        print(f"\nRunning Count: {get_running_count(used_cards)}")
        return -bet_amount
    else:
        print("It's a tie")
        print(f"\nRunning Count: {get_running_count(used_cards)}")
        return 0


# Main game loop
def main():
    num_decks = int(input("Please enter the number of decks: "))
    total_money = int(input("Please enter the amount of money you would like to start with: "))
    min_bet = 10

    deck = create_deck(num_decks)
    used_cards = {}

    round_number = 1
    penetration = .5
    reshuffle_amount = penetration * len(deck)

    # running_count = 0

    while total_money >= min_bet:
        bet_amount = int(input("Please enter the amount of money to bet on this hand (>=" + str(min_bet) + "): "))
        if bet_amount < min_bet or bet_amount > total_money:
            continue
        print(f"\nHand: {round_number}")
        result = play_blackjack(deck, used_cards, bet_amount, total_money)
        total_money += result
        print(f"\nYour total money: {total_money}")
        print(f"\nUsed cards: {used_cards}")
        round_number += 1
        if len(deck) < reshuffle_amount:
            print("Reshuffling deck")
            deck = create_deck(num_decks)
            # running_count = 0
            used_cards = {}


    print("Game over! You're a brokie")

if __name__ == "__main__":
    main()