available_amount = int(input("enter available amount: "))
withdrawl_amount = int(input("enter withdrawl amount: "))

if withdrawl_amount < available_amount:
    if withdrawl_amount % 10 == 0:
        print("transection is successful")
        b = 100
        c = available_amount - (withdrawl_amount + b)
        print("available_amount", c)
    else:
        print("transection is not successful")
else:
    print("low balance")

