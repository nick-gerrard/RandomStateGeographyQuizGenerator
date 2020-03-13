#! usr/bin/python3

#Random Quiz Generator - creates random quizzes.
#random order of questions, plus answer key

import random
from Capitals import capitals

#Setting up the generator for the quizzes:

for quizNum in range(35):
    #Generating the names for the Quiz/Answer Files:

    quiz_name = "Quiz" + str(quizNum) + ".txt"
    answer_name = "Answer"+str(quizNum) + ".txt"

    #Opening/Generating Quiz and answer files

    with open(quiz_name, "w") as quiz_file, open(answer_name, "w") as answer_file:
        
        #Building the Quiz/Answer Key headers:

        quiz_file.write(quiz_name +"\n\n\n")
        quiz_file.write("Geography Quiz\n\n")

        answer_file.write(answer_name + "\n\n\n")
        answer_file.write("Answer Key\n\n")
        
        #Creating the question order and randomizing it

        quiz_order = [key for key in capitals]
        random.shuffle(quiz_order)
        answer_list = [capitals[key] for key in capitals]
        
        #Writing the values to files:

        question_num = 1
        
        for value in quiz_order:
            line_to_write = str(question_num) + ". What is the capital of " + value + "?\n\n"
            quiz_file.write(line_to_write)
            potential_answers = [capitals[value]]
            while len(potential_answers) < 4:
                random_index = random.randint(0, 49)
                if answer_list[random_index] not in potential_answers:
                    potential_answers.append(answer_list[random_index])

            random.shuffle(potential_answers)
            potential_letters = ['A', 'B', 'C', 'D']
            answer_index = 3 - potential_answers.index(capitals[value])
            for letter in potential_letters:
                new_line_to_write = letter + ". " + potential_answers.pop() + ".\n"
                quiz_file.write(new_line_to_write)
            quiz_file.write("\n")

            #Building the Answer Key

            answer = str(question_num) + ": " + potential_letters[answer_index] + " i.e. " + capitals[value] +'\n'
            answer_file.write(answer)

            question_num += 1


