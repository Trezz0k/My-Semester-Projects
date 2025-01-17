import random

# Function to play the Guess the Number Game
def guess_the_number():
    # Prompt for difficulty level
    difficulty = input("Choose a difficulty (Easy, Medium, Hard): ").lower()

    # Set range based on difficulty level
    if difficulty == "easy":
        max_num = 10
        max_guesses = 3
    elif difficulty == "medium":
        max_num = 20
        max_guesses = 5
    elif difficulty == "hard":
        max_num = 50
        max_guesses = 7
    else:
        print("Invalid difficulty. Defaulting to Easy.")
        max_num = 10
        max_guesses = 3

    # Generate a random number based on the difficulty range
    secret_number = random.randint(1, max_num)

    # Give the player a limited number of guesses
    print(f"\nI have selected a number between 1 and {max_num}. You have {max_guesses} attempts to guess it correctly.")

    # Loop for the guesses
    guesses_left = max_guesses
    while guesses_left > 0:
        try:
            guess = int(input(f"Guess the number (You have {guesses_left} guesses left): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break
        else:
            guesses_left -= 1
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")

            # If no guesses left, the player loses
            if guesses_left == 0:
                print(f"Sorry, you've lost the game. The correct number was {secret_number}. Better luck next time!")

# Main program entry point
if __name__ == "__main__":
    guess_the_number()
