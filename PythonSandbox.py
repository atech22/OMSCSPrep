def find_the_evens(a_list):
    list_of_evens = []
    for i in range(len(a_list)):
        if i % 2 == 0:
            list_of_evens.append(a_list[i])
    return list_of_evens
my_list = [1, 5, 4, 4, 2, 1, 5, 9]
find_the_evens(my_list)
print(my_list)