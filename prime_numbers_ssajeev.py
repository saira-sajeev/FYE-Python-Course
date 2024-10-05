"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 4.2.4 Prime Numbers
Date: 09/20/2024

Description:
Uses a function that determines wheter a number is prime or not and will keep taking inputs until the user enters a negative number.
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
  
  #Prompts the user for a number and checks if it's prime.
  while True:
    number = int(input("Enter a positive integer (-1 to quit): "))
    #command to end loop if -1 is entered
    if number == -1:
      break
    #output results based on the boolean result
    if is_prime(number):
      print(f"  {number} is prime!")
    else:
      print(f"  {number} is not prime.")

if __name__ == "__main__":
  main()