#Imagine you're writing a cash register application. To make
#interaction easier on the user, it doesn't have separate
#areas for passwords, PIN numbers, or cash totals --
#instead, it looks at what the cashier enters and infers
#whether it's their PIN number, their password, or the cash
#total for a transaction.
#
#The register makes this decision with the following rules:
#
# - If the cashier entered only digits, then it's a PIN
#   number.
# - If the cashier entered a decimal number, then it's the
#   transaction amount.
# - If the cashier entered anything else, then it's their
#   password.
#
#Write a function named interpretCashier. interpretCashier
#should take one parameter as input, which will always be
#a string initially.
#
# - If the string entered represents a PIN number, return
#   "PIN". 
# - If the string entered represents a transaction amount,
#   return "Transaction".
# - If the string entered represents a password, return
#   "Password".
#
#Hint: There is a very easy way to do this, and a very hard
#way to do this. Remember, this test is on control
#structures, not strings.


#Write your function here!
def interpretCashier(cashier_input):
    try:
        interpretation = (int(cashier_input))
        if type(interpretation) == int:
            return "PIN"
    except:
        pass
    try:
        interpretation = (float(cashier_input))
        if type(interpretation) == float:
            return "Transaction"
    except:
        pass
    try:
        interpretation = (str(cashier_input))
        if type(interpretation) == str:
            return "Password"
    except:
        pass
        
#The lines of code below will test your function. It is not
#used for grading, so feel free to change it. As written,
#these lines should print Transaction, PIN, and Password,
#each on a separate line.
print(interpretCashier("24.59"))
print(interpretCashier("123456"))
print(interpretCashier("my$up3rs3cur3p4$$w0rd"))


