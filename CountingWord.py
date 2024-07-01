#Programmed by James Ald Teves
#Counting Word occurrences length greater than 2

#User Input
inputText = input("\n\t Enter the text: ")

#Split Inputs
noWords = inputText.split()

#Conditional Statement
if len(inputText.split()) > 2:
    print("\n\t The words are: ", noWords)
    print("\n\t Words Counted: ", len(inputText.split()))
else:
    print("\n\t The Word is less than 2. ")