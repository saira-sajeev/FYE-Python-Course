"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 5.2.2 Spiral
Date: 09/26/2024

Description:
     Using turtle commands, draw a octogonal spiral that starts with sides 4 pixels long and increases by 4 pixels every 45 degree turn.

Contributors:
    Name, login@purdue.edu [repeat for each]

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
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(10)


def main():
    """Write your mainline logic below this line (then delete this line)."""
#using a for loop to draw the spiral
#use range from 1 to number that I find based on guess and check
for pixels in range(1,43):
    #multiplies by 4 pixels, turns 45 degrees and multiplies by 4 again
    width(5)
    forward(4*pixels)
    left(45)



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
