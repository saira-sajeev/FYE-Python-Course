"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 1.2.3 - Cookie Recipe
Date: 08/30/2024

Description:
    Prompts the user to enter how many cookies they want to make, and then informs the user how many cups of each ingredient they need.
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
    cookies = int(input("How many cookies do you want to make? "))
    #formulas to calculate how many of each ingredient you need
    butter = float(cookies/38.4)
    sugar = float(cookies/32)
    flour = float(cookies/19.2)
    #informing the user of how much they need
    print(f'To make {cookies:,} cookies, you will need:')
    print(f'{butter:10,.2f} cups of butter')   
    print(f'{sugar:10,.2f} cups of sugar')
    print(f'{flour:10,.2f} cups of flour')     

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()