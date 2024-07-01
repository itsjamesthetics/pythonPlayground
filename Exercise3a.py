#Programmed by: James Ald Teves
#Exercise 3a (If Statement)

#Input User
#Mark One Input
markOne = int(input("\n\t Enter First Mark Obtained: "))
if markOne < 0 or markOne > 100:
    print(markOne, "\n\t Only Input from 0-100 ")
    exit()
elif markOne > 0 and markOne < 100:
    print("\n\t Recorded!")

#Mark Two Input        
markTwo = int(input("\n\t Enter Second Mark Obtained: "))
if markTwo < 0 or markTwo > 100:
    print(markTwo, "\n\t Only Input from 0-100 ")
    exit()
elif markTwo > 0 and markTwo < 100:
    print("\n\t Recorded!")

#Mark Three Input
markThree = int(input("\n\t Enter Mark Obtained: "))
if markThree < 0 or markThree > 100:
    print(markThree, "\n\t Only Input from 0-100 ")
    exit()
elif markThree > 0 and markThree < 100:
    print("\n\t Recorded!")

#Solution
total = markOne + markTwo + markThree
totalAve = total / 3
FinalTotal = "{:.2f}".format(totalAve, 2)

#Else if Statement
if (totalAve >= 90):
    print("\n\t\t  Your Grade is A", FinalTotal + "%")
elif (totalAve >= 80):
    print("\n\t\t  Your Grade is B", FinalTotal + "%")
elif (totalAve >= 70):
    print("\n\t\t  Your Grade is C", FinalTotal + "%")
elif (totalAve >= 60):
    print("\n\t\t  Your Grade is D", FinalTotal + "%")
elif (totalAve >= 40):
    print("\n\t\t  Your Grade is E", FinalTotal + "%")
elif (totalAve < 40):
    print("\n\t\t  Your Grade is F", FinalTotal + "%")
else:
    print("\n\t\t Your Grade is F")