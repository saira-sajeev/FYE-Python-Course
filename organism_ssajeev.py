"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 3.2.4 - Organism
Date: 09/15/2024

Description:
    Prompts the user to enter several pieces of information about a population of organisms and then calculates the population across multiple days.

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
    starting_pop = float(input("Starting population, in thousands: "))
    percent_increase = int(input("Average daily increase, in percent: "))
    number_of_days = int(input("Number of days to multiply: "))
    new_population = starting_pop
    #print a table 
    print("Day   Approx. Pop")
    #to print the intial value of the population
    print(f"  0{starting_pop:14,.3f}")
    #for loop to go through list of days and calculate population for each day
    for day in range(1,number_of_days+1):
        chart_day = day
        new_population = new_population*(1+(percent_increase/100))
        print(f'{chart_day:3}{new_population:14,.3f}')
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()