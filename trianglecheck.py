a = int(input("enter side a: "))
b = int(input("enter side b: "))
c = int(input("enter side c: "))
print()

if a > b and a > c:
   f1 = a
   if f1 < b + c:
      print("triangle is valid: ")
      if a * a == (b * b) + (c * c):
         print("triangle is right angled triangle and scalene triangle")
      elif a == b or a == c or b ==c:
         print("this is isosceles triangle")
      else:
         print("this is scalene triangle")
   else:
      print("triangle is not valid")
if b > a and b > c:
   f2 = b
   if a + c > f2:
      print("triangle is valid: ")
      if b * b == (a * a) + (c * c):
         print("triangle is right angled triangle and scalene triangle")
      elif a == b or a == c or b == c:
         print("this is isosceles triangle")
      else:
         print("this is scalene triangle")
   else:
      print("triangle is not valid")
if c > a and c > b:
   f3 = c
   if a + b > f3:
      print("triangle is valid: ")
      if c * c == (a * a) + (b * b):
         print("triangle is right angled triangle and scalene triangle")
      elif a == b or a == c or b == c:
         print("this is isosceles triangle")
      else:
         print("this is scalene triangle")
   else:
      print("triangle is not valid")
if a == b == c:
   f4 = c
   print("triangle is valid: ")
   print("this is equilateral triangle")









