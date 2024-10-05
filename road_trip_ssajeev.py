"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 1.2.1 - Road Trip
Date: 08/29/2024

Description:
    Prompts the user to enter the distance they're driving, the gas price, and their mpg to calculate the fuel cost for their trip.

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
    print("Road trip fuel cost estimator:")
    #commands to prompt the user for their inputs
    distance = float(input("  How far away is your destination (miles)? "))
    price = float(input("  What is the average price of gas (dollars per gallon)? "))
    mpg = float(input("  What is the fuel efficiency of your vehicle (mpg)? "))\
    #command to calculate the fuel efficiency
    cost = int((2*distance*price)/mpg)
    #command to inform the user of their cost
    print()
    print(f'The fuel cost for this trip is approximately ${cost}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()