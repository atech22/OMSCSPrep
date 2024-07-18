#Write a function called find_median. find_median
#should take as input a string representing a filename.
#The file corresponding to that filename will be a list
#of integers, one integer per line. find_median should
#return the median of the numbers in the file.
#
#If there is an odd number of values in the file, then
#find_median will return the middle value from the numbers
#in the file after they're sorted.
#
#If there is an even number of values in the file, then
#find_median should return the average of the two middle
#values after they're sorted.
#
#For example, in the dropdown in the top left you'll find a
#file named FindMedianInput.txt. There are 19 numbers in
#this file, so the median is the value at index 10 after
#sorting them: 16.
#
#You may assume that all lines in the file will contain a
#positive integer (greater than 0). There may be duplicates.


#Write your function here!
def find_median(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        numbers = [int(line.strip()) for line in lines]
        numbers.sort()
        n = len(numbers)
        if n % 2 == 1:
            return numbers[n // 2]
        else:
            middle1 = numbers[n // 2 - 1]
            middle2 = numbers[n // 2]
            return (middle1 + middle2) / 2

####My first try to implement
####
####def find_median(filename):
####
####    try:
####        file_reader = open(filename, "r")
####        file_content = file_reader.read()
####        list_of_ints = []
####        
####        #change the line from string to int
####        for line in file_content:
####            num = int(line)strip()
####            list_of_ints.append(num)
####        list_of_ints.sort()
####        #print(list_of_ints)
####        
####        # find the median
####        
####        if len(list_of_ints) % 2 == 0:
####            position = (len(list_of_ints) / 2)
####            position = int(position)
####            return list_of_ints[position]
####            
####               
####        else:
####             position1 = ((len(list_of_ints) / 2) + 0.5)
####             position1 = int(position1)
####             median1 = (list_of_ints[position1])
####             position2 = ((len(list_of_ints) / 2) - 0.5)
####             position2 = int(position2)
####             median2 = (list_of_ints[position2])   
####             return (median1 + median2) / 2
####
####    except:
####        return "an error has occurred when reading the file"
####    finally:
####        file_reader.close()
####    
####
#####Below are some lines of code that will test your function.
#####You can change the value of the variable(s) to test your
#####function with different inputs.
#####
#####If your function works correctly, this will originally
#####print: 16
####print(find_median("FindMedianInput.txt"))


