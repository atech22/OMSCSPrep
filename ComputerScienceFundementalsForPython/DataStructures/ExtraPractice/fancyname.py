#It's a well-known and indisputable fact that if you want
#to make your name sound fancy, you should list it as only
#your first two initials followed by your last name. For
#example, my full name is David Andrew Joyner, and therefore
#my fancy name is D. A. Joyner. (If you have two middle names,
#it's even better, but we'll assume we have only one -- we're
#C. S. Lewis, not J. R. R. Tolkien).
#
#Write a function called fancy_me. fancy_me should take as
#input a list of strings, each representing a full name (e.g.
#"David Andrew Joyner" or "First Middle Last". fancy_me should
#return a single string, formatting that list of names in this
#fancy style, like this:
#
#  F. M. Last, D. A. Joyner, G. P. Burdell
#
#Each individual name is the first initial, then a period, then
#a space, then the second initial, then a period, then a space,
#then the last name, then a comma. There is no comma after the
#last name in the list.
#
#For example:
#
#  fancy_me(["First Middle Last", "David Andrew Joyner", "George P Burdell"])
#
#...would return "F. M. Last, D. A. Joyner, G. P. Burdell"


#Write your function below!
def fancy_me(list_of_names):
    result = ""
    for name in list_of_names:
        name = name.split(" ")
        f = name[0][0] + ". "
        m = name[1][0] + ". "
        fancyname = f + m + name[2] + ", "
        result += fancyname
    result = result.rstrip(", ")
    return(result)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: F. M. Last, D. A. Joyner, G. P. Burdell
print(fancy_me(["First Middle Last", "David Andrew Joyner", "George P Burdell"]))


