"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 5.2.1 - Maze
Date: 09/26/2024

Description:
    Using the turtle import function, navigate a maze png without touching the walls.

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
    #function for dimensions of the imported turtle case
    setup(564, 564)
    bgpic("maze.png")
    shape("turtle")
    color("green")
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    #fucntions for moving forward and turning
    #forward for moving: counted the boxes and multiplied by 12 pixels because each box is 12 pixels
    forward(12)
    right(90)
    forward(35)
    left(90)
    forward(72)
    left(90)
    forward(48)
    right(90)
    forward(24)
    left(90)
    forward(24)
    left(90)
    forward(14*12)
    left(90)
    forward(24)
    right(90)
    forward(72)
    right(90)
    forward(24)
    left(90)
    forward(24)
    right(90)
    forward(48)
    left(90)
    forward(24)
    right(90)
    forward(72)
    right(90)
    forward(72)
    left(90)
    forward(48)
    left(90)
    forward(24)
    right(90)
    forward(24)
    right(90)
    forward(30*12)
    right(90)
    forward(12*19)
    left(90)
    forward(24)








"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
