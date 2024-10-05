"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 6.2.1 - Math Quiz
Date: 10/05/2024

Description:
    Uses the random module in python to return two random numbers and then prompts the user to enter an answer to a division problem using the two generated numbers.

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
#random_factor function that generates a random 2 digit number and a random one digit number
def random_factor(number_of_digits):
        import random as r
        lower_limit = 10**(number_of_digits-1)
        upper_limit = (10**number_of_digits)- 1
        random_number = r.randint(lower_limit,upper_limit)
        return random_number
#call ranom_factor function in main function 
def main():
    
    correct_answer = int(random_factor(2))
    denominator = int(random_factor(1))
    #caclculate the numerator value by multiplyinf the two generated numbers
    numerator = denominator*correct_answer
    #notation for printing game format and prompting user to enter the correct answer  
    print(f"{numerator:4}") 
    print(f"÷  {denominator}") 
    print('----')
    #prompts user to enter their answer
    user_answer = int(input("= "))
    if user_answer != correct_answer:
        print(f"Sorry, the correct answer is {correct_answer}.")
    else:
        print("Great job, that's correct!")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()