import art
import random
import os

def main():
    print(art.logo)
    players = []
    add_another = 'y'
    while add_another != 'n':
        player = add_player(players)
        players.append(player)
        while True:
            try:
                add_another = input('Add another? y/n ').lower().strip()
                if add_another not in ['y', 'n']:
                    raise ValueError
            except ValueError:
                print("Error: answer must be 'y' or 'n'")
            else:
                break
    players_left = len(players)
    play_again = 'y'
    while play_again != 'n':
        cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
           7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", 
           "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
        winners = []
        random.shuffle(cards)
        for player in players:
            player["Score"] = 0
            player["Hand"] = []
        dealer = {"Name": "Dealer", "Hand": [], "Score": 0}
        clear()
        print(art.logo)
        for _ in range(2):
            for player in players:
                player = deal(player, players, cards[0])
                cards.pop(0)
            dealer = deal(dealer, players, cards[0])
            cards.pop(0)
        print(f"Dealer Face Up Card: {dealer["Hand"][1]}")
        for player in players:
                print(player)
        for player in players:
            if player["Score"] == 21:
                winners.append(player["Name"])
                print(f"{player["Name"]} got a Blackjack!")
        if dealer["Score"] != 21:
            for player in players:
                if player["Score"] < 21:
                    hit_choice = input(f"{player["Name"]}, would you like to hit, or stay? ").lower().strip()
                    while hit_choice.lower() != "stay" and player["Score"] < 21:
                        player = deal(player, players, cards[0])
                        cards.pop(0)
                        print(player)
                        if player["Score"] > 21:
                            print("You busted! ")
                            players_left -= 1
                            break
                        elif player["Score"] < 21:
                            hit_choice = input("Would you like another hit, or to stay? ").lower().strip()
            while dealer["Score"] <= 15 and players_left > 0:
                dealer = deal(dealer, players, cards[0])
                cards.pop(0)
                print(f'Dealer Face Up Cards: {dealer["Hand"][1:]}')
                if dealer["Score"] > 21:
                    print('Dealer busted!')
                    for player in players:
                        if player["Score"] <= 21 and player["Name"] not in winners:
                            winners.append(player["Name"])
                    break
        else:
            winners = []
            players_left = 0
            print("Dealer got a BlackJack!")
        for player in players:
            print(player)
            if player["Score"] > dealer["Score"] and player["Score"] <= 21 and player["Name"] not in winners:
                winners.append(player["Name"])
        print(dealer)
        if len(winners) == 0:
            print("No Players Beat the Dealer. Game Over!")
        else:
            if len(winners) > 1:
                for winner in winners[:-1]:
                    print(winner, end = " ")
                print(f"and {winners[-1]}", end = "")
            else:
                print(winners[0], end = "")
            print(" beat the Dealer! Congratulations!")
        while True:
            try:
                play_again = input("Play Again? Y/n ").lower().strip()
                if play_again not in ['y', 'n']:
                    raise ValueError
            except ValueError:
                print("Error: must answer 'y' or 'n'")
            else:
                break     


# Simple function to clear terminal window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def add_player(players):
    while True:
        try:
            name = input("What is your name? ").strip()
            for player in players:
                if player["Name"] == name:
                    raise ValueError
        except ValueError:
            print("Error: Name Taken")
        else:
            break 
    hand = []
    score = 0
    player = {"Name": name, "Hand": hand, "Score": score}
    
    return player
    

def deal(player, players, card):
    if card == "A":
        if player in players:
            while True:
                try:
                    ace_choice = int(input(f"{player["Name"]}, you drew an Ace! Would you like a 1, or 11? "))
                    if ace_choice not in [1, 11]:
                        raise ValueError
                except ValueError:
                    print("Error: Choice must be 1 or 11")
                else:
                    break
            player["Hand"].append(ace_choice)
            player["Score"] += ace_choice
        elif player["Name"] == "Dealer":
            player['Hand'].append(card)
            if player["Score"] >= 11:
                player["Score"] += 1
            else:
                player["Score"] += 11
    elif card in ['J', 'Q', 'K']:
        player["Hand"].append(card)
        player["Score"] += 10
    else:
        player["Hand"].append(card)
        player["Score"] += card
        
    return player
        
    

if __name__ == "__main__":
    main()

