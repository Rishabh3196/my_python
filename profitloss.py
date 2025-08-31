cp=int(input("enter cost price:"))
sp=int(input("enter selling price:"))
if cp > sp:
    loss = cp - sp
    print("we made loss of", loss)
elif cp < sp:
    profit = sp - cp
    print("we made profit of", profit)
else:
    print("neither profit nor loss")
