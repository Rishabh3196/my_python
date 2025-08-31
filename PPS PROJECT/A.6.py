# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 6 Write a program to Check whether a given Number is an Armstrong Number.

num_1 = int(input("Enter a number :"))
sum = 0
a = num_1
while a > 0:
    x = a % 10
    sum += x ** 3
    a //= 10
if num_1 == sum:
    print("ARMSTRONG")
else:
    print("Not Armstrong")