import random

try:
    replay_amount = int(input("How many times do you want to face the bot: "))
except:
    print("Please Enter a Numeric Input")
    quit()

player_score = 0
computer_score = 0

possible_playerchoice = ["rock", "scissor", "paper"]

for tries in range(replay_amount):

    print("                                                     ")
    user_choice = input("First Player: rock, paper, Or scissor: ")

    if user_choice not in possible_playerchoice:
        print("Please enter rock paper or scissor with no uppercase's")
        quit()

    possible_actions = ["rock", "paper", "scissors"]

    big_brainpc = random.choice(possible_actions)

    print("         ")
    print("You chose " + user_choice + " and " + "the computer chose " + big_brainpc)
    print("         ")

    if user_choice == big_brainpc:
        print("It's a draw XD")
    elif user_choice == "rock":
        if big_brainpc == "paper":
            print("Bro you lost to a bot, get good XD")
            computer_score = computer_score + 1
        else:
            print("You won against a robot loser.")
            player_score = player_score + 1

    if user_choice == "paper":
        if big_brainpc == "rock":
            print("You won against a robot loser.")
            player_score = player_score + 1
        else:
            print("Bro you lost to a bot, get good XD")
            computer_score = computer_score + 1

    if user_choice == "scissor":
        if big_brainpc == "rock":
            print("Bro you lost to a bot, get good XD")
            computer_score = computer_score + 1
        else:
            print("You won against a robot loser.")
            player_score = player_score + 1


    print("----------------------------------------")
    print("Computer Score: " + str(computer_score))
    print("Player Score: " + str(player_score))
    print("----------------------------------------")

print("              ")
input("Press a key close")








