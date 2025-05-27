# Function to generate a Batman name based on user input
def generate_batman_name():
    # Ask the user for three pieces of information
    city = input("Choose your city (Gotham, Metropolis, Star City): ").lower()
    animal = input("Choose your animal (Bat, Panther, Eagle): ").lower()
    weapon = input("Choose your weapon (Batarang, Sword, Boomerang): ").lower()

    # Generate the Batman name based on the choices
    if city == "gotham":
        if animal == "bat":
            if weapon == "batarang":
                name = "The Dark Knight"
            elif weapon == "sword":
                name = "The Shadow Blade"
            else:
                name = "The Boomerang Avenger"
        elif animal == "panther":
            name = "The Midnight Panther"
        else:
            name = "The Eagle of Gotham"

    elif city == "metropolis":
        if animal == "bat":
            name = "The Metropolis Bat"
        elif animal == "panther":
            name = "The Steel Panther"
        else:
            name = "The Golden Eagle"

    elif city == "star city":
        if animal == "bat":
            name = "The Star Bat"
        elif animal == "panther":
            name = "The Star Panther"
        else:
            name = "The Sky Eagle"

    # Print out the generated Batman name
    print(f"Your Batman name is: {name}")

# Main Program
def main():
    print("Welcome to the Batman Name Generator!")
    generate_batman_name()

if __name__ == "__main__":
    main()
