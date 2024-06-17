#The function below adds up all the numbers in a list. However, it does so in a strange way: it changes the sign of each number, but then subtracts the number instead of adding it.

def add(numbers):
    sum = 0
    print(numbers)
    for i in range(len(numbers)):
        #Line 8 changes the actual values of the list. So, when we run the function again, the values of the list have changed, and the output is different!
        numbers[i] = -numbers[i]
        #print(numbers[i])
        sum -= numbers[i]
        print(sum)
    return sum

my_list = [2, 4, 6, 8, 10]
print(add(my_list))
print(add(my_list))


## Example 2 - in this example, the list is not changed, but the values of the list are changed. so both print statements return the same value
def add(numbers):
    sum = 0
    for number in numbers:
        number = -number
        sum -= number
    return sum

my_list = [2, 4, 6, 8, 10]
print(add(my_list))
print(add(my_list))