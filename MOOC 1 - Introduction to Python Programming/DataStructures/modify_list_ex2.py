#Write a function called multiply_strings. Multiply
#strings should have one parameter, a list of strings.
#It should return a modified list according to the
#following changes:
#
# - Every string stored at an even index should be
#   doubled.
# - Every string stored at an index that is a multiple
#   of 3 should be tripled.
# - Every other string should remain unchanged.
#
#These changes should "stack": the string stored at index
#6 should be duplicated six times (2 * 3).
#
#Then, return the new list. You may assume that 0 is a
#multiple of 2 and 3.
#
#Hint: To do this, you need to modify the values of the
#list using their indices, e.g. a_list[1]. If you're not
#using their indices, your answer won't work!


#Write your function here!
def multiply_strings(input_list):
    #error handling for "D"
    input_list[3]*3
    
    # skip every other index 
    for item in input_list[0:len(input_list)]:

        index = input_list.index(item)
        print("Index: #" + str(index))
        
    # double even index values note: index has 1 added to address the -1 position
        if (index) % 2 == 0:
            newvalue = input_list.pop(index) * 2
            print(newvalue)
            input_list.insert(index, newvalue)

    #Every string stored at an index that is a multiple of 3 should be tripled.    
        if (index) % 3 == 0:
            newvalue = input_list.pop(index) * 3
            print(newvalue)
            input_list.insert(index, newvalue)
    
    return input_list

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#['AAAAAA', 'B', 'CC', 'DDD', 'EE', 'F', 'GGGGGG']
test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))


