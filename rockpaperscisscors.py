#Latrez O'Neal
#Rock Paper Scissors
#init
# = gets the value of
# == is equal to
import random
#Main
print("Welcome to Rock, Paper, Scissors")
while True: #infinite Loop
    #Players Choice
    print("Please select one of the three options")
    player1=input("Selection: ")
    #Computer's Choice
    #Randint
    computer = random.randint(1,3)
    if computer == 1:
        computer= "rock"
        print("Computer chose rock")
    elif computer== 2:
        computer= "paper"
        print("Computer chose paper")
    if computer == 3:
        computer= "scissors"
        print("Computer chose scissors")
    #Determine the outcome
    if player1== "rock" and computer =="rock":
        print("Tie Game!")
    if player1== "rock" and computer =="paper":
        print("Computer wins!")
    if player1== "rock" and computer =="scissors":
        print("player1 wins!")


    #Ask player if they want to continue
    playagain= input("Would you like to play again")
    if playagain == ("yes"):
                    print("restarting....")




