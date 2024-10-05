"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 4.2.1 Falling
Date: 09/19/2024

Description:
 Uses a function to calculate the amount of distance an object falls during several time intervals.
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

#gravity constant and falling_dist function defined outside of main function
g = float(8.87)
def falling_dist(time):
        return float((0.5*g*(time)**2))

def main():
    
    #printing format
    print("Time (s)  Distance (m)")
    print("----------------------")
    
    #iterating through ranges of times and calling falling_dist function
    for seconds in range(5,55,5):
        distance = falling_dist(seconds)
        print(f'{seconds:8} {distance:13.1f}')
        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()