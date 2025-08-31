# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5
"""
33.3 If the three sides of a triangle are entered through the
keyboard, write a program to  check whether the triangle is
valid or not. The triangle is valid if the sum of two sides is
greater than the largest of the three sides.
"""
a = int(input("Enter the value of side 'A' :"))
b = int(input("Enter the value of side 'B' :"))
c = int(input("Enter the value of side 'C' :"))
print()
print('''FOR TRAINGLE TO BE VALID
THE SUM OF THE TWO SIDE SHOULD BE GREATER THAN THE GREATEST SIDE''')
print()
if a > b and a > c:
    f1 = a
    if b + c > f1:
        print("The triangle is valid")
    else:
        print("The triangle is not valid")
    print("The greatest side of the triangle is", f1)

elif b > c and b > a:
    f2 = b
    if a + c > f2:
        print("The triangle is valid")
    else:
        print("The triangle is not valid")
    print("The greatest side of the triangle is", f2)

elif c > a and c > b:
    f3 = c
    if b + a > f3:
        print("The triangle is valid")
    else:
        print("The triangle is not valid")
    print("The greatest side of the triangle is", f3)

elif a == b == c:
    f4 = a
    print("The triangle is valid")
    print("THIS IS A EQUILATERAL TRAINGLE")
    print("The side of the triangle", f4)
    print()