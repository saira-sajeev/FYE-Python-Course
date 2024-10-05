"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 4.2.2 Lucky Sum
Date: 09/20/2024

Description:
 Uses a function to calculate the sum of the smallest argument and largest argument that are divisible by 7 in the range of two numbers entered by the user.
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

#lucky_sum function defined outside of main function
def lucky_sum(small,large):
    
    #if loop to make sure the arguments are put in numerical order
    if small > large:
        largest = small
        smallest = large
    else:
        largest = large
        smallest = small
    lucky_sum_list = []
    for number in range(smallest, largest+1):
        if number%7 == 0:
            lucky_sum_list.append(number)
    final_sum = sum(lucky_sum_list)
    return(final_sum)
    


def main():
    
    small = int(input('Enter the first integer: '))
    large = int(input('Enter the second integer: '))

    print(f'The sum of the lucky numbers is {lucky_sum(small, large):,}.')


        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()