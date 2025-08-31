# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 32.Find Largest of three numbers.

a = float(input("Enter first number :"))
b = float(input("Enter second number :"))
c = float(input("Enter third number :"))
print("The given three numbers are ", a, ",", b, "and", c)

if a > b and a > c:
    print(a, "is the largest of given 3 numbers")
elif b > c and b > a:
    print(b, "is the largest of given 3 numbers")
else:
    print(c, "is the largest of given 3 numbers")