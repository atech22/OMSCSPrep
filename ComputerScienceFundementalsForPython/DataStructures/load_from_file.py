#Write a function called "load_file" that accepts one 
#parameter: a filename. The function should open the
#file and return the contents.#
#
# - If the contents of the file can be interpreted as
#   an integer, return the contents as an integer.
# - Otherwise, if the contents of the file can be
#   interpreted as a float, return the contents as a
#   float.
# - Otherwise, return the contents of the file as a
#   string.
#
#You may assume that the file has only one line.
#
#Hints:
#
# - Don't forget to close the file when you're done!
# - Remember, anything you read from a file is
#   initially interpreted as a string.


#Write your function here!
def load_file(filename):
    try:
        with open(filename, "r") as file_reader:
            loaded_content = file_reader.read().strip()
            if loaded_content.lstrip("-").isdigit():                      
                file_reader.close()
                return int(loaded_content)
            elif "." in loaded_content:
                file_reader.close()
                return float(loaded_content)
            else:
                file_reader.close()
                return loaded_content
    except FileNotFoundError:
        return None

#### The better way of doing this would be:

###This is going to look complex, but it's simpler than it
###looks! We'll take two slightly different approaches.
##
##def load_file(filename):
##    file_reader = open(filename, "r")
##    contents = file_reader.readline()
##    try:
##        return int(contents)
##    except:
##        try:
##           return float(contents)
##        except:
##            return contents
##    finally:
##        file_reader.close()


contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 123, followed by <class 'int'>.
contents = load_file("LoadFromFileInput.txt")
print(contents)
print(type(contents))


####Leaving this here for my own notes as I leveraged codewhisperer to rewrite my code and make it work. below was the original code I had trouble debugging

##    def load_file(filename):
##    #create a space in memory for program to output to
##    file_content = []
##    #open file
##    file_reader = open(filename, "r")
##    #load content
##    loaded_content = file_reader.read()
##    #print(type(loaded_content))
##    def load_file(filename):
##    #create a space in memory for program to output to
##    file_content = []
##    #open file
##    file_reader = open(filename, "r")
##    #load content
##    loaded_content = file_reader.read()
##    #print(type(loaded_content))
##    #append content to list
##    try:
##    if (int(loaded_content)):
##    file_content = (int(loaded_content))
##    elif (float(loaded_content)):
##    file_content = (float(loaded_content))
##    except:
##        file_content = (str(loaded_content))      
##    #close and return
##    file_reader.close()
##    return file_content#append content to list
##    try:
##    if (int(loaded_content)):
##    file_content = (int(loaded_content))
##    elif (float(loaded_content)):
##    file_content = (float(loaded_content))
##
##    except:
##        file_content = (str(loaded_content)) 
##              
##    #close and return
##    file_reader.close()
##    return file_content

