'''
    Developed by: James Ald Teves
    BS Computer Science
    CCS 1 - C
'''

twist = True
while twist == True:

    nums = 0
    result = 0
    i = 0

    while nums < 1 or nums > 300:
        nums = int (input("Enter an integer: "))
        if nums > 300 or nums < 1:
            print ("Invalid. Choose only between 1 and 300.")
            continue

        while i < nums:
            i = i + 1
            if i%3 == 0 or i%5 == 0:
                result += i 
                print(" The multiples of 3 or 5 are: " ,format(result))
                
        
        

    repeater = input("\nWould you like to continue Y or N?")
    if repeater == "Yes" or repeater == "YES" or repeater == "Y" or repeater == "y" or repeater == "yes":
        continue
    elif repeater == "No" or repeater == "NO" or repeater =="no" or repeater == "N" or repeater == "n":
        print ("I hope you enjoyed. Have a great day!")
        break
    else:
        break