# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

# 16.Write a program to convert temperature from
# degree to centigrade to fahrenheit.
print("CONERSION BETWEEN °C & F ")
print()
print("°C TO F")
a = float(input("Enter the Temperature in °C :"))
x = 32 + 1.8 * a
print(a,"°C in Fahrenheit is", x,"F")
print()
print("F TO C°")
b = float(input("Enter the Temperature in F :"))
y = (b - 32)/1.8
print(b,"F in Celsius is", y,"°C")