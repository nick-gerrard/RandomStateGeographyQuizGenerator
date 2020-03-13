#! usr/bin/python3

from Capitals import capitals
import re
import os

#Setting up directory names

current_directory = os.getcwd()
ungraded = current_directory + "/ungraded"
graded = current_directory + "/graded"

try:
    os.makedirs(ungraded)
    print("ungraded folders created")
except:
    print("folders already exist")
try:
    os.makedirs(graded)
    print("graded folder created")
except:
    print("graded folder already exists")
#Reg Ex compilations for generating lists:

nameRegEx = re.compile(r'Name: (.*)')
stateRegEx = re.compile(r'\d+\. What is the capital of (.*)\?')
studentAnswerRegEx = re.compile(r'Enter your answer here:(.*)')
aRegEx = re.compile(r'A. (.*)\.')
bRegEx = re.compile(r'B. (.*)\.')
cRegEx = re.compile(r'C. (.*)\.') 
dRegEx = re.compile(r'D. (.*)\.') 

#Input name of file to be graded

name_of_file_to_grade = input("Enter the name of the file to be graded: ")

full_path_of_file_to_grade = ungraded + "/" + name_of_file_to_grade

with open(full_path_of_file_to_grade, "r") as ungraded_test:
    
    #Lists to be added to

    state_list = []
    student_answer_list = []
    a_list = []
    b_list = []
    c_list = []
    d_list = []

    for line in ungraded_test:
        name_re = nameRegEx.search(line)
        state_re = stateRegEx.search(line)
        student_answer_re = studentAnswerRegEx.search(line)
        a_re = aRegEx.search(line)
        b_re = bRegEx.search(line)
        c_re = cRegEx.search(line)
        d_re = dRegEx.search(line)
        if name_re:
            name = name_re.group(1)
        elif state_re:
            state = state_re.group(1)
            state_list.append(state)
        elif student_answer_re:
            studentAnswer = student_answer_re.group(1)
            student_answer_list.append(studentAnswer)
        elif a_re:
            a = a_re.group(1)
            a_list.append(a)
        elif b_re:
            b = b_re.group(1)
            b_list.append(b)
        elif c_re:
            c = c_re.group(1)
            c_list.append(c)
        elif d_re:
            d = d_re.group(1)
            d_list.append(d)


"""
print(name)
print(state_list)
print(student_answer_list)
print(a_list)
print(b_list)
print(c_list)
print(d_list)"""

#Creating a cleaned student answer list

cleaned_student_answer_list = [answer.upper().strip() for answer in student_answer_list]

#Create a name for the graded file

graded_file_name = "GradedQuizFor" + name + ".txt"
graded_file_path = graded + "/" + graded_file_name
#Create a function for returning the state from a given capital:

def get_state_from_cap(cap):
    for key in capitals:
        if cap == capitals[key]:
            return key
    return("key does not exist")
with open(graded_file_path, "w") as graded_file:
    graded_file.write(name)
    graded_file.write('\n\n\n')
    total_correct = 0
    total_incorrect = 0
    for number in range(0, 50):
        if cleaned_student_answer_list[number] == "A":
            capital_answered = a_list[number]
        elif cleaned_student_answer_list[number] == "B":
            capital_answered = b_list[number]
        elif cleaned_student_answer_list[number] == "C": 
            capital_answered = c_list[number]
        elif cleaned_student_answer_list[number] == "D":    
            capital_answered = d_list[number]
        else:
            capital_answered = "N/A"

        #Determine if student got question right

        state_answered = get_state_from_cap(capital_answered)

        if state_answered == state_list[number]:
            total_correct += 1
            line_to_print = str(number) + ". Correct\n"
        else:
            total_incorrect += 1
            line_to_print = str(number) + ". Incorrect\n"
        graded_file.write(line_to_print)

    graded_file.write("\n\n")

    total_correct_and_incorrect = "Total Correct: " + str(total_correct) + '\nTotal Incorrect: ' + str(total_incorrect) + "\n\n"

    graded_file.write(total_correct_and_incorrect)
    percentage = total_correct / 50 * 100

    if percentage > 90:
        grade = "A"
    elif percentage >80 and percentage <90:
        grade = "B"
    elif percentage >70 and percentage < 80:
        grade = "C"
    elif percentage > 60 and percentage < 70:
        grade = "D"
    else:
        grade = "F"

    percent_to_write = str(percentage) + "% right."
    grade_to_write = "Grade: " + grade

    graded_file.write(percent_to_write)
    graded_file.write("\n\n")
    graded_file.write(grade_to_write)



