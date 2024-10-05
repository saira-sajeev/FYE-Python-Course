"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 2.2.5. Fluid Mechanics
Date: 09/07/2024

Description: Calculates the Reynolds number for a user after they enter multiple parameters.
 Tells the user how much discount they get and how much they have to pay after they enter the number of packages they get.
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
    #Prompts the user to enter multiple values 
    temp = float(input("Enter the temperature in \u00b0C as 5, 20, or 50: "))
    velocity = float(input("Enter the velocity of water in the pipe (m/s): "))
    diameter = float(input("Enter the pipe's diameter (m): "))
    #to determine what viscosity value to use
    if temp == 5:
        viscosity = 1.52*10**(-6)
    elif temp == 20:
        viscosity = 1.00*10**(-6)
    else:
        viscosity = 5.54*10**(-7)
    #equation to calculate Reynolds value
    Reynolds_number = (velocity*diameter)/viscosity
    print(f"At {temp}\u00b0C, the Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe is {Reynolds_number:.2e}.")

5
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()