"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 2.2.3. Roulette Colors
Date: 09/06/2024

Description:
 Prompts the user for a pocket number, and then displays the color of that pocket.
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


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Prompts user to enter the number of the pocket
    number = int(input("Please choose a pocket number: "))
    
    if number == 0:
        color = "green"
    elif 1 <= number <= 10:
        if number%2 == 0:
            color = "black"
        else:
            color = "red"
    elif 11 <= number <= 18:
        if number%2 == 0:
            color = "red"
        else:
            color = "black" 
    elif 19 <= number <=28:
        if number%2 == 0:
            color = "black"
        else:
            color = "red"
    elif 29<= number <=36:
        if number%2 == 0:
            color = "red"
        else:
            color = "black"
    else:
        return print("  Invalid Input!")

    print(f"  Pocket number {number} is {color}.")
   

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()