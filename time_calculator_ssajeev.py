"""
Author: Saira Sajeev, ssajeev@purdue.edu
Assignment: 2.2.4. Time Calculator
Date: 09/08/24

Description:
Prompts the user to enter a number of seconds and converts it into days, hours, minutes, and seconds.
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
    #defining number of seconds in each value
    seconds_in_day = 86400
    seconds_in_hour = 3600
    seconds_in_minute = 60
    #prompt user for their input
    user_input_seconds = int(input("Please enter a time in seconds: "))
    
    #finding values 
    days = user_input_seconds // seconds_in_day
    remaining_seconds = user_input_seconds % seconds_in_day
   
    hours = remaining_seconds // seconds_in_hour
    remaining_seconds = remaining_seconds % seconds_in_hour

    minutes = remaining_seconds // seconds_in_minute
    remaining_seconds = remaining_seconds % seconds_in_minute

    seconds = remaining_seconds

    #creating output string
    output_string = ''
    if days > 0:
        output_string = str(days) + ' day(s)'

    #just 'hours' if there are no days. ', hours' if there are days. 'and hours' if there are no minutes and seconds.
    if days <= 0 and hours > 0:
        output_string = output_string + str(hours) + ' hour(s)'
    elif days > 0 and minutes <= 0 and seconds <= 0 and hours > 0:
        output_string = output_string + ' and ' + str(hours) + ' hour(s)'
    elif days > 0 and hours > 0:
        output_string = output_string + ', ' + str(hours) + ' hour(s)'

    #just 'minutes' if there are no days and hours. ', minutes' if there are days or hours. 'and hours' if there are no seconds.
    if days <= 0 and hours <= 0 and minutes > 0:
        output_string = output_string + str(minutes) + ' minute(s)'
    elif (days > 0 or hours > 0) and seconds <= 0 and minutes > 0:
        output_string = output_string + ' and ' + str(minutes) + ' minute(s)'
    elif minutes > 0 and (days > 0 or hours > 0):
        output_string = output_string + ', ' + str(minutes) + ' minute(s)'

    #seconds always 'and seconds' as we have another statement if only seconds and there is nothing that will follow this
    if (days > 0 or hours > 0 or minutes > 0) and seconds > 0:
        output_string = output_string + ' and ' + str(seconds) + ' second(s)'
    #build the final output string for less than one minute scenario or for all other scenarios
    if user_input_seconds < seconds_in_minute:
        output_string = "  " + str(seconds) + ' seconds is less than one minute.'
    else:
        output_string = "  " + f'{user_input_seconds:,d}' + ' seconds equals ' + output_string + '.'

    #output_string is fully built and formatted now. so just print it as is.
    print (output_string)


    
    
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()