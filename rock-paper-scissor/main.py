from utils import get_computer_choice, determine_winner

def main():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if user_choice == 'q':
            print("Thank you for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 30)

if __name__ == "__main__":
    main()
