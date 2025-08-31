class Instructor:
    followers = 0         # class object variable

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self, subject_name):
        print(f"hi, i am {self.name} and i teach {subject_name}")

    def update_followers(self, follower_name):
        self.followers += 2


instructor_1 = Instructor("jenny","kargil")
print(instructor_1.name)
instructor_1.display("python")
instructor_1.update_followers("ravi")
print(instructor_1.followers)
instructor_2 = Instructor("rahul", "patil")
instructor_2.update_followers("nikhil",)
print(instructor_2.followers)


