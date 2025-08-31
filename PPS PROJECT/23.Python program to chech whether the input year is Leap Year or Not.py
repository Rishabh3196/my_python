# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 23.Python program to check whether the
# input year is Leap Year or Not
a = int(input("Enter the year :"))
b = a % 4
if b==0:
    print(a, "is leap year")
else:
    print(a, "is not a leap year")