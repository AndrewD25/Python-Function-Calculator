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
import re
import math


## Variables ##

x = []
y = []


## Functions ##

def ordered_pair_to_dict(op):

    #Input validation in separate function
    
    #Formatting logic
    space_removed = op.replace(" ", "")
    parentheses_removed = space_removed.replace("(", "").replace(")", "")
    op_dict = parentheses_removed.split(",")

    return {"x": float(op_dict[0]), "y": float(op_dict[1])}


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


def is_a_function(x, y):
    # Function to check if a list contains duplicates
    def contains_duplicates(lst):
        seen = set()
        for item in lst:
            if item in seen:
                return True
            seen.add(item)
        return False

    # Check if x contains duplicates
    if contains_duplicates(x):
        # Create a dictionary to store y values for each x
        x_y_map = {}
        for i in range(len(x)):
            if x[i] in x_y_map:
                # Check if the y value matches the previously stored y value
                if y[i] != x_y_map[x[i]]:
                    return False
            else:
                x_y_map[x[i]] = y[i]
    return True      


def check_x_spacing():

    differences = []
    
    #Logic
    for i in range(0, len(x)):
        if i + 1 < len(x):
            differences.append(x[i+1] - x[i])

    return contains_same_values(differences)
        

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


def get_ordered_pair_input(question, outlier):
    #Question is the input number to be asked
    #Outlier is an exception string that is also a valid input and is returned on this case

    answer = input(question)

    while True:
        
        #Exit if outlier is entered
        if answer.lower() == outlier.lower():
            return outlier

        #Check for valid input
        has_comma = answer.count(",") == 1
        correct_length = len(answer.split(",")) == 2
        no_other_symbols = bool(re.match(r'^[0-9(),.-]+$', answer))

        if has_comma and correct_length and no_other_symbols:
            return ordered_pair_to_dict(answer)

        print("The input given does not appear to be in ordered pair format")
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
            diff = previous_list[k + 1] - previous_list[k]
            sigfigs = "." + str(len(str(int(diff))) + 3) + "g"
            differences[i].append(float(format(diff, sigfigs)))

        #Output
        print("The %d%s differences of this function in order are..." % (i, get_counter(i)))
        pprint(differences[i])

    return differences     


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


def get_equation(degree, differences):

    if degree == 1:
        #Linear function in slope intercept form
        slope = differences[1][0]
        y_int = slope * -1 * x[0] + y[0]
        return "f(x) = " + str(slope) + "x + " + str(y_int)

    elif degree == 2:

        return None
    
        '''
        #Quadratic function in standard form
        a = float(differences[2][0]) / 2
        #b = differences[1][0] #B was broken :(
        x1 = x[0]
        y1 = y[0]
        c = -1 * a * math.pow(x1, 2) - b * x1 + y1
        
        return "f(x) = " + str(a) + "x² + " + str(b) + "x + " + str(c)
        '''

    else:
        #No equation handling yet
        return None

    

## Runtime ##

#Create a list of the y values of each ordered pair
get_op = get_ordered_pair_input("Enter an ordered pair or type 'End' to finish: ", "End")

while get_op != "End":
    x.append(get_op["x"])
    y.append(get_op["y"])
    get_op = get_ordered_pair_input("Enter an ordered pair or type 'End' to finish: ", "End")

print() #Create a newline for readability

#Check if the table creates a function
if not is_a_function(x, y) or not len(x) > 1:
    print("I'm sorry, this data does not appear to be a function")
    input()
    exit()
elif contains_same_values(x):
    print("This data appears to be from a function but you entered the same point multiple times.")
    print("Please remove duplicate entries and try again")
    input()
    exit()
    
#Check if x values are evenly spaced
if not check_x_spacing():
    print("I'm sorry, your x values are not at even differences and this program currently does not support this type of data.")
    input()
    exit()

#Get the list of all calculable differences from the set of numbers
diff_list = get_differences()

print() #Create a newline for readability

#Display the degree of the function
degree = get_degree(diff_list)
if degree == None:
    print("The degree cannot be determined confidently from the given information.")
else:
    print("The data provided appears to be from a %s function" % (get_degree_counter(degree)))

    print() #Create a newline for readability

    #If I know how to, get function equation
    equation = get_equation(degree, diff_list)
    if equation == None:
        print("I'm sorry, I don't know how to make an equation for that degree of function yet")
    else:
        print("The function's equation appears to be: " + equation)

## Keep Window Open For Console ##
input()
