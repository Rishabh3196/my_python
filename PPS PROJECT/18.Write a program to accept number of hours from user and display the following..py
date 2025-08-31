# NAME : RISHABH RAJ
# ADMN.NO :23SCSE10119796
# SEC-5

# 18.Write a program to accept number of hours from user
# and display the following.
a = float(input("ENTER THE NO OF HOUR'S :"))
print("Total Amount= No of Hours * Charges per hour"
      "\nGST= 18% of Total Amount"
      "\nAmount Due= Total Amount+GST"
      "\n"
      "\nTherefore")
print()
# let charge per hour be rs 200
b = 200
x = a * b
y = (18 / 100) * x
z = x + y
print("Total Amount= RS", x)
print()
print("GST= RS", y)
print()
print("Amount Due= RS", z)