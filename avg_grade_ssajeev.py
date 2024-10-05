"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 4.2.3 Avg Grade
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

#this function asks the user to enter scores and re-enter if the value doesn't fit in the range of [0,100]
def get_valid_score():
    valid_score = -1
    while True:
        valid_score = float(input("Enter a score: "))
        if valid_score < 0 or valid_score > 100:
            print("  Invalid Input. Please try again.")
        else:
            return valid_score
#this function calculates the average of the scores entered        
def calc_average(scores):
    total_score = 0
    for score in scores:
        total_score += score
    
    average = total_score / len(scores)
    return average
#this function assigns letter grades to score values
def determine_grade(score):
    if score >= 92 and score <=100:
        return 'A'
    elif score >= 82 and score <= 92:
        return 'B'
    elif score >= 73 and score <= 82:
        return 'C'
    elif score >= 64 and score <= 73:
        return 'D'
    elif score >=0 and score <= 64:
        return 'F'

def main():
    
    scores = []
    for count in range (0, 5):
        score = get_valid_score()
        scores.append(score)
        grade = determine_grade(score)
        print(f"  The letter grade for {score} is {grade}.")

    #print final results
    average_score = calc_average(scores)
    average_grade = determine_grade(average_score)
    print()
    print("Results:")
    print(f"  The average score is{average_score: .2f}.")
    print(f"  The letter grade for{average_score: .2f} is {average_grade}.")      

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()