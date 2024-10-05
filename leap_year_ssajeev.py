"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 2.2.1. Leap Year
Date: 09/06/2024

Description:
   Tells the user how many days are in February in a specific user.
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
    #Prompts user to enter year
    year = int(input("Enter a year: "))
   #boolean that checks if the year entered is divisible by 10
    if year%100 == 0 and year%400 == 0 or year%100 != 0 and year%4 == 0:
        print(f"The year {year} is a leap year.")
        print(f"February of {year} has 29 days.")
    else:
        print(f"The year {year} is not a leap year.")
        print(f"February of {year} has 28 days.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()