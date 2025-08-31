# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 20.Write a program to find real roots of a quadratic equation.
print("FINIDING REAL ROOTS OF QUADRATIC EQUATION")
print()
print("QUADRATIC EQUATION=aX² + bX + c")
a = int(input("Enter the value of 'a' with sign :"))
b = int(input("Enter the value of 'b' with sign :"))
c = int(input("Enter the value of 'c' with sign :"))
print("QUADRATIC EQUATION=", a, 'X²', b, "X", c)

z = ((b ** 2) - (4 * a * c))
d = abs(z) ** (0.5)  # abs == for absolute value
x = (- b + d)
e = (2 * a)
y = (- b - d)
t = (- b)
if z < 0:
    print("No real roots for the equation .")
elif z > 0:
    print("Roots of the equation are :\n ", x, "/", e, "\n", y, "/", e)
elif z == 0:
    print("Roots of the equation are :", t, "/", e)
