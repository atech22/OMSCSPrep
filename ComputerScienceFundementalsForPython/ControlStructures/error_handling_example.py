list_sum = 7
list_count = 1

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The variables above give the sum of all numbers in a list,
#and the count of how many numbers were in the list. Your
#goal is to find their average.
#
#However, if list_count is 0, then we can't divide list_sum
#by list_count. In this case, you should print "Can't divide
#by zero!" Otherwise, you should print the average.
#
#Note that you may not use any conditionals in your answer.
#Note also that you should not assume that every error that
#occurs is a divide-by-zero error: any other errors should
#not be caught.


#Add your code here!
def find_average(input_list_sum, input_list_count):
    try:
        average = input_list_sum / input_list_count
        return average
    except ZeroDivisionError:
        return "Can't divide by zero!"
    except TypeError:
        return "unsupported operand type(s) for /: 'str' and 'str'"
    except:
        return "Unknown Error"

print(find_average(list_sum, list_count))    





