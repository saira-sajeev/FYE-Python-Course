"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 5.2.3 - star pattern
Date: 09/26/2024

Description:
    Prompts user for a amount of points. Then draw a star with that many points using turtle. Star should have correct orientation and be filled with color.

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
    width(7)
    side_length = 60  # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length)  # Start at the bottom of the star.
    pendown()


def main():
    """Write your mainline logic below this line (then delete this line)."""
    
    setup(564, 564)
    width(7)
    side_length = 60  # Also the radius of a circle enclosed by the star.
    goto(0, -side_length) # setting the starting point
    points = int(input("Enter the number of points: "))
    #calculations to determine angles that need to be turned at each corner
    A = 360/points
    B = 2*A
    #calculated what angle I need to start the cursor at
    starting_angle = (180-B)/2
    right(starting_angle)
    width(7)
    sides = 0
    #color function to determine color and begin fill and end fill to color the shape
    color('black','green')
    begin_fill()
    #while loop to check that point value entered is above zero
    if points > 0:
        for sides in range (1, points+1):
            sides += 1
            forward(60)
            left(180-A)
            forward(60)
            right(180-B)
        end_fill()


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
