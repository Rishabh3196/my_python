# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 10 Write a program to Convert the given Binary Number into Decimal.

def binary(binary_1):
    x,y = 0,0
    while binary_1 != 0:
        z = binary_1 % 10
        x = x + (z * pow(2,y))
        binary_1 = binary_1 // 10
        y += 1
    return x
binary_1 = int(input("Enter the Binary number :"))
a = binary(binary_1)
print("The decimal form of the given binary number", binary_1, "is", a)