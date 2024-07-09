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
    
    for problem in problem_list:

        if "+" in problem:
            num1,num2=problem.split("+")
            operator='+'
        elif '-' in problem:
            num1,num2=problem.split("-")
            operator="-"
        elif "*" in problem:
            num1,num2=problem.split("*")
            operator="*"
        elif "/" in problem:
            num1,num2=problem.split("/")
            operator="/"
        else:
            print("Operator is not Valid")

        #push num1 in first row
        width=max(len(num1),len(num2))+2
        top_row.append(num1.rjust(width))
        bottom_row.append(operator+num2.rjust(width-1))
        dash_row.append("-"*width)

        #Calculating result
        if show_result:
            if operator=='+':
                result=str(int(num1)+int(num2))
            elif operator=='-':
                result=str(int(num1)-int(num2))
            elif operator=='*':
                result=str(int(num1)*int(num2))
            elif operator=='/':
                result=str(float(num1)/float(num2))
            else:
                print("Error:Invalid Operator")
            
            result_row.append(result.rjust(width))
        

        

    #Formating Part
    formated_row=["    ".join(top_row),"    ".join(bottom_row),"    ".join(dash_row)]
    if show_result:
        formated_row.append("    ".join(result_row))

    return "\n".join(formated_row)



def main():
    problem_list=get_problem()
    print("Formated Output!")
    print("----------------")
    print(arithematic_formater(problem_list,True))


if __name__=="__main__":
    main()