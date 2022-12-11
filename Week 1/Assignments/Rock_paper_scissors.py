import random

computer_score = 0
player_score = 0
i=0
while i <= 5:
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    user_action = input("Enter a choice (rock, paper, scissors): ")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            player_score +=1
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            player_score +=1
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            player_score +=1
        else:
            print("Rock smashes scissors! You lose.")
    i+= 1

print('The final score is' + str(player_score))

if user_action not in possible_actions:
    print('Invalid choice')