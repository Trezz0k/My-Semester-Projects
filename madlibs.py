#Latrez O'Neal Mad Libs 12/13/24
def madlibs_game():
    print("Welcome to the Mad Libs game!")
    print("Please fill in the blanks with the requested types of words.\n")

    # Asking the user for input
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb (past tense): ")
    place1 = input("Enter a place: ")

    # Creating the Mad Libs story
    story = f"One day, a {adjective1} {noun1} decided to {verb1} all the way to {place1}. It was a very strange adventure!"

    # Printing the completed story
    print("\nHere's your Mad Libs story:")
    print(story)

# Call the function to start the game
madlibs_game()

noun = ("male")
adjective = ("tall")
verb = ("ran")
place = ("home")

story = f"One day, a tall man decided to ran all the way to home. It was a very strange adventure!"
print=("\nHere's your Mad Libs story:")
print=("One day, a tall man decided to ran all the way to home. It was a very strange adventure!")
