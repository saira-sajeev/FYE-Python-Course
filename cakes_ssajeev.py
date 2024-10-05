"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 3.2.1 Cakes
Date: 09/12/24

Description:
Prompts the user to enter a number and then displays a ASCII cake drawing with that many layers.
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
    #ask user to input the number of layers
    layers = int(input("Enter the number of layers: "))
    stars_count = 1
    for current_layer in range(1, layers+1):
        #spaces required before each layer line is total number of layers - current layer number
        space_count = layers - current_layer
        #building the line_to_print as individual print statements will insert newlines after each print
        #we want a continuous set of starts
        line_to_print = "["
        #doing range from 0 to stars_count which will loop from 0 to stars_count - 1
        for count_stars in range (0, stars_count):
            line_to_print += "*"
        line_to_print += "]"
        #insert the right number of spaces before the current layer line
        #multiplying a single space with space_count will give a string with that many spaces
        line_to_print = space_count * " " + line_to_print
        print (line_to_print)
        stars_count +=2

            


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()