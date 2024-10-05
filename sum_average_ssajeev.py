"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 3.2.2 Sum Average
Date: 09/13/24

Description:
Prompts the user to enter a a series of non-negative number and adds us all the values entered until a negative number is entered.
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
   
    #getting input value, and setting variables that will be inside the while loop to zero
    message = "Enter a non-negative number (negative to quit): "
    numbers = float(input(message))
    total = 0
    count = 0
    #while loop to recalculate total and average with each new non-negative value added.
    if numbers >= 0:
        while numbers >= 0:
            count += 1
            total += numbers
            numbers = float(input(message))
            average = total/count
        print(f"  You entered {count} numbers.")
        print(f"  Their sum is {total:.3f} and their average is {average:.3f}.")
    else:
        print("  You didn't enter any numbers.")                    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
    
     