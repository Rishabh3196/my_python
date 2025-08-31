# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5
"""
35.If the three sides of a triangle are entered through the keyboard,
write a program to check whether the triangle is isosceles, equilateral,
scalene or right angled triangle.
"""
a = int(input("Enter the value of side 'A' :"))
b = int(input("Enter the value of side 'B' :"))
c = int(input("Enter the value of side 'C' :"))
print()

if a > b and a > c:
    f1 = a
    if b + c > f1:
        print("The triangle is valid")
        if a * a == (b * b) + (c * c):
            print("This is Right Angled Triangle AND also a Scalene Triangle")
        elif a == b or a == c or b == c:
            print("This is Isosceles Triangle")
        else:
            print("This is Scalene Triangle")
    else:
        print("The triangle is not valid")

elif b > c and b > a:
    f2 = b
    if a + c > f2:
        print("The triangle is valid")
        if b * b == (a * a) + (c * c):
            print("This is Right Angled Triangle AND also a Scalene Triangle")
        elif a == b or a == c or b == c:
            print("This is Isosceles Triangle")
        else:
            print("This is Scalene Triangle")
    else:
        print("The triangle is not valid")
elif c > a and c > b:
    f3 = c
    if b + a > f3:
        print("The triangle is valid")
        if c * c == (b * b) + (a * a):
            print("This is Right Angled Triangle AND also a Scalene Triangle")
        elif a == b or a == c or b == c:
            print("This is Isosceles Triangle")
        else:
            print("This is Scalene Triangle")
    else:
        print("The triangle is not valid")
elif a == b == c:
    f4 = a
    print("The triangle is valid")
    print("THIS IS A EQUILATERAL TRAINGLE")