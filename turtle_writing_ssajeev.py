"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 5.2.4 - Turtle Writing
Date: 09/27/2024

Description:
    After writing multiple fucntions for each letter, write out a sentence by calling each function and having turtle draw each letter.

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
    setup(600, 400)
    width(9)
    color('purple')


def draw_S(x, y): 
    penup()
    goto(x, y)
    pendown()
    forward(24)
    circle(24,180)
    right(180)
    circle(24,-180)
    forward(-22)

def draw_t(x, y):
    penup()
    goto(x+24, y)
    pendown()
    goto(x+24, y+96)
    penup()
    goto(x, y+72)
    pendown()
    setheading(0)
    forward(48)

def draw_e(x, y):
    penup()
    goto(x, y+24)
    setheading(0)
    pendown()
    forward(48)
    left(90)
    circle(24,320)

def draw_p(x, y): 
    penup()
    goto(x+24, y)
    pendown()
    setheading (0)
    circle(24)
    penup()
    goto(x, y+48)
    setheading(270)
    pendown()
    forward(96)

def draw_s(x, y):
    penup()
    goto(x+12, y)
    setheading(0)
    pendown()
    forward(12)
    circle(12, 180)
    right(180)
    circle(12, -180)
    forward(-10)

def draw_T(x, y):
    penup()
    goto(x+24, y)
    setheading(90)
    pendown()
    forward(96)
    penup()
    goto(x, y+96)
    setheading(0)
    pendown()
    forward(48)

def draw_o(x, y):
    penup()
    goto(x+24, y)
    pendown()
    circle(24)

def draw_L(x, y):
    penup()
    goto(x, y)
    pendown()
    forward(48)
    penup()
    goto(x, y)
    setheading(90)
    pendown()
    forward(96)

def draw_a(x, y):
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


def main():
    '''After these lines, call your letter drawing functions as needed to draw
    the words "Steps To Leaps".'''
    # Saving start x and y positions for later use in moving to the next line
    start_xpos = -250
    start_ypos = 80

    letter_spacing = 60
    word_spacing = 90

    xpos = start_xpos
    ypos = start_ypos
    
    #Each virtual bounding box is 48X96 
    
    draw_S(xpos, ypos)

    #increment only xpos for the same line
    xpos += letter_spacing
    
    draw_t(xpos, ypos)

    xpos += letter_spacing
    draw_e(xpos, ypos)

    xpos += letter_spacing
    draw_p(xpos, ypos)

    xpos += letter_spacing
    draw_s(xpos, ypos)

    #extra spacing for word
    xpos += word_spacing
    draw_T(xpos, ypos)

    xpos += letter_spacing
    draw_o(xpos, ypos)

    xpos = start_xpos #starting xpos
    ypos = start_ypos - (96*1.5)
    draw_L(xpos, ypos)

    xpos += letter_spacing
    draw_e(xpos, ypos)

    xpos += letter_spacing
    draw_a(xpos, ypos)

    xpos += letter_spacing
    draw_p(xpos, ypos)

    xpos += letter_spacing
    draw_s(xpos, ypos)

'''Do not change anything below this line.'''
if __name__ == "__main__":
    start()
    main()
    done()
