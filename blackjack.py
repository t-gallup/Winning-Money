print('Money Moves')
print('YO')
print('Gene is gey')
import random

def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

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

def play_game():
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    is_game_over = False
    player_bet = 10  # Starting bet, you can change this to any amount

    print(f"Your current bet: ${player_bet}")

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, 'n' to pass, 'd' to double down: ").lower()

            if user_choice == 'y':
                user_cards.append(deal_card())
            elif user_choice == 'd':
                player_bet *= 2
                user_cards.append(deal_card())
                is_game_over = True
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))
    print(f"Your final bet: ${player_bet}")

# Run the game
play_game()

