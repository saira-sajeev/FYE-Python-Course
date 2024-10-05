"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 6.2.2 - Rock Paper Scissors
Date: 10/05/2024

Description:
    Uses the random module in python to return rock, paper, or scissors. Then 3 functions are used to determine a play by the computer, user, and then shows the winner.
Contributors:
    None
My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
#make a get_computer_choice function that randomly chooses a play option from a defined list
def get_computer_choice():
    import random as r
    choices = ['rock', 'paper', 'scissors']
    computer_choice = r.choice(choices)
    return computer_choice
#function to get the user's play. If the user enters a wrong choice, re-ask the question
def get_player_choice():
    user_choice = input('Choose rock, paper, or scissors: ')
    while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print('You made an invalid choice. Please try again.')
        user_choice = input('Choose rock, paper, or scissors: ') 
    return user_choice
#this function determines a winner based on a defined set of rules. Define the rules inside the function.
#uses nested if loops to check conitions and determine winner
def get_winner(computer_choice, user_choice):
    if computer_choice == "rock":
        if user_choice == "rock":
            return "tie"
        elif user_choice == "paper":
            return "player"
        elif user_choice == "scissors":
            return "computer"
    elif computer_choice == "paper":
        if user_choice == "rock":
            return "computer"
        elif user_choice == "paper":
            return "tie"
        elif user_choice == "scissors":
            return "player"
    elif computer_choice == "scissors":
        if user_choice == "rock":
            return "player"
        elif user_choice == "paper":
            return "computer"
        elif user_choice == "scissors":
            return "tie"
def main():
    #set winner to tie outside the while loop to get it to iterate through the loop.
    winner = "tie"
    #while loop will keep the game running if the result is a tie
    while winner == "tie":
        computer_choice = get_computer_choice()
        user_choice = get_player_choice()
        print(f"  The computer chose {computer_choice}, and you chose {user_choice}.")
        winner = get_winner(computer_choice, user_choice)
        if winner == "player":
            print(f"  {user_choice} beats {computer_choice}")
            print("  You won the game!")
            break
        elif winner == "computer":
            print(f"  {computer_choice} beats {user_choice}")
            print("  You lost.  Better luck next time.")
            break
        else:
            print("  It's a tie. Starting over.\n")
            
            
    #final print statement
    print("Thanks for playing.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()