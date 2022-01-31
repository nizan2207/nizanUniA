import math
"""
flatten function is getting a rec_list that is a recursive list
the function return a list that is only numbers
"""


def flatten(rec_list):
    if rec_list == []:  # the stop condition
        return rec_list
    if isinstance(rec_list[0], list):  # if the item is a list
        return flatten(rec_list[0]) + flatten(rec_list[1:])  # recursive call for the items
    return rec_list[:1] + flatten(rec_list[1:])

"""
the function gets a list and return if the can be divoded to 2  diffrent lists that are equal to one onther 
"""
def partition(lst):
    return partitionHelper(lst, 0, 0)
"""
this function helps the partition function to run every senario there is of possible adding of numbers in the list to 2 diffrent lists and to see if they are equal to onr onther
"""
def partitionHelper(lst, sumN1, sumN2):
    if len(lst) == 0:#the stop condition
        return sumN1 == sumN2
    op1 = partitionHelper(lst[:len(lst) - 1], sumN1 + lst[len(lst) - 1], sumN2) #starting to check the senarios on sum number 1
    op2 = partitionHelper(lst[:len(lst) - 1], sumN1, sumN2 + lst[len(lst) - 1])# starting to check the senarios in sum number 2
    return op1 or op2
"""
the function gets a matrix and 2 sets of indexes and the function return if we can swap them by the terms we disdied that if they are nabors and the secound one is much bogger than the first one 
"""


def is_valid_move(matrix, i1, j1, i2, j2):
    if j1 == j2 and i1 == i2 + 1 and matrix[i2][j2] > matrix[i1][
        j1]:  # check if naboor and if the secound value is bogger than the first
        return True
    if j1 == j2 and i1 == i2 - 1 and matrix[i2][j2] > matrix[i1][
        j1]:  # check if naboor and if the secound value is bogger than the first
        return True
    if j1 == j2 - 1 and i1 == i2 and matrix[i2][j2] > matrix[i1][
        j1]:  # check if naboor and if the secound value is bogger than the first
        return True
    if j1 == j2 + 1 and i1 == i2 and matrix[i2][j2] > matrix[i1][
        j1]:  # check if naboor and if the secound value is bogger than the first
        return True
    return False

"""
the function gets a mtrix and set of indexes 
and return the count recurivly the number of pathes between the 0,0 to thei j
"""
def num_paths(matrix, i2, j2):
    return num_path_healper(matrix, 0, 0, i2, j2, 0)

"""
the function gets a mtrix and 2 sets if indexes and the sum of the path 
and return the number of pathes between the i1 j1 to the i2 j2
"""
def num_path_healper(matrix, i1, j1, i2, j2, Sum):
    if i1 == i2 and j1 == j2:# the stop condition 
        Sum += 1
        return (Sum)
    if is_right(matrix, i1, j1, i1, j1 + 1): # the opstions after right
        Sum = num_path_healper(matrix, i1, j1 + 1, i2, j2, Sum)
    if is_left(matrix, i1, j1, i1, j1 - 1): # the options after left
        Sum = num_path_healper(matrix, i1, j1 - 1, i2, j2, Sum)
    if is_up(matrix, i1, j1, i1 - 1, j1):# the options after up
        Sum = num_path_healper(matrix, i1 - 1, j1, i2, j2, Sum)
    if is_down(matrix, i1, j1, i1 + 1, j1): # the options after down
        Sum = num_path_healper(matrix, i1 + 1, j1, i2, j2, Sum)
    return Sum


"""
the function gets a mtrix and 2 sets of indexes and return if moving right in the matrix is valid
"""


def is_right(matrix, i1, j1, i2, j2):
    if 0 <= j2 < len(matrix[0]) and 0 <= i2 < len(matrix) and 0 <= j1 < len(matrix[0]) and 0 <= i1 < len(matrix):
        return is_valid_move(matrix, i1, j1, i2, j2)
    return False


"""
the function gets a mtrix and 2 sets of indexes and return if moving left in the matrix is valid
"""


def is_left(matrix, i1, j1, i2, j2):
    if 0 <= j2 < len(matrix[0]) and 0 <= i2 < len(matrix) and 0 <= j1 < len(matrix[0]) and 0 <= i1 < len(matrix):
        return is_valid_move(matrix, i1, j1, i2, j2)
    return False


"""
the function gets a mtrix and 2 sets of indexes and return if moving up in the matrix is valid
"""


def is_up(matrix, i1, j1, i2, j2):
    if 0 <= j2 < len(matrix[0]) and 0 <= i2 < len(matrix) and 0 <= j1 < len(matrix[0]) and 0 <= i1 < len(matrix):
        return is_valid_move(matrix, i1, j1, i2, j2)
    return False


"""
the function gets a mtrix and 2 sets of indexes and return if moving down in the matrix is valid
"""


def is_down(matrix, i1, j1, i2, j2):
    if 0 <= j2 < len(matrix[0]) and 0 <= i2 < len(matrix) and 0 <= j1 < len(matrix[0]) and 0 <= i1 < len(matrix):
        return is_valid_move(matrix, i1, j1, i2, j2)
    return False

"""
the function gets a number of the floor we want to get to,
a list of the prices of the floors and the steps we can do
the function return the minimal cost of the climbing
"""
def minimal_cost_path(n, taxes, steps_options):
    if n in steps_options:
        return taxes[steps_options.index(n)]
    return minimal_cost_path_helper(n,taxes,steps_options,0,sum(taxes))-1

"""
the function gets a number of the floor we want to get to,
a list of the prices of the floors and the steps we can do
the function return the minimal cost of the climbing and the adding and a number that the first adding cant be higher than him 
the function return the minimal cost of the climbing
"""
def minimal_cost_path_helper(n,taxes,steps_options,lastAdding,x):
    if n == 0: # stop conition
        return lastAdding + taxes[0]
    if n < 0: # to prevent it from going to an minos
        return 0
    for i in steps_options:
        lastAdding = taxes[n] + minimal_cost_path_helper(n-i,taxes,steps_options,lastAdding,x)
        if lastAdding < x:
            x = lastAdding
    return x

"""
the function gets a number of the floor we want to get to,
a list of the prices of the floors and the steps we can do
the function return the minimal cost of the climbing only fatser
"""
def minimal_cost_path_faster(n, taxes, steps_options):
    if n in steps_options:
        return taxes[steps_options.index(n)]
    return minimal_cost_path_helper_secound(n,taxes,steps_options,0,math.inf,{})

"""
the function gets a number of the floor we want to get to,
a list of the prices of the floors and the steps we can do
the function return the minimal cost of the climbing and the adding and a number that the first adding cant be higher than him and a dict
the function return the minimal cost of the climbing only faster
"""
def minimal_cost_path_helper_secound(n,taxes,steps_options,lastAdding,x,Dict):
    if n == 0: # stop conition
        return lastAdding + taxes[0]
    if n < 0: # to prevent it from going to an minos
        return 0
    for i in steps_options:
        lastAdding = taxes[n] + minimal_cost_path_helper(n-i,taxes,steps_options,lastAdding,x)
        if lastAdding < x:
            x = lastAdding
    return x
    
