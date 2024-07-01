# Programmed by: James Ald Teves
# Activity 1: Tip Calculator (modified)

#Input
Bill = float (input("\n Meal Ammount: $ "))
Tip = float (input("\n Tip Percentage: " + "%"))
billTip = Tip / 100
Tips = Bill * billTip
FinalTip = "{:.2f}".format(Tips, 2)

#Output
print("\n Server Tip: $" + FinalTip)