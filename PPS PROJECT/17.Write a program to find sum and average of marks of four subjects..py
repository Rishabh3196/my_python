# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 17.Write a program to find sum and average of
# marks of four subjects.
name = input("PLEASE ENTER YOUR NAME :")
print()
print("Enter The Full Marks Of The Subject")
p = int(input("SUBJECT 1 :"))
q = int(input("SUBJECT 2 :"))
r = int(input("SUBJECT 3 :"))
s = int(input("SUBJRCT 4 :"))

print("Enter Marks Obtained in each Subject")
a = float(input("SUBJECT 1 :"))
b = float(input("SUBJECT 2 :"))
c = float(input("SUBJECT 3 :"))
d = float(input("SUBJECT 4 :"))

x = p + q + r + s
sum = a + b + c + d
average = (a + b + c + d) / 4
y = (sum / x) * 100

print()
print("Name :", name)
print("TOTAL MARKS=", x)
print("MARKS OBTAINED=", sum)
print("AVERAGE=", average)
print("PERCENTAGE=", y)