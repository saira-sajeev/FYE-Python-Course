"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 2.2.2. Software Sales
Date: 09/06/2024

Description:
 Tells the user how much discount they get and how much they have to pay after they enter the number of packages they get.
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
    #Prompts user to enter the number of packages they're buying
    packages = int(input("How many packages will be purchased: "))
    cost = float(880)

    if packages < 0:
        return print("  Invalid Input!")
    elif packages >= 4 and packages <= 39:
        discount = 0.10
        print("  10% discount applied.")
    elif packages >= 40 and packages <= 199:
        discount = 0.15
        print("  15% discount applied.")
    elif packages >= 200 and packages <= 999:
        discount = 0.30
        print("  30% discount applied.")
    elif packages >= 1000:
        discount = 0.42
        print("  42% discount applied.")
    else:
        print("  No discount applied.")
        discount = 0
    
    final_cost = (packages*cost)*(1-discount)
    print(f"  The total price to purchase {packages} packages is ${final_cost:,.2f}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()