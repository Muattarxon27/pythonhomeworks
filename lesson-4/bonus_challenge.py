import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    print("\n🎮 Welcome to Rock, Paper, Scissors! First to 5 wins the match.")

    while player_score < 5 and computer_score < 5:
        computer_choice = random.choice(choices)  # Random computer choice
        player_choice = input("\nChoose rock, paper, or scissors: ").lower().strip()

        if player_choice not in choices:
            print("❌ Invalid choice! Please choose rock, paper, or scissors.")
            continue

        print(f"🖥 Computer chose: {computer_choice}")

        # Determine the winner
        if player_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!")
            player_score += 1
        else:
            print("😢 Computer wins this round!")
            computer_score += 1

        # Display current score
        print(f"📊 Score -> You: {player_score} | Computer: {computer_score}")

    # Declare final winner
    if player_score == 5:
        print("\n🏆 Congratulations! You won the match! 🎉")
    else:
        print("\n🤖 Computer wins the match! Better luck next time!")

# Start the game
play_game()