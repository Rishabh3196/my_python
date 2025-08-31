# NAME : RISHABH RAJ
# ADMN.NO :23SCSE1011979
# SEC-5

"""
30.An event organizer company needs to organize an event for 100 people.
Accept the length and breadth of the hall. Calculate area and display
message based on following criteria.
Area Message display
>=10000 suitable for event
<10000 not suitable
"""
a = int(input("Enter the lenght of the hall :"))
b = int(input("Enter the breadth of the hall :"))
c = a * b

if c >= 10000:
    print("THE HALL IS SUITABLE FOR EVENT")
else:
    print("THE HALL IS NOT SUITABLE FOR EVENT")