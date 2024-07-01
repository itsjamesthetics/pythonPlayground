import sys

# Programmed by: James Ald Teves
# Exercise 1 (Input and output statements with simple addition)

#UserInputName
name = input ("\n What is your name? ")
print("\n Hello", name)
print("\n Let's write your name in Small Case! ")
print(name.lower())
Surname = "teves"
sys.stdin.flush()
print("\n When we get married, Your name will be " + name + " " + Surname)

#Age
sys.stdin.flush()
age = int (input ("\n What year you are born? "))
finalAge = 2023 - age
print("\n Your Age is ", finalAge)
futureYears = 10
Future = futureYears + finalAge
sys.stdin.flush()
print("\n In 10 years, you would be", Future)

