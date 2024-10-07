"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/06/2024

Description:
    This program will be a file I import to random vowels. It uses turtle to individually give commands to draw each vowel.

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


def draw_a(x=0, y=0):
    #draw the character a
    penup()
    goto(x+24, y)
    setheading(0)
    pendown()
    circle(24)
    penup()
    goto(x+48, y+48)
    setheading(270)
    pendown()
    forward(48)
    

def draw_e(x=0, y=0):
    #draw the character e
    penup()
    goto(x, y+24)
    setheading(0)
    pendown()
    forward(48)
    left(90)
    circle(24,320)
    

def draw_i(x=0, y=0):
    #draw the character i
    penup()
    goto(x+24,y)
    setheading(90)
    pendown()
    forward(48)
    penup()
    forward(24)
    pendown()
    forward(2)
    penup()
    

def draw_o(x=0, y=0):
    #draw the character o
    penup()
    goto(x+24, y)
    setheading(0)
    pendown()
    circle(24)
    penup()
    
def draw_u(x=0, y=0):
    #draw the character u
    penup()
    goto(x,y+48)
    setheading(270)
    pendown()
    forward(24)
    circle(24, 180)
    forward(24)
    setheading(270)
    forward(48)
    
def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    pass



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
