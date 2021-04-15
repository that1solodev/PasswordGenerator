from PyInquirer import prompt
import numpy as np 
import pyperclip
import random

if __name__ == "__main__":
    allCaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    allSmalls = "abcdefghijklmnopqrstuvwxyz"
    allNums = "0123456789"
    allSpecials = "@%+/!#\\?-=()[]{}$&*"

    ## password size
    pass_Size = input("Enter Password Size(8-16): ")
    try:
        pass_Size = int(pass_Size)
    except ValueError:
        exit("Invalid Password Size")
    if pass_Size > 16 or pass_Size < 8:
        exit("Invalid Password Size")

    ## Capital or not
    questions = [{
            'type':'list',
            'name':'capital',
            'message':'Do you want Capital letters?: ',
            'choices': ['Yes','No']
        }]
    ans = prompt(questions)['capital']

    ## Capital letter Count
    if ans == 'Yes':
        capital = True
        count_Capital = input("How many Capital letter you want?: ")
        try:
            count_Capital = int(count_Capital)
        except ValueError:
            exit("Invalid Capital Count")
        if count_Capital > pass_Size:
            exit("Invalid Capital Count")
    else:
        capital = False
        count_Capital = 0

    ## Special Character or not
    questions = [{
            'type':'list',
            'name':'special',
            'message':'Do you want Special Characters?: ',
            'choices': ['Yes','No']
        }]
    ans = prompt(questions)['special']

    ## Special Character Count
    if ans == 'Yes':
        special = True
        count_Special = input("How many Special Characters you want?: ")
        try:
            count_Special = int(count_Special)
        except ValueError:
            exit("Invalid Special Character Count")
        if count_Special + count_Capital > pass_Size:
            exit("Invalid Special Character Count")
    else:
        special = False
        count_Special = 0

    ## Numbers or not
    questions = [{
            'type':'list',
            'name':'number',
            'message':'Do you want Numbers?: ',
            'choices': ['Yes','No']
        }]
    ans = prompt(questions)['number']

    ## Number Count
    if ans == 'Yes':
        number = True
        count_Number = input("How many Number you want?: ")
        try:
            count_Number = int(count_Number)
        except ValueError:
            exit("Invalid Number Count")
        if count_Capital + count_Special + count_Number > pass_Size :
            exit("Invalid Number Count")
    else:
        number = False
        count_Number = 0
    
    ## Small Letter Count
    count_Small = pass_Size - count_Special - count_Number - count_Capital
    
    ## select count random number of characters from respective list
    passCaps = random.sample(allCaps, count_Capital)
    passSpecials = random.sample(allSpecials, count_Special)
    passNums = random.sample(allNums, count_Number)
    passSmalls = random.sample(allSmalls,count_Small)

    ## password shuffling
    passNonShuffled = passCaps + passSpecials + passNums + passSmalls
    random.shuffle(passNonShuffled)
    finalPassword = "".join(passNonShuffled)

    print("finalPassword: ", finalPassword)
    pyperclip.copy(finalPassword)
    print("Password copied to clipboard")