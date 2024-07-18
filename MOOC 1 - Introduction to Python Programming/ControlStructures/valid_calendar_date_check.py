#Write a function called check_date. check_date should
#require two positional parameters: a string representing
#the name of a month, and an integer representing a date.
#check_date should also have a keyword parameter called
#is_leap_year, assumed to be False, representing whether or
#not it's a leap year.
#
#Return True if the date is a valid calendar date. Return
#False if it is not. A date may not be a valid calendar
#date if the month isn't a real month, or if that date does
#not exist for that month. You can see some examples at the
#end of this file.
#
#Remember: 30 days has September, April, June, and November.
#All the rest have 31, except February, which has 28, until
#Leap Year gives it 29.
#
#You may assume that day will be greater than 0 (you don't
#need to check negative or zero values for day).


#Write your function here!
def check_date(month_name, day_number, is_leap_year = False):
#    valid_months = ["January", "February", "March", "April", "May", "June", "July", #"August", "September", "October", "November", "December"]
#    if month_name in valid_months:
#        return True    
#    else:
#        return False
    if month_name == "January" and day_number <= 31:
        return True
    elif month_name == "February":
        if is_leap_year == False:
            if day_number <= 28:
                return True
            else:
                return False
        elif is_leap_year == True:
            if day_number <= 29:
                return True
            else:
                return False
    elif month_name == "March" and day_number <= 31:
        return True
    elif month_name == "April" and day_number <= 30:
        return True
    elif month_name == "May" and day_number <= 31:
        return True
    elif month_name == "June" and day_number <= 30:
        return True
    elif month_name == "July" and day_number <= 31:
        return True  
    elif month_name == "August" and day_number <= 31:
        return True 
    elif month_name == "September" and day_number <= 30:
        return True     
    elif month_name == "October" and day_number <= 31:
        return True
    elif month_name == "November" and day_number <= 30:
        return True   
    elif month_name == "December" and day_number <= 31:
        return True       
    else:
        return False       
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, each on their own line.
print(check_date("January", 31))
print(check_date("February", 29, is_leap_year = True))
print(check_date("Techtember", 15, is_leap_year = True))
print(check_date("June", 31))
print(check_date("February", 29, is_leap_year = False))



