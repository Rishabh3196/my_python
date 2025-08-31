class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Students("Raj", 22, "A+")
print("NAME:", student1.name)
print("AGE:", student1.age)
print("GRADE:", student1.grade)