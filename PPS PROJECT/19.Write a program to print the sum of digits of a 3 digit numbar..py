# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 19.Write a program to print the sum of digits of a 3 digit number.
# applicable for only 3 digit number

print("SUM OF THE DIGIT OF A 3 DIGIT NUMBER")
print()
n = int(input("Enter a three digit number :"))
#n = int(n)
d1 = n % 10
n1 = n // 10
d2 = n1 % 10
n2 = n1 // 10
print("sum of the digits of ", n, "is", d1 + d2 + n2)
print()