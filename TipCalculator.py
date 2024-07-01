# Programmed by: James Ald Teves
# Activity 1: Tip Calculator

#Input
Bill = float (input("\n Meal Ammount: $ "))
tipBill = Bill * 0.15
finallTip = "{:.2f}".format(tipBill, 2)

#Output
print("\n Server Tip: $ " + finallTip)