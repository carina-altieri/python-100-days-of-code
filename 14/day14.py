# Higher or Lower 

import art
import game_data
import random

should_continue = True
score = 0

def  higher_or_lower():
    global should_continue, score

    while should_continue:
        print (art.logo)
        random_celeb_A = random.choice(game_data.data)
        random_celeb_B = random.choice(game_data.data)
        while random_celeb_A == random_celeb_B:  # enquanto B == A, continue escolhendo um valor para B
            random_celeb_B = random.choice(game_data.data)

        print(f"Compare A: {random_celeb_A['name']}, a {random_celeb_A['description']}, from {random_celeb_A['country']}.")
        print(art.vs)
        print(f"Against B: {random_celeb_B['name']}, a {random_celeb_B['description']}, from {random_celeb_B['country']}.")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if (answer == 'a' and random_celeb_A['follower_count'] > random_celeb_B["follower_count"]) or \
           (answer == 'b' and random_celeb_B['follower_count'] > random_celeb_A['follower_count']):
            score += 1
            random_celeb_B = random_celeb_A # a próxima rodada começa com o vencedor da rodada anterior
            while random_celeb_A == random_celeb_B: # garantindo que A seja diferente de B:
                random_celeb_B = random.choice(game_data.data)
                
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            should_continue = False

higher_or_lower()