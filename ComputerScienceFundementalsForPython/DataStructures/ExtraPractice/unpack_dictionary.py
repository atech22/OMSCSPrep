#Write a function called volume_and_area. volume_and_area
#will take in a dictionary. This dictionary is guaranteed to
#have three keys: "length", "width", and "height", whose
#values are integers representing three attributes of a
#rectangular prism (also known as a box).
#
#Modify this dictionary to add two keys: "volume" and "area".
#The values associated with these keys should be the volume
#and surface area of the box.
#
#The formula for volume is:
#  length * width * height
#
#The formula for surface area is:
#  2 * ((length * width) + (length*height) + (width*height))
#
#Because length, width, and height are integers, and because
#these formulas have no division, your results should be
#integers as well.


#Add your code here!
def volume_and_area(input_measurements):
    length, width, height = input_measurements
    my_dict = {}
    my_dict["length"] = input_measurements[length]
    my_dict["width"] = input_measurements[width]
    my_dict["height"] = input_measurements[height]
    my_dict["volume"] = input_measurements[length] * input_measurements[width] * input_measurements[height]
    #print(my_dict["volume"])
    my_dict["area"] = (2 * ((input_measurements[length] * input_measurements[width]) + (input_measurements[length] * input_measurements[height]) + (input_measurements[width] * input_measurements[height])))
    #print(my_dict)
    return my_dict
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 6 and 22, each on a different line.
rectangle = {"length": 1, "width": 2, "height": 3}
volume_and_area(rectangle)
rectangle = volume_and_area(rectangle)
print(rectangle["volume"])
print(rectangle["area"])





