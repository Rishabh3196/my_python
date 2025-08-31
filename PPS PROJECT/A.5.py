# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 5 Write a program to display all odd numbers from 1 to 20

print("Display odd no between given two numbers ")
num_1 = int(input("Enter the first value :"))
num_2 = int(input("Enter the second value :"))
Oddlist = []
Evenlist = []
for i in range(num_1, num_2):
    if i % 2 == 0:
        Evenlist.append(i)
    else:
        Oddlist.append(i)
print("Odd number from ", num_1, "to", num_2, "are", Oddlist)
print("Even number from ", num_1, "to", num_2, "are", Evenlist)