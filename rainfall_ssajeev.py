"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 3.2.3 Rainfall
Date: 09/13/24

Description:
Prompts user to ask for a number of years, and then asks the user for inches of rainfall for each month in that time period. The program will then return the number of months, total inches of rain, and average rain per month for the entired time period.
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
    #input for number of years, and then setting variables to base values to later be changed throughout the loop
    years_input = int(input("Enter the number of years: "))
    if years_input == 0:
                print("Invalid input; years must be greater than 0.")
        
    rainfall_list = []
    total_rainfall = float(0)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for year in range (1, years_input+1):
        print(f"  For year No. {year}")
        current_month = 0
    #current_month variable allows me to cycle through each month for the course of multiple years
        while current_month < 12:
            rainfall = float(input(f"    Enter the rainfall for {months[current_month]}.: "))
            if rainfall < 0:
                print("    Invalid input; rainfall cannot be negative.")
                continue
            else:
                rainfall_list.append(rainfall)
                total_rainfall += rainfall
                current_month += 1

    if years_input > 0:
        number_of_months = len(rainfall_list)
        avg_rainfall = total_rainfall / number_of_months

        print(f"There are {number_of_months} months.")
        print(f"The total rainfall was {total_rainfall:.2f} inches.")
        print(f"The monthly average rainfall was {avg_rainfall:.2f} inches.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()


     