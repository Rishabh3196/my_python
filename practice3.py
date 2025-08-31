class Staff:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class Teacher(Staff):
    def __init__(self, name, position, subject):
        super().__init__(name, position)
        self.subject = subject


teacher1 = Teacher("ravi", "teach", "oops")
staff1 = Staff("lalu", "cook")
print("NAME", teacher1.name)
print("work", teacher1.position)
print("subject", teacher1.subject)




