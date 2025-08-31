# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

"""
34. A year is entered through the keyboard, write
a program to determine whether the year
is leap or not. Use the logical operators and & or.
If year % 4 = 0 and year % 100!= 0 or year%400 == 0:
Print leap year
"""
a = int(input("Enter the year :"))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(a, "is a Leap year")
else:
    print(a, "is not a leap year")