# Arithematic Formater
import re

#Getting Problems from the user
def get_problem():
    problem_list = []
    while True:
        problem = input("Enter a problem(number operator number),'q' to stop:")
        if problem.lower() == 'q':
            break
        if re.search(r"^\d+\s*[+\-\*\/]\s*\d+$", problem):
            problem_list.append(problem)
        else:
            print("Error:Invalid Format(number(space)operator(space)number)")
            continue
    return problem_list

#Formating the Inputs and outputs
def arithematic_formater(problem_list,show_result=False):
    top_row=[]
    bottom_row=[]
    dash_row=[]
    result_row=[]
    formated_row=[]
    pass
