# This is the function to collect user info: name, age, day of the week, and coupon code
def get_user_input():
    # Getting basic info from person
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    day_of_week = input("Enter the day of the week (e.g., Monday, Friday): ").lower()
    coupon_code = input("Enter a coupon code (if any): ").upper()

    return name, age, day_of_week, coupon_code

# Function to calculate the ticket price based on age, day of the week, and coupon code
def calculate_ticket_price(age, day_of_week, coupon_code):
    # Default ticket price for adults
    ticket_price = 100

    # Age logic for children (ages 3 and under get free admission)
    if age <= 3:
        ticket_price = 0
    elif 4 <= age <= 17:  # Kids and students (ages 4-17)
        if day_of_week in ['saturday', 'sunday']:
            ticket_price = 100  # Full price on weekends
        else:
            ticket_price = 50  # Half price on weekdays

        # Special coupon codes for kids/students
        if coupon_code == "FREEFRIDAY" and day_of_week == "friday":
            ticket_price = 0  # Free on Friday with FREEFRIDAY code
        elif coupon_code == "SUNDAY10" and day_of_week == "sunday":
            ticket_price = 90  # $10 discount on Sunday with SUNDAY10 code
    # Adults (18 and older) always pay full price
    else:
        ticket_price = 100

    return ticket_price

# Function to display the ticket details to the user
def display_ticket(name, day_of_week, ticket_price):
    # Display the ticket information clearly
    print("\n" + "="*40)
    print(f"Ticket for {name}")
    print(f"Day: {day_of_week.capitalize()}")
    print(f"Price: ${ticket_price}")
    print("="*40)

# Main function to orchestrate the ticket generation process
def generate_ticket():
    # Get user input
    name, age, day_of_week, coupon_code = get_user_input()

    # Calculate the ticket price based on the user input
    ticket_price = calculate_ticket_price(age, day_of_week, coupon_code)

    # Display the ticket details to the user
    display_ticket(name, day_of_week, ticket_price)

# Run the program
generate_ticket()
