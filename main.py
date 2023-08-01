import art
import random
import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal(player):
    card = random.choice(cards)
    if player == player_name:
        if card == 11:
            ace_choice = int(input('You drew an Ace! Would you like a 1, or 11?\n'))
            player_cards.append(ace_choice)
        else:
            player_cards.append(card)
    elif player == 'dealer':
        if card == 11:
            if len(dealer_cards) >= 1 and dealer_cards[0] == 11 or dealer_score >= 11:
                card = 1
                dealer_cards.append(card)
            else:
                card = 11
                dealer_cards.append(card)
        else:
            dealer_cards.append(card)
        print(dealer_cards)

def calculate_score(player):
    if player == player_name:
        score = sum(player_cards)
    elif player == 'dealer':
       score = sum(dealer_cards)
    return score


def compare(player_score, dealer_score, player_card_count, dealer_card_count):
  if player_score == 0:
    return player_name
  elif dealer_score == 0:
    return 'Dealer'
  elif player_score > dealer_score and player_score <= 21:
    return player_name
  elif dealer_score > player_score and dealer_score <= 21:
    return 'Dealer'
  elif dealer_score > 21 and player_score <= 21:
    return player_name
  elif dealer_score <= 21 and player_score > 21:
    return 'Dealer'
  elif player_score == dealer_score and player_score <= 21:
    if player_card_count < dealer_card_count:
      return player_name
    else:
      return 'Dealer'
  
def game():
    deal(player_name)
    deal('dealer')
    deal(player_name)
    deal('dealer')
    player_score = calculate_score(player_name)
    dealer_score = calculate_score('dealer')
    dealer_card_count = 2
    player_card_count = 2
    print(f'{player_name}  Hand: {player_cards}  Score: {player_score}\n')
    print(f'Dealer  Face-Up Card: {dealer_cards[1]} \n')
    if player_score == 21:
            player_score = 0
            winner = compare(player_score, dealer_score, player_card_count, dealer_card_count)
    elif dealer_score == 21:
            dealer_score = 0
            winner = compare(player_score, dealer_score, player_card_count, dealer_card_count)
    else:
            hit_choice = input("Would you like to hit, or stay?\n")
            while hit_choice != 'stay' and player_score < 21:
                deal(player_name)
                player_card_count += 1
                player_score = calculate_score(player_name)
                print(f'{player_name}  Hand: {player_cards}  Score: {player_score}')
                if player_score > 21:
                    print('You busted!')
                    break
                hit_choice = input("Would you like to hit, or stay?\n")
            while dealer_score <= 16 and player_score <= 21:
                deal('dealer')
                dealer_card_count += 1
                dealer_score = calculate_score('dealer')
                print(f'Dealer  Face Up Cards:{dealer_cards[1:]}')
                if dealer_score > 21:
                    print('Dealer busted!')
                    break
    print(f'Player Final Hand: {player_cards}  Score: {player_score}')
    print(f'Dealer Final Hand: {dealer_cards}  Score: {dealer_score}')
    winner = compare(player_score, dealer_score, player_card_count, dealer_card_count)
    return winner
  
print(art.logo)
print('NOTE: If your score shows 0, this indicates a BlackJack!')
player_name = input('Hello! Welcome to BlackJack. What is your name?\n')
play_again = 'y'
while play_again != 'n':
  player_score = 0
  dealer_score = 0
  player_cards = []
  dealer_cards = []
  player_card_count = 0
  dealer_card_count = 0
  clear()
  print(art.logo)
  winner = game()
  print(f'The winner is {winner}!')
  play_again = input('Would you like to play again? y/n\n')
  
    


  




