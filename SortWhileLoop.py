#Programmed by: James Ald Teves
#Sort method with For or While loop statement Exercise

#Array Input
inputList = []

#Input User How many Elements
inputNum = int(input("\n\t Enter the Total Number of Lists Elements: "))

#For Loop
for i in range (1, inputNum + 1):

    #Input User for Values to be Stored
    value = int(input("\n\t Enter Value of %d Element: " %i))
    inputList.append(value)

#Sorting
inputList.sort()

#Display
print("\n\t Element After Sorting List in Ascending Order is: ", inputList)