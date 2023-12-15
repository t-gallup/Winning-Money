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
    # ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    ranks = [5]
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
    

# Function to play a hand of blackjack
def play_blackjack(deck, used_cards, bet_amount, total_money):
    player_hand = []
    dealer_hand = []

    # Deal initial cards
    player_hand.append(get_card_rank(deck.pop()))
    dealer_hand.append(get_card_rank(deck.pop()))
    player_hand.append(get_card_rank(deck.pop()))
    dealer_hand.append(get_card_rank(deck.pop()))

    print("\nYour cards:", ' '.join(map(str, player_hand)))
    print("Dealer's face up card:", dealer_hand[0])

    # Check for blackjack in the initial hand
    if check_blackjack(player_hand):
        if check_blackjack(dealer_hand):
            print("Player and dealer both have blackjack. It's a tie.")
            return 0
        else:
            print("Player has blackjack! You win 3:2")
            return int(bet_amount * 1.5)

    # Check for pair to enable splitting
    if player_hand[0] == player_hand[1]:
        split = input("Would you like to split? (yes/no): ").lower()
        if split == 'yes':
            split_hands = [[player_hand[0]], [player_hand[1]]]
            for i in range(len(split_hands)):
                split_hands[i].append(get_card_value(deck.pop()))
            hand_count = -1
            while hand_count < len(split_hands) - 1:
                hand_count += 1
                print(f"\nHand {hand_count + 1}: {' '.join(map(str, split_hands[hand_count]))}")
                if len(split_hands[hand_count]) == 2 and split_hands[hand_count][0] == split_hands[hand_count][1]:
                    split = input("Would you like to split? (yes/no): ").lower()
                    if split == 'yes':
                        split_hands.append([split_hands[hand_count][1]])
                        split_hands[hand_count] = [split_hands[hand_count][0]]
                        split_hands[hand_count].append(get_card_value(deck.pop()))
                        split_hands[len(split_hands)-1].append(get_card_value(deck.pop()))
                
                double_down = input("Would you like to double down? (yes/no): ").lower()
                if double_down == 'yes':
                    bet_amount *= 2
                    card = get_card_value(deck.pop())
                    split_hands[hand_count].append(card)
                    used_cards.append(card)
                    print("Your cards:", ' '.join(map(str, split_hands[hand_count])))
                    adjust_for_aces(split_hands[hand_count])

                    # if sum(split_hands[i]) > 21:
                    #     print("You busted")
                    #     return -bet_amount
                else:
                    while get_true_sum(split_hands[hand_count]) < 21:
                        action = input("Would you like to hit or stay: ").lower()
                        if action == 'hit':
                            card = get_card_value(deck.pop())
                            split_hands[hand_count].append(card)
                            print(f"Hand {hand_count + 1}: {' '.join(map(str, split_hands[hand_count]))}")
                            used_cards.append(card)
                            adjust_for_aces(split_hands[hand_count])
                            if get_true_sum(split_hands[hand_count]) > 21:
                                print(f"Hand {hand_count + 1} busted")
                                break
                        elif action == 'stay':
                            break

            # Dealer's turn
            while get_true_sum(dealer_hand) < 18:
                card = deck.pop()
                dealer_hand.append(card)
                used_cards.append(card)
                adjust_for_aces(dealer_hand)

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
    else:
        double_down = input("Would you like to double down? (yes/no): ").lower()
        if double_down == 'yes':
            bet_amount *= 2
            card = get_card_value(deck.pop())
            player_hand.append(card)
            used_cards.append(card)
            print("Your cards:", ' '.join(map(str, player_hand)))
            adjust_for_aces(player_hand)

            if get_true_sum(player_hand) > 21:
                print("You busted")
                return -bet_amount
        else:
            while get_true_sum(player_hand) <= 21:
                action = input("Would you like to hit or stay: ").lower()
                if action == 'hit':
                    card = get_card_value(deck.pop())
                    player_hand.append(card)
                    used_cards.append(card)
                    print("Your cards:", ' '.join(map(str, player_hand)))
                    adjust_for_aces(player_hand)
                    if get_true_sum(player_hand) > 21:
                        print("You busted")
                        return -bet_amount
                elif action == 'stay':
                    break

        # Dealer's turn
        while get_true_sum(dealer_hand) < 18:
            card = get_card_value(deck.pop())
            dealer_hand.append(card)
            used_cards.append(card)
            adjust_for_aces(dealer_hand)

        print("\nDealer's cards:", ' '.join(map(str, dealer_hand)))

        # Determine the winner for the non-split hand
        player_value = get_true_sum(player_hand)
        dealer_value = get_true_sum(dealer_hand)

        if player_value > 21:
            print("Player busts. Dealer wins")
            return -bet_amount
        elif dealer_value > 21 or player_value > dealer_value:
            print("Player wins")
            return bet_amount
        elif player_value < dealer_value:
            print("Dealer wins")
            return -bet_amount
        else:
            print("It's a tie")
            return 0

# Main game loop
def main():
    num_decks = int(input("Please enter the number of decks: "))
    total_money = int(input("Please enter the amount of money you would like to start with: "))
    bet_amount = int(input("Please enter the amount of money to bet on each hand: "))

    deck = create_deck(num_decks)
    used_cards = []

    round_number = 1

    while total_money >= bet_amount:
        print(f"\nHand: {round_number}")
        result = play_blackjack(deck, used_cards, bet_amount, total_money)
        total_money += result
        print(f"\nYour total money: {total_money}")
        round_number += 1

    print("You're out of money. Game over!")

if __name__ == "__main__":
    main()
