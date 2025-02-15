"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 6.2.4 - Spiral
Date: 10/06/2024

Description:
    Using the math and turtle modules, draw an Archimedean spiral using the equations for the x and y path.

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
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    import math as m
    #setting x,y,and theta to zero to initialize values for each variable
    theta = 0
    x = 0
    y = 0
    speed(100)
    '''radius = int(m.sqrt(((m.degrees(theta)*m.cos(theta))/m.pi**2)**2 + ((m.degrees(theta)*m.sin(theta))/m.pi**2)**2))'''
    #setting origin point for the spiral
    goto(x,y)
    #use a while function to keep solving for x and y components of each point on the spiral
    #increase theta in range from 0 to 38
    while theta <= 37.6:
        theta += 0.05
        x = (m.degrees(theta)*m.cos(theta))/m.pi**2
        y = (m.degrees(theta)*m.sin(theta))/m.pi**2
        goto(x, y)
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
