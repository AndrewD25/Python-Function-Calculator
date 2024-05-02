'''
Andrew Deal
Ultimate Function Calculator
'''


## To-Add in Future ##
# - Work for functions with uneven x spacing? Ex: (1, 5), (2, 7), (9, 9)
# - Calculate function equation
# - If not a calc-able equation: Linreg, quadreg, etc for the function?
# - Calculate interecepts?
# - Work for equations instead of a table of values? Or is this going too deep lol


## Imports ##
from pprint import pprint 


## Variables ##

y = []


## Functions ##


def get_counter(integer):
    if integer == 1:
        return "st"
    elif integer == 2:
        return "nd"
    elif integer == 3:
        return "rd"
    else:
        return "th"


def get_degree_counter(integer):
    if integer == 1:
        return "linear"
    elif integer == 2:
        return "quadratic"
    elif integer == 3:
        return "cubic"
    elif integer == 4:
        return "quartic"
    elif integer == 5:
        return "quintic"
    else:
        return str(integer) + "th degree"
    

def get_number_input(question, outlier):
    #Question is the input number to be asked
    #Outlier is an exception string that is also a valid input and is returned on this case

    answer = input(question)

    while True:
        
        if answer.lower() == outlier.lower():
            return outlier
    
        try:
            answer = float(answer)
            return answer
        except:
            print("Value error. " + question)
            answer = input(question)


def get_differences():

    #Setup
    differences = [
        y
    ]

    #Logic
    for i in range(1, len(y)):
        
        differences.append([])

        previous_list = differences[i - 1]

        for k in range(len(previous_list) - 1):
            differences[i].append(previous_list[k + 1] - previous_list[k])

        #Output
        print("The %d%s differences of this function in order are..." % (i, get_counter(i)))
        pprint(differences[i])

    return differences


def contains_other_than(value, lst):
    for item in lst:
        if item != value:
            return True
    return False


def contains_same_values(lst):
    value = lst[0]
    for item in lst:
        if item != value:
            return False
    return True        


def get_degree(diff):
    
    highest_index = 0

    #Find Highest List That != 0s
    for i in range(1, len(diff)):
        if contains_other_than(0, diff[i]):
            highest_index = i

    #Check if that list is all the same
    if contains_same_values(diff[highest_index]) and len(diff[highest_index]) > 1:
        return highest_index
    #Otherwise it is not determinable by the given data
    else:
        return None
    
    

## Runtime ##

#Create a list of the y values of each ordered pair
get_y = get_number_input("Enter a y-value or type 'End' to finish: ", "End")

while get_y != "End":
    y.append(get_y)
    get_y = get_number_input("Enter a y-value or type 'End' to finish: ", "End")

print() #Create a newline for readability

#Get the list of all calculable differences from the set of numbers
diff_list = get_differences()

print() #Create a newline for readability

#Display the degree of the function
degree = get_degree(diff_list)
if degree == None:
    print("The degree cannot be determined confidently from the given information.")
else:
    print("The data provided appears to be from a %s function" % (get_degree_counter(degree)))

## Keep Window Open For Console ##
input()
