i = 4
for i in range(4):
    print("*" * (i+1))

# 2.
n = int(input("ENTER THE NUMBER : "))
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
