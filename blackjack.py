from art import logo
import random
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def draw_card(hand):
    draw = random.randint(0, len(cards)-1)
    hand.append(cards[draw])


def get_hand_sum(hand):
    hand_sum = 0
    ace = False
    for card in hand:
        if card == 11 and ace == False:
            hand_sum += card
            ace = True
        elif card == 11 and ace == True:
            hand_sum += 1
        else:
            hand_sum += card
    # make sure we add up total without counting 11's if over 21
    alt_sum = 0
    if hand_sum > 21:
        for card in hand:
            if card == 11:
                alt_sum += 1
            else:
                alt_sum += card
    if hand_sum <= 21:
        return hand_sum
    elif alt_sum <= 21:
        return alt_sum
    else:
        return alt_sum

def draw_dealer(dealer_hand):
    while get_hand_sum(dealer_hand) < 17:
        draw_card(dealer_hand)

def display_winner(player_hand, dealer_hand):
    player_score = get_hand_sum(player_hand)
    dealer_score = get_hand_sum(dealer_hand)
    if player_score > 21:
        print(f"You BUSTED! You lose! Hand: {player_hand} = {player_score}")
        return
    if dealer_score > 21:
        print(f"Dealer bust! You WIN! Hand: {dealer_hand} = {dealer_score}")
        return

    if player_score < dealer_score and dealer_score == 21:
        print(f"YOU LOSE! Dealer Blackjack! Dealer hand: {dealer_hand} = {dealer_score} vs Your hand: {player_hand} = {player_score}")
    elif player_score > dealer_score and player_score == 21:
        print(f"YOU WIN! Player Blackjack! Dealer hand: {dealer_hand} = {dealer_score} vs Your hand: {player_hand} = {player_score}")
    elif player_score < dealer_score:
        print(f"YOU LOSE! Dealer hand: {dealer_hand} = {dealer_score} vs Your hand: {player_hand} = {player_score}")
    elif player_score > dealer_score:
        print(f"YOU WIN! Dealer hand: {dealer_hand} = {dealer_score} vs Your hand: {player_hand} = {player_score}")
    else:
        print(f"Its a DRAW! Nobody wins!  Dealer hand: {dealer_hand} = {dealer_score} vs Your hand: {player_hand} = {player_score}")



game_active = input("Would you like to play a game of blackjack yes('y') or no('n')?")
while game_active == 'y':
    player = []
    dealer = []
    # start game draw 2 cards for player and 1 card for dealer
    draw_card(player)
    draw_card(player)
    draw_card(dealer)

    if get_hand_sum(player) == 21:
        print(f"Player wins on a blackjack! Hand: {player}")
    else:
        print(f"Your hand: {player}")
        print(f"Dealers first card: {dealer[0]}")
        draw_again = input("Would you like to hit('h') or stand('s')?")
        while draw_again == 'h' and get_hand_sum(player) < 21:
            # player hits draw another card
            draw_card(player)
            if get_hand_sum(player) < 21:
                print(f"Your hand: {player} = {get_hand_sum(player)}")
                print(f"Dealers first card: {dealer[0]}")
                draw_again = input("Would you like to hit('h') or stand('s')?")

            else:
                draw_again = "s"
        # check for blackjack or bust
        draw_dealer(dealer)
        display_winner(player, dealer)



    game_active = input("Would you like to play a game of blackjack yes('y') or no('no')?")