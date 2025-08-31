# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

"""8 Write a program to display the following pattern:
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * """

n = int(input("Enter the no of rows :"))
for i in range(n):
    for j in range(i+1):
        print(" " , end=" ")
    for j in range(i,n):
        print("*", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    print()