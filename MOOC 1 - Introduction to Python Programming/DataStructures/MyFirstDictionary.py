ta_info = [("Joshua", "Georgia"),
          ("Jackie", "Vermont"),
          ("Marguerite", "Tennessee")]

#The problem said you could either create the dictionary
#from scratch, create it based on ta_info, or create it
#dynamically. Let's look at all three!
#
#Here's creating it from scratch:

ta_dict = {"Joshua":"Georgia", "Jackie":"Vermont", "Marguerite":"Tennessee"}

#To create it from ta_info, we'd just replace the string
#literals in the dictionary definition with the list
#and tuple indices:

ta_dict = {ta_info[0][0]:ta_info[0][1], ta_info[1][0]:ta_info[1][1], ta_info[2][0]:ta_info[2][1]}

#To create it dynamically, we would look over all the keys
#and add the new key-value pair to the dictionary:

ta_dict = {}
for ta_tuple in ta_info:
    ta_dict[ta_tuple[0]] = ta_tuple[1]

#Any of these three approaches would crate ta_dict with the
#right values. The first method only works with these three
#names and states, the second method works with any values of
#ta_info as long as there are exactly three, and the third
#works for any values of ta_info no matter how many names.
#   
#
#Now, we just need to pull the data back out of the dictionary:

josh_val = ta_dict['Joshua']
jack_val = ta_dict["Jackie"]
marg_val = ta_dict["Marguerite"]

#And print it:

print(josh_val)
print(jack_val)
print(marg_val)






