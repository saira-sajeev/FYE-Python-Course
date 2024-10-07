"""
Author: Saira, ssajeev@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/06/24

Description:
   Using the vowel file I created defining the turtle commands for letters and importing that file, generate the letters in a random order.

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import random as r
import vowels as v


"""Write new functions below this line (starting with unit 4)."""


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
    """Write your mainline logic below this line (then delete this line)."""

    x,y = pos()
    
    list_of_vowels = ['a','e','i','o','u']
    
    # Draw each letter and move to the next position
    r.shuffle(list_of_vowels) # iterate through list of letters randomly
    for letter in list_of_vowels:
        if letter == 'a':
            v.draw_a(x, y)
        elif letter == 'e':
            v.draw_e(x, y)
        elif letter == 'i':
            v.draw_i(x, y)
        elif letter == 'o':
            v.draw_o(x, y)
        elif letter == 'u':
            v.draw_u(x, y)
        x += 90 #move horizontally after every letter is drawn
          

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
