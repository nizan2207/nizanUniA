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
    if len(lst) == 0:  # the stop condition
        return sumN1 == sumN2
    op1 = partitionHelper(lst[:len(lst) - 1], sumN1 + lst[len(lst) - 1],
                          sumN2)  # starting to check the senarios on sum number 1
    op2 = partitionHelper(lst[:len(lst) - 1], sumN1,
                          sumN2 + lst[len(lst) - 1])  # starting to check the senarios in sum number 2
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


def num_paths(matrix, i2, j2):
    return num_path_healper(matrix, 0, 0, i2, j2, 0)


def num_path_healper(matrix, i1, j1, i2, j2, Sum):
    if i1 == i2 and j1 == j2:
        Sum += 1
        return (Sum)
    if is_right(matrix, i1, j1, i1, j1 + 1):
        Sum = num_path_healper(matrix, i1, j1 + 1, i2, j2, Sum)
    if is_left(matrix, i1, j1, i1, j1 - 1):
        Sum = num_path_healper(matrix, i1, j1 - 1, i2, j2, Sum)
    if is_up(matrix, i1, j1, i1 - 1, j1):
        Sum = num_path_healper(matrix, i1 - 1, j1, i2, j2, Sum)
    if is_down(matrix, i1, j1, i1 + 1, j1):
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


def minimal_cost_path(n, taxes, steps_options):
    print('************ TO DO: Question 4A')  # DELETE BEFORE SUBMISSION
    ### WRITE CODE HERE


def minimal_cost_path_faster(n, taxes, steps_options):
    print('************ TO DO: Question 4B')  # DELETE BEFORE SUBMISSION
    ### WRITE CODE HERE


m = [[1, 2, 7, 8], [3, 5, 6, 9], [6, 7, 10, 23]]
print(num_paths(m, 2, 2))
