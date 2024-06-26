#Write a function called get_capitals. get_capitals should
#accept one parameter, a string. It should return a string
#containing only the capital letters from the original
#string: no lower-case letters, numbers, punctuation marks,
#or spaces.
#
#Remember, capital letters have ordinal numbers between 65
#("A") and 90 ("Z"). You may use the ord() function to get
#a letter's ordinal number.
#
#Your function should be able to handle strings with no
#capitals (return an empty string) and strings with all
#capitals (return the original string). You may assume
#we'll only use regular characters (no emojis, formatting
#characters, etc.).


#Write your function here!
def get_capitals(a_string):
    try:
        return_string = ""
        for c in a_string:
            if ord(c) >= 65 and ord(c) <= 90:
                return_string += c
        return(return_string)
    except Exception as error:
        return error
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#CS
#GIT
print(get_capitals("CS1301"))
print(get_capitals("Georgia Institute of Technology"))
#print(get_capitals("test"))
#print(get_capitals(55))





