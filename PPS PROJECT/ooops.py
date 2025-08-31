class Instructor:
    def __init__(self, instructor_name, address):
        self.name=instructor_name
        self.address = address
        self.followers = 0

instructor_1 =Instructor("rishabh", "bihar")
print(instructor_1.name)

instructor_2=Instructor("rahul", "sneha")


print(instructor_2.followers)
