class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):

        return 2 * self.pi * self.radius

    def get_area(self):

        return self.pi * self.radius * self.radius

    
circle_1 = Circle(3)
print("circumference = ", circle_1.get_circumference())
print("area = ", circle_1.get_area())
circle_2 = Circle(5)
print("circumference = ", circle_2.get_circumference())
print("area = ", circle_2.get_area())



