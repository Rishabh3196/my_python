# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 2 Write a program to find the perimeter of a circle, rectangle and triangle

print("For perimeter of circle")
radius = float(input("Enter the value of radius : "))
perimeter = 3.14 * 2 * radius
print("Perimeter of the circle is ", perimeter)
print()
print("For perimeter of rectangle")
length = float(input("Enter the value of length : "))
breadth = float(input("Enter the value of breadth : "))
perimeter = 2 * (length + breadth)
print("Perimeter of the rectangle is ", perimeter)
print()
print("For perimeter of triangle")
side_1 = float(input("Enter the value of side_1 : "))
side_2 = float(input("Enter the value of side_2 : "))
side_3 = float(input("Enter the value of side_3 : "))
perimeter = side_3 + side_2 + side_1
print("Perimeter of the triangle is ", perimeter)