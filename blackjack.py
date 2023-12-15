import random

def create_deck(num_decks):
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * num_decks
    random.shuffle(cards)
    return cards

def deal_card(deck):
    return deck.pop()

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "Dealer has Blackjack. You lose!"
    elif user_score == 0:
        return "You have Blackjack! You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def get_bet(player_money):
    while True:
        try:
            bet = int(input(f"Your current balance: ${player_money}\nEnter your bet amount: $"))
            if 0 < bet <= player_money:
                return bet
            else:
                print("Please enter a valid bet amount within your balance.")
        except ValueError:
            print("Please enter a valid bet amount.")

def play_game(num_decks):
    deck = create_deck(num_decks)
    player_money = 1000  # Starting money
    is_game_over = False

    while player_money > 0 and not is_game_over:
        player_bet = get_bet(player_money)

        user_cards = [deal_card(deck), deal_card(deck)]
        dealer_cards = [deal_card(deck), deal_card(deck)]

        print(f"Your current balance: ${player_money}")
        print(f"Your current bet: ${player_bet}")

        while True:
            user_score = calculate_score(user_cards)
            dealer_score = calculate_score(dealer_cards)

            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Dealer's first card: {dealer_cards[0]}")

            if user_score == 0 or dealer_score == 0 or user_score > 21:
                break
            else:
                user_choice = input("Type 'y' to get another card, 'n' to pass, 'd' to double down: ").lower()

                if user_choice == 'y':
                    user_cards.append(deal_card(deck))
                elif user_choice == 'd':
                    player_bet *= 2
                    user_cards.append(deal_card(deck))
                    break
                else:
                    break

        while dealer_score != 0 and dealer_score < 17:
            dealer_cards.append(deal_card(deck))
            dealer_score = calculate_score(dealer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
        result = compare(user_score, dealer_score)
        print(result)

        if result == "You win!":
            player_money += player_bet
        elif result == "You lose!":
            player_money -= player_bet

        print(f"Your current balance: ${player_money}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            is_game_over = True

# Run the game with 4 decks
play_game(num_decks=4)
