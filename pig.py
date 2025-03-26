import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()
print(value)

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1<= players <= 4:
            break
        else:
            print("Must be 1 - 4")
    else:
        print("Invalid, Try again!")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:

    for players_idx in range(players):
        print("\nPlayer", players_idx + 1, "turn has just started!\n")
        current_score = 0

    while True:
        should_roll = input("Would you like to roll (y)? ")
        if should_roll.lower() != 'y':
            break

    value = roll()
    if value == 1:
        current_score = 0
        print("You rolled a 1! Turn done!", )
    else:
        current_score += value
        print("You rolled a:", value)
    print("You score is:", current_score)
    player_score[players_idx] += current_score
    print("Your total score is:", player_score[players_idx])