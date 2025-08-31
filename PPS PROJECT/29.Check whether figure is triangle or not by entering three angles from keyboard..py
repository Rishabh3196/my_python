# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 29.Check whether figure is triangle or not by
# entering three angles from keyboard.
a = int(input("Enter the value of angle 1 :"))
b = int(input("Enter the value of angle 2 :"))
c = int(input("Enter the value of angle 3 :"))

d = a + b + c

if d==180:
    print("The given figure is a triangle")
else:
    print("The given figure is not a triangle")