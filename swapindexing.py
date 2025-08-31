n = int(input("enter size of list:"))
list = []
for i  in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("enter index1: "))
idx2 = int(input("enter index2: "))
temp = list[idx1]

list[idx1] = list[idx2]
list[idx2] = temp
print(list)