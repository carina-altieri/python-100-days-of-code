# Blackjack Project

import art
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the carts"""
    if sum(cards) == 21 and len == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if c_score == u_score:
        return "It's a draw!"
    elif c_score == 0:
        return "Computer has a blackjack. You lose!"
    elif u_score == 0:
        return "You have a blackjack! win!"
    elif u_score > 21:
        return "You went over. You lose!"
    elif c_score > 21:
        return "The computer score went over. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def play():
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your deck: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_another_card = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
            if draw_another_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17 : # blackjack = 0
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards) # updating computer score

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play()















