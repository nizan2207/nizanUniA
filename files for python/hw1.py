# *************** HOMEWORK 1 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def question1(a, b, c):
    if (b**2 - 4*a*c) > 0: # Checks whether the equation is greater than zero and if it prints 2
        print(2)
    elif (b**2 - 4*a*c) == 0: # Checks whether the equation equals zero and if it prints 1
        print(1)
    else: # If both came out wrong there are no solutions and so it will print 0
        print(0)

# **************************************************************
# ************************ QUESTION 2 **************************
def question2(date):
    day = date % 100 # A variable that saves the day
    month = (int(date / 100)) % 100 # A variable that saves the month
    year = int(date / 10000) # A variable that saves the year
    if year > 2020: # If the year is greater than two thousand twenty wrong prints if the year is closed continues
        print("invalid")
    elif (month <= 12) and (month > 0): # Checking for a month's health
        if month == 2: # Checking if the month is February
            if year % 4 == 0: # Checking if this year is leapfrogged
                if (day < 0) or (day > 29): # Daytime for a year is passed for February
                    print("invalid")
                else:
                    print("valid")
            else:
                if (day < 0) or (day > 28): # validate for a not leapyear
                    print("invalid")
                else:
                    print("valid")
        elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month ==8) or (month == 10) or (month == 12):
            if (day < 0) or (day > 31): # validate for 31 days month's
                print("invalid")
            else:
                print("valid")
        else:
            if (day < 0) or (day > 30): # validate for 30 days month's
                print("invalid")
            else:
                print("valid")

# **************************************************************
# ************************ QUESTION 3 **************************
def question3(s):
    temp = "" # save the last list
    for i in range(len(s)): # loop the check the value and add the not digits to the list temp
        if not s[i].isdigit():
            temp += "" + s[i]
        else:
            break
    print(temp)  # print temp


# **************************************************************
# ************************ QUESTION 4 **************************
def question4(input_list):
    index_out = 0 # save the index that got us out of the loop
    Sum = 0 # variebale of the sum
    for i in range(len(input_list)-1):
        if input_list[i] >= input_list[i+1]: # check if the sidra is going down
            if input_list[i] % 3 == 0: # if the number dived by 3 without sheerit and if it is ass it to the sum
                Sum += input_list[i]
        else:
            index_out = i+1 # if we got out the loop it means the sidra is not going down so we are saving the index of the number that got us out of the loop
            Sum = 0 # reset the sum coz it is not a going sown sidra
            break
    if index_out != 0: # loop to calculate the sidra if it not going down until the number that got us ou og the loop without him
        for i in range(index_out):
            Sum += input_list[i]
    elif input_list[len(input_list)-1] % 3 == 0: # add the last number of the sidra if it divided by 3 with no sheerit
        Sum += input_list[len(input_list)-1]
    print(Sum)
    
question2(19911302)
