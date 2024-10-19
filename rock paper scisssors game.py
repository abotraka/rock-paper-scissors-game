import random  # Importing the random module to generate a random choice for the computer

def get_user_choice():
    """
    Prompts the user to enter their choice and validates the input.
    
    Returns:
        str: A lowercase character representing the user's choice ('r' for rock, 'p' for paper, 's' for scissors).
    """
    user_choice = input("Choose: Rock (r), Paper (p), Scissors (s): ").lower()
    while user_choice not in ['r', 'p', 's']:  # Validating user input
        user_choice = input("Invalid choice. Choose: Rock (r), Paper (p), Scissors (s): ").lower()
    return user_choice  # Return the valid user choice

def get_computer_choice():
    """
    Randomly selects a choice for the computer.
    
    Returns:
        str: A lowercase character representing the computer's choice ('r' for rock, 'p' for paper, 's' for scissors).
    """
    choices = ['r', 'p', 's']
    return random.choice(choices)  # Randomly select and return a choice for the computer

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the game based on user and computer choices.
    
    Args:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.
        
    Returns:
        str: A message indicating whether the user wins, the computer wins, or it's a tie.
    """
    if user_choice == computer_choice:  # Checking for a tie
        return "It's a tie!"
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):  # Checking if user wins
        return "You win!"
    else:  # If above conditions are not met, the computer wins
        return "Computer wins!"

def play_game():
    """
    Plays a single round of Rock-Paper-Scissors, showing the choices and the result.
    """
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()  # Get the user's choice
    computer_choice = get_computer_choice()  # Get the computer's choice
    print(f"Your choice: {user_choice}")  # Print the user's choice
    print(f"Computer's choice: {computer_choice}")  # Print the computer's choice
    result = determine_winner(user_choice, computer_choice)  # Determine the winner
    print(result)  # Print the result of the game

if __name__ == "__main__":
    play_game()  # Execute the play_game function if the script is run directly
