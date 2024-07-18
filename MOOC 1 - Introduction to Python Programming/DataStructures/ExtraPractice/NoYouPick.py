#-----------------------------------------------------------
#Write a function called no_you_pick. no_you_pick should
#have two parameters. The first parameter is a dictionary
#where the keys are restaurant names and the values are lists
#of attributes of those restaurants as strings, such as
#"vegetarian", "vegan", and "gluten-free".
#
#The second parameter is a list of strings representing of
#necessary attributes of the restaurant you select.
#
#Return a list of restaurants from the dictionary who each
#contain all the diet restrictions listed in the list,
#sorted alphabetically. If there are no restaurants that
#meet all the restrictions, return the string "Sorry, no
#restaurants meet your restrictions". Types of diet
#restrictions that exist in this question's universe are:
#vegetarian, vegan, kosher, gluten-free, dairy-free
#
#For example:
#grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
#                 "jacob's pickles": ["vegetarian", "gluten-free"], \
#                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher"]}
#guests_diet = ["dairy-free"]
#no_you_pick(grading_scale, guests_diet) -> ["blossom"]


#Write your code here!
def no_you_pick(grading_scale, guests_diet):
    matching_restaurants = []
    for restaurant, diets in grading_scale.items():
        is_match = True
        for diet in guests_diet:
            if diet not in diets:
                is_match = False
                break
        if is_match:
            matching_restaurants.append(restaurant)
    if not matching_restaurants:
        return "Sorry, no restaurants meet your restrictions"
    else:
        return sorted(matching_restaurants)

#### My failed first attempt:
#    def no_you_pick(restaurant_dict, guests_diet):
#    eligible_restaurants = []
#    for restaurant in restaurant_dict.items():
#        name, attributes = restaurant
#        print(attributes)
#        for category in guests_diet:
#            print(category)
#            if category in attributes:               
#                pass
#            else:
#                return "Sorry, no restaurants meet your restrictions"
#    eligible_restaurants.append(name)
#    print(eligible_restaurants)   
#   if eligible_restaurants == []:


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: blossom
grading_scale = {"blossom": ["vegetarian", "vegan", "kosher", "gluten-free", "dairy-free"], \
                 "jacob's pickles": ["vegetarian", "gluten-free"], \
                 "sweetgreen": ["vegetarian", "vegan", "gluten-free", "kosher"]}
guests_diet = ["dairy-free"]
print(no_you_pick(grading_scale, guests_diet))




