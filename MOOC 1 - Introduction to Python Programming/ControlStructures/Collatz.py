#The Collatz Conjecture is a famous sequence in mathematics
#proposed by Lothar Collatz. It proceeds as follows:
#
#Start with any number. If the number is even, divide it by
#2. If the number is odd, triple it and add one. Repeat.
#Eventually, no matter what number you begin with, this
#sequence will converge on 1 (and if you continue repeating
#it, you'll repeat 1-4-2 infinitely).
#
#For example, imagine we started with the number 5:
#5 is odd, so 5 * 3 + 1 = 16
#16 is even, so 16 / 2 = 8
#8 is even, so 8 / 2 = 4
#4 is even, so 4 / 2 = 2
#2 is even, so 2 / 1 = 1
#
#Starting with 5, this sequence converges on 1 in 5
#iterations: 5 to 16, 16 to 8, 8 to 4, 4 to 2, and 2 to 1.
#
#Implement a function called collatz. collatz should take
#as input an integer, and return the number of iterations
#it takes for the Collatz sequence to reach 1 from that
#number. For example, collatz(5) would return 5 because
#it took 5 iterations to converge on 1.


#Add your code here!
def collatz(input_number):
    iteration = 0
    while input_number > 1:
        if input_number % 2 == 0:
            input_number = (input_number / 2)
            iteration += 1
        elif input_number % 2 != 0:
            input_number = ((input_number * 3) + 1)
            iteration += 1
        #return input_number
    return iteration
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5, 17, and 23, each on their own lines.
print(collatz(5))
print(collatz(15))
print(collatz(25))




