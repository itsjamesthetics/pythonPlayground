'''
    Developed by: James Ald Teves
    BS Computer Science
    CCS 1 - C

    Description: This program is a simple calculator that uses function in the operation.
'''

def add(a, b):
	result = a+b
	resfloat = "{:.2f}".format(result)
	print(resfloat)
def sub(a, b):
	result = a-b
	resfloat = "{:.2f}".format(result)
	print(resfloat)
def mul(a, b):
	result = a*b
	resfloat = "{:.2f}".format(result)
	print(resfloat)
def div(a, b):
	result = a/b
	resfloat = "{:.2f}".format(result)
	print(resfloat)

a = float (input ("Enter the first number: "))
b = float (input ("Enter the second number: "))
op = input ("Enter the operator: ")


if op == "+":
	add(a, b)
elif op == "-":
	sub(a, b)
elif op == "*":
	mul(a, b)
elif op == "/":
	div(a, b)
else: 
	print("Invalid Operator")

#The Operators you select may only include such as: +, -, *, /.
#You can input a float integer with 2 decimal places.