#Import Statement
import calendar
from calendar import monthrange

#Programmed by: James Ald Teves
#Exercise 3b (Nested If Statement)

#User Input
inputYear = int(input("\n\t Enter year: "))
inputMonth = int(input("\n\t Enter month: "))

#Visual Display
print(calendar.month(inputYear, inputMonth))

#Solution
if (inputYear % 400 == 0) and (inputYear % 100 == 0):
    print("{0} is a leap year.".format(inputYear))
elif (inputYear % 4 == 0) and (inputYear % 100 != 0):
    print("{0} is a leap year.".format(inputYear))
elif (inputYear > 12) and (inputYear < 1):
    print("\n\t The are only 12 ")
else:
    print("{0} is not a leap year.".format(inputYear))

print(calendar.monthrange(inputYear, inputMonth), "Days")






