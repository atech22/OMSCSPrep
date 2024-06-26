#Write a function called "find_coffee" that expects a 
#filename as a parameter. The function should open the 
#given file and return True if the file contains the word 
#"coffee". Otherwise, the function should return False.
#
#Hint: look up the read() method if you want to do this
#more simply than you might do with readline().


#Write your function here!
def find_coffee(file_name):
    #open the file
    filereader = open(file_name, "r")
    #read from the file
    filecontents = (filereader.read())
    coffee = "coffee" in filecontents
    
    #close the file
    filereader.close()
    #return the boolean expresssion if "coffee" is in the file
    return coffee

    

#You can test your function with the provided files named 
#"coffeeful.txt" and "coffeeless.txt". With their original
#text, the lines below should print True, then False. You
#may also edit the files by selecting them in the drop
#down in the top left to try your code with different
#input.
print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))




