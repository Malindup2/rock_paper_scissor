import random

options = ("rock", "paper", "scissor")
score = 0

while True:
    machine = random.choice(options)
    player = None  # Reset player input for the round

    while player not in options:  # Validate user input
        player = input("Your turn :) Enter your choice (rock, paper, scissor):\n").lower()
        if player not in options:
            print("Invalid choice! Please select from rock, paper, or scissor.")

    print("You: ", player)
    print("Computer: ", machine)

    # Game logic
    if machine == player:
        print("Game Tie -XD")
    elif (machine == "rock" and player == "paper") or \
         (machine == "paper" and player == "scissor") or \
         (machine == "scissor" and player == "rock"):
        print("You win!")
        score += 1
    else:
        print("You lose-:(")



    ans = input("Do you like to continue the game? (Y/N): ").lower()
    if ans != 'y':
        print(f"Your current score: {score}")
        print("Thank you for playing! Your final score is:", score)
        break
