# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979

# SEC-5

# 1 Write a program to Read Two Numbers and Print Their Quotient and Remainder

first_num = int(input("Enter the first number :"))
second_num = int(input("Enter the second number :"))
print("First number = ", first_num, "\n", "Second number = ", second_num)
print("When first number divided by second number")
quotient = first_num // second_num
remainder = first_num % second_num
print("quotient = ", quotient, "\n", "remainder = ", remainder)
print()
print("When second number divided by first number")
quotient = second_num // first_num
remainder = second_num % first_num
print("quotient = ", quotient, "\n", "remainder = ", remainder)