import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if win_conditions[user_choice] == computer_choice:
        return "You win!"
    else:
        return "You lose!"
