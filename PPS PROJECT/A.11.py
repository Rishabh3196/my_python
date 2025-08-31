# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 11 Python Program to Print Odd Numbers Within a Given Range

print("Print Odd Numbers Within a Given Range ")
num_1 = int(input("Enter the first value :"))
num_2 = int(input("Enter the second value :"))
Oddlist = []
for i in range(num_1, num_2):
    if i % 2 != 0:
        Oddlist.append(i)
print("Odd number from ", num_1, "to", num_2, "are", Oddlist)
