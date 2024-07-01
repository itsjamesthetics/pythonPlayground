#Python program that determine which is the maximum

def Max(x, y):
    if x > y:
        return x
    else:
        return y

a = int(input("Enter 1st int: "))
b = int(input("Enter 2nd int: "))

print("The maximum value of integer is {0}".format(Max(a,b)))