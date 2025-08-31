# NAME : Rishabh raj
# ADMN.NO :23SCSE1012243
# SEC-5

# 4 Write a program to Simulate Arithmetic Calculator.

def add(num_1,num_2):
    return num_1 + num_2
def subtract(num_1,num_2):
    return num_1 - num_2
def multiply(num_1,num_2):
    return num_1 * num_2
def divide(num_1,num_2):
    return num_1 / num_2

print(""""
      1.ADD
      2.SUBTRACT
      3.MULTIPLY
      4.DIVIDE       
""")

input_1 = int(input("Select operation by entering coresponding numerical value :"))
if input_1 <= 4:
    num_1 = int(input("Enter first number :"))
    num_2 = int(input("Enter the second number :"))

    if input_1 == 1:
        print(num_1, "+", num_2, "=", add(num_1, num_2))
    elif input_1 == 2:
        print(num_1, "-", num_2, "=", subtract(num_1, num_2))
    elif input_1 == 3:
        print(num_1, "*", num_2, "=", multiply(num_1, num_2))
    elif input_1 == 4:
        print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("Invalid input .")