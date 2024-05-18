import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You Won!", 1
    else:
        return "Computer Won!", -1

# Function to display choices and result
def display_result(user_choice, computer_choice, result):
    print("Your Choice:", user_choice)
    print("Computer's Choice:", computer_choice)
    print(result)

# Function to play the game
def play_game():
    global user_score, computer_score, game_count

    # User's choice input
    user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

    # Check if user wants to quit
    if user_choice == "q":
        return False

    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please enter rock, paper, scissors, or 'q' to quit.")
        return True

    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    result, score = determine_winner(user_choice, computer_choice)

    # Update scores
    user_score += score
    computer_score -= score

    # Display result
    display_result(user_choice, computer_choice, result)

    # Increment game count
    game_count += 1

    return True

# Initialize scores and game count
user_score = 0
computer_score = 0
game_count = 0

# Game loop
while True:
    continue_game = play_game()

    if not continue_game:
        break

# Display final scores
print()
print("Your Score:", user_score)
print("Computer's Score:", abs(computer_score))
print("Number of Games Played:", game_count)
