# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5
"""
27.While purchasing certain items, a discount of 10% is offered if the quantity purchased is
more than 1000. If quantity and price per item are input through the keyboard, write a
 program to calculate the total expenses.
"""
# lets suppose 3 items are bought
a = int(input("Price for item 1 :"))
b = int(input("Quantity of item 1 :"))
c = int(input("Price for item 2 :"))
d = int(input("Quantity of item 2 :"))
e = int(input("Price for item 3 :"))
f = int(input("Quantity of item 3 :"))

k = a * b
l = c * d
m = e * f

if b > 1000:
    k = k - (k /10)
else:
    k = k
if d > 1000:
    l = l - (l /10)
else:
    l = l
if f > 1000:
    m = m - (m /10)
else:
    m = m
print("Total price for item 1 is ", k)
print("Total price for item 2 is ", l)
print("Total price for item 3 is ", m)
x = k + l + m
print("Total expenses = ", x)