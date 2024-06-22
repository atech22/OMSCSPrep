#Imagine you're writing the code for an onboard vehicle
#monitoring system. One thing the system does is measure
#tire pressure. It does this by taking a measurement every
#10 seconds. However, lots of environmental conditions can
#lead to intermittent bad readings: if it takes a reading
#as a car goes over a bump, for example, it will be way
#higher than it would have been otherwise. So, the system
#needs to know to ignore these ratings, as well as only
#process the more recent measurements. Let's tell the system
#that the only valid tire pressures are between 15 and 55.
#
#Write a function called tire_pressure. tire_pressure
#should have one parameter, a list of integers. The list
#represents a series of tire pressure measurements over the
#past several minutes.
#
#tire_pressure should return the average of the last 5
#measurements that are greater than or equal to 15 and less
#than or equal to 55. Round the result to 1 decimal place
#(you can use round(some_float, 1) to round to 1 decimal
#place).
#
#For example, if the list of measurements was this:
#
# [34, 34, 64, 34, 5, 5, 34, 34, 35, 35, 35, 65, 60, 35, 12, 35]
#
#tire_pressure would return 35.0: the last five measurements
#in range are all 35. You may assume there will be at least
#5 measurements in the proper range.


#Add your code here!
def tire_pressure(measurements):
    true_measurements = []
    for measurement in measurements:
        #print(measurement)
        if measurement >= 15 and measurement <= 55:
            true_measurements.append(measurement)
    #print(true_measurements)   
    #return the average of the last 5 measurements 
    average = (true_measurements[-5]+ true_measurements[-4] + true_measurements[-3] + true_measurements[-2] + true_measurements[-1]) / 5
    return average
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 35.0
a_list = [34, 34, 64, 34, 5, 5, 34, 34, 35, 35, 35, 65, 60, 35, 12, 35]
print(tire_pressure(a_list))






####

#Alternative Solution

####We have a count variable that tracks how many tires we added
####to our final result.
###
###def tire_pressure(list_int):
###    count = 0
###    result = 0
###
####A for loop is written with a range from the last index of
####the list of integers to the first index. We decrement so
####that we are able to get the last five digits
####We have a condition inside that for loop that checks
####if current i is within the needed range
####If so, we add the value to our result and increment count
####When count equals 5, we break out of the loop
###
###    for i in range (len(list_int) - 1, -1, -1):
###        if (15 <= list_int[i] <= 55):
###            result += list_int[i]
###            count += 1
###            if count == 5:
###                break
###
####Since our result will have the sum of 5 tires, we find
####the average by dividing by 5 and rounding to the first
####decimal, like asked.
###
###    result = round(result / 5, 1)
###    return result