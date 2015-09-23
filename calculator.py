"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.


"""

from arithmetic import *


# Your code goes here
# No setup
'''repeat forever:
    read input
    tokenize input
    if the first token is 'q', quit
    otherwise decide which math function to call based on the tokens we read'''
def calculatorz():
    while True:
        user_data=raw_input(" > ")
        tokenized_user_data=user_data.split(" ")
        if tokenized_user_data[0]=="q":
            break
        elif tokenized_user_data[0]== "+":
            print add(int(tokenized_user_data[1]),int(tokenized_user_data[2]))
        elif tokenized_user_data[0]== "-":
            print subtract(int(tokenized_user_data[1]),int(tokenized_user_data[2]))
        elif tokenized_user_data[0]== "*":
            print multiply(int(tokenized_user_data[1]),int(tokenized_user_data[2]))
        elif tokenized_user_data[0]== "/":
            print divide(int(tokenized_user_data[1]),int(tokenized_user_data[2]))
        elif tokenized_user_data[0]== "square":
            print square(int(tokenized_user_data[1]))
        elif tokenized_user_data[0]== "cube":
            print cube(int(tokenized_user_data[1]))
        elif tokenized_user_data[0]== "pow":
            print power(int(tokenized_user_data[1]),int(tokenized_user_data[2]))
        elif tokenized_user_data[0]== "mod":
            print mod(int(tokenized_user_data[1]),int(tokenized_user_data[2]))
calculatorz()
