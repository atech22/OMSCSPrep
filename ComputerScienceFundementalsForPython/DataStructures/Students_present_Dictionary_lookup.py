#Write a function called students_present. students_present
#should take as input one parameter, a dictionary. The keys
#of the dictionary will be names, and the values will be one
#of three strings: "Here", "Present", or an empty string "".
#
#Return a list of the keys for whom the corresponding value
#is either "Here" or "Present".


#Add your code here!
def students_present(input_student_list):
    attendence_list = []
    for student in input_student_list.items():
        if student[1] == "Here" or student[1] == "Present":
            attendence_list.append(student[0])
    return attendence_list

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#["David", "Marguerite", "Joshua", "Erica"]

student_list = {"David" : "Here", "Marguerite" : "Here",
                "Jackie": "", "Joshua": "Present",
                "Erica": "Here", "Daniel": ""}
print(students_present(student_list))



