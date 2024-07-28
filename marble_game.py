import random

def draw_marble(bag):
    return random.choice(bag)

def play_game(starting_gold, rounds, bag):
    gold = starting_gold
    for round in range(1, rounds + 1):
        print(f"Round {round}")
        print(f"Current gold: {gold} pieces")

        bet = int(input("Enter your bet amount: "))
        if bet > gold:
            print("You cannot bet more than you have!")
            continue

        marble = draw_marble(bag)
        print(f"You drew a {marble} marble.")

        if marble == 'green':
            gold += bet
            print(f"You won {bet} gold pieces!")
        elif marble == 'red':
            gold -= bet
            print(f"You lost {bet} gold pieces!")
        elif marble == 'black':
            gold += bet * 10
            print(f"You won {bet * 10} gold pieces!")
        elif marble == 'white':
            gold -= bet * 5
            print(f"You lost {bet * 5} gold pieces!")

        print(f"Gold after round {round}: {gold} pieces\n")

        if gold <= starting_gold / 2:
            print("You have lost half of your starting gold. Game over!")
            break

    print("Thanks for playing!")
    print(f"Total gold at the end: {gold} pieces")

def main():
    starting_gold = 1000
    rounds = int(input("Enter the number of rounds you want to play: "))

    # Bag with 10 marbles: 5 green, 3 red, 1 black, 1 white
    bag = ['green'] * 5 + ['black'] + ['red'] * 3 + ['white']

    play_game(starting_gold, rounds, bag)

if __name__ == "__main__":
    main()
