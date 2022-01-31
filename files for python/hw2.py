# question 1
def triangle(perpendicular):
    last_line = ""  # save the last line
    line = ""  # save the lines
    got_in = False #if x is bogger than 9
    if perpendicular == 1:  # if it one we know to pring only it top
        print("*")
    else:
        for i in range(perpendicular - 1):  # we running on all of the lenght of the triangle chela
            if i == 0:  # if it is the first it wis the top sso we print *
                print("*")
            elif i == 1:  # of it os the secound we print the head of th triangle
                print("|\\")
            if i > 1:  # if it is not the top or the head
                for x in range(i):
                    if x == 0:
                        line += "|"
                    if x+1 == i:
                        line += "\\"
                    else:
                        temp = x
                        while((temp>9) and (i<perpendicular-1)):
                            temp-=10
                            got_in = True
                        if got_in:
                            line+= str(temp)
                        else:
                            line+=str(x)
            if line != "":  # so if the line is empty after the head or thr the top it wont go a line under
                print(line)
            line = ""  # afrer we printed theline we reet it for the next one
        for i in range(perpendicular):  # we running or the lenght of the triangle chela
            if (i == 0) or (i == perpendicular - 1):  # if it is one of the kodkods we add * to the last line
                last_line += "*"
            else:
                last_line += "-"  # if it is not kodkods we print _
        print(last_line)


# check if a number is a prime number
def is_prime(x):
    is_prime = True
    i = 2
    while i <= x ** 0.5:
        if x % i == 0:
            is_prime = False
            break
        i += 1
    return is_prime


# question 2
def goldbach(num):
    i = 2  # the first prime number
    lisrOfList = []  # save all the list of the cuppels of prime numbers
    listOfTow = []  # temp list of the couples
    if ((num % 2 != 0) or (num < 4)):  # if the number is zogi
        return lisrOfList
    while i <= (num / 2):  # if i is bigger than the half of the number it will be reapeted
        if is_prime(i):  # if i is prime number
            if is_prime(
                    num - i):  # if the addition of a number to i that will be equal to the number is a prime number and not
                listOfTow.append(i)  # put the lower prime number first
                listOfTow.append(num - i)  # put the bugger prime number after
                lisrOfList.append(listOfTow)  # put the couple in the list
                listOfTow = []  # reset the temp list
        i += 1  # add one to i
    return lisrOfList


# question 3
def seven_poom(start, rounds):
    game_lst = []  # the list that saves the numbers
    if rounds == 0:
        return game_lst
    if rounds>0:  # if the numbers is going up
        for i in range(start, rounds + start):
            if (i % 7 == 0 or ("7" in str(i))): # if the number is divided by 7 or has 7 in his digits
                if is_prime(i): # if it is a prime number
                    game_lst.append("Poom") # if it is both u put poom if it is not prime number put boom
                else:
                    game_lst.append("Boom")
            else:
                game_lst.append(i) # if it is not divided by 7 or has the digit 7 put the number himself
        return game_lst
    else:
        for i in range(start, rounds + start, -1):
            if i == 0:
                break
            if (i % 7 == 0 or ("7" in str(i))): # if the number is divided by 7 or has 7 in his digits
                if is_prime(i):# if it is a prime number
                    game_lst.append("Poom")# if it is both u put poom if it is not prime number put boom
                else:
                    game_lst.append("Boom")
            else:
                game_lst.append(i)# if it is not divided by 7 or has the digit 7 put the number himself

    return game_lst