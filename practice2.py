#circumference and area of circle
#circumference
#r = int(input("enter radius of circle:"))
#circumference = 2 * 3.14 * r
#area = 3.14 * r * r
#print(f" circumference ={circumference} \n area = {area}")

n = float(input("enter number of hours:"))
print("Total amount = No. of hours * charges per hour"
          "\nGst = 18% of total amount"
          "\nAmount due = Total amount + Gst"
          "\n"
          "\nTherefore")
print()
#charg per hour rs200
b = 200
x = n * b
y = (18/100) * x
z = x + y
print(f" total amount = {x} ")
print()
print(f" Gst = {y}")
print()
print(f" amount due = {z}")


