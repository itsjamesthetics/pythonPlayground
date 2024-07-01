'''
    Developed by: James Ald Teves
    BS Computer Science
    Python program to add 2 integers

    Description: This program enables to demonstrate an input and output
    with a combination of addition operation.    
'''


import operator

#Input
num1 = int(input("\n\t Enter first integer: "))
num2 = int(input("\n\t Enter second integer: "))

sum = operator.add(num1, num2)

print("\n\t The sum of {0} and {1} is {2}".format(num1, num2, sum))