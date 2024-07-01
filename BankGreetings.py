#Programmed by: James Ald Teves
#Bank Greetings

#User Input
userGreetings = input("\n\t Greetings: ")

#Initilized Value
userBank = 0

#If else Conditional Statement
if userGreetings == "hello" or userGreetings == "HELLO" or userGreetings == "Hello":
    userBank += 0
    print("\n\t $",  userBank)

elif userGreetings == "h" or userGreetings == "H":
    userBank += 20
    print("\n\t $", userBank)

else:
    userBank += 100
    print("\n\t $", userBank)