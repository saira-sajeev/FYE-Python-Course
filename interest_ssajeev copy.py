"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 1.2.2 - Interest
Date: 08/29/2024

Description:
    Prompts the user to enter information about their bank deposit in order to calculate the future value of their money in the bank.
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
    print("Enter the following parameters.")
    #commands to prompt the user for their inputs
    p = float(input("  The initial deposit? "))
    R = float(input("  The annual interest rate in percent? "))
    t = float(input("  The number of years the account earn interest? "))
    n = float(input("  The number of times interest is compounded each year: "))
    r = R/100 #number entered needs to be converted to a decimal
    #command to calculate the fuel efficiency
    FV = float(p*(1+(r/n))**(n*t))
    #command to inform the user of their future value
    print(f'The balance of this account will be ${FV:,.2f} after {t} years.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()