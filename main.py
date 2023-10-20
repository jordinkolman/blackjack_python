import art
import random
import os

def main():
    #TODO
    print(art.logo)
    print('Note: If your score shows 0 after deal, this indicates a BlackJack!')
    players = []
    print("Please add a player, or leave blank to begin (Requires at least 1 player)")
    add_another = 'y'
    while add_another != 'n':
        player = add_player()
        players.append(player)
        add_another = input('Add another? y/n ').lower().strip()
    play_again = 'y'
    while play_again != 'n':
        cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
           7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "J", "J", "J", 
           "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
        winners = []
        random.shuffle(cards)
        for player in players:
            player["Score"] = 0
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
                print("Blackjack!")
        else:
            for player in players:
                hit_choice = input(f"{player["Name"]}, would you like to hit, or stay? ").lower().strip()
                while hit_choice.lower() != "stay" and player["Score"] < 21:
                    player = deal(player, players, cards[0])
                    cards.pop(0)
                    print(player)
                    if player["Score"] > 21:
                        print("You busted! ")
                        break
                    hit_choice = input("Would you like another hit, or to stay? ").lower().strip()
            while dealer["Score"] < 16:
                dealer = deal(dealer, players, cards[0])
                cards.pop(0)
                print(f'Dealer Face Up Cards: {dealer["Hand"][1:]}')
                if dealer["Score"] > 21:
                    print('Dealer busted!')
                    break
        for player in players:
            print(player)
            if player["Score"] > dealer["Score"] and player["Score"] <= 21 and player["Name"] not in winners:
                winners.append(player["Name"])
        print(dealer)
        if len(winners) == 0:
            print("No Players Beat the Dealer. Game Over!")
        else:
            print("The Following Players Beat the Dealer! Congratulations!")
            for winner in winners:
                print(winner, end=" ")
                print()
        play_again = input("Play Again? Y/n ").lower().strip()
        
               
        
    
        


# Simple function to clear terminal window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def add_player():
    name = input("What is your name? ").strip()
    hand = []
    score = 0
    player = {"Name": name, "Hand": hand, "Score": score}
    
    return player
    

def deal(player, players, card):
    if card == "A":
        if player in players:
            ace_choice = int(input(f"{player["Name"]}, you drew an Ace! Would you like a 1, or 11? "))
            player["Hand"].append(ace_choice)
            player["Score"] += ace_choice
        elif player["Name"] == "Dealer":
            player['Hand'].append(card)
            if player["Score"] >= 11:
                score += 1
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

