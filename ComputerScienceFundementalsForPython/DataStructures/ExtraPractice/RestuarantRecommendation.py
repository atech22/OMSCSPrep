#Imagine you are trying to choose what restaurant to visit.
#You have a list of restaurants, each with a collection of
#star ratings. You also have a minimum standard; you will
#only go to a restaurant whose star rating is at least your
#minimum standard.
#
#Write a function called restaurant_rating. restaurant_rating
#has two parameters. The first is a dictionary, where the keys
#are restaurant names and the values are lists of ratings. The
#second parameter is your minimum rating. If a restaurant's
#average rating is above your minimum rating, you might visit
#it. If it is not, you won't.
#
#restaurant_rating should return a list of restaurants eligible
#for you to visit. That is, it should return a list of
#restaurant names from the dictionary whose average ratings
#(the average of the ratings in their lists) is greater than or
#equal to your minimum rating.
#
#For example:
#rest_and_rating = {'burger king':[4,5,3,4,3], 'moes':[4,5,5,5,5], 'taco bell':[1,2,3,4,5]}
#value = 4.5
#restaurant_rating(rest_and_rating, value) -> ['moes']


#Write your code here!
def restaurant_rating(restaurant_dict, min_rating):
    eligible_restaurants = []
    for restaurant in restaurant_dict.items():
        name, ratings = restaurant
        average_rating = (sum(ratings) / len(ratings))
        print(average_rating)
        if average_rating >= min_rating:
            eligible_restaurants.append(name)
    eligible_restaurants = sorted(eligible_restaurants)
    return(eligible_restaurants)
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: ['moes']
rest_and_rating = {'burger king':[4,5,3,4,3], 'moes':[4,5,5,5,5], 'taco bell':[1,2,3,4,5]}
value = 4.5
print(restaurant_rating(rest_and_rating, value))

