"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 4.2.5 Prime List
Date: 09/20/2024

Description:
Uses is_prime function to list all the prime numbers from 2 to a number the user enters
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

#function to determine if number is prime
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False

    return True 


def main():
    #empty list for prime numbers to be added to
    prime_numbers = []
    limit = int(input('Enter a positive integer: '))
    #goes through numbers in the range and checks them to see if they are prime numbers
    for numbers in range(2, limit+1):
        if is_prime(numbers) == True:
            prime_numbers.append(numbers)
    #.join function used to print list of numbers without []        
    print(f'The primes up to {limit} are: {", ".join(str(num) for num in prime_numbers)}')



if __name__ == "__main__":
  main()