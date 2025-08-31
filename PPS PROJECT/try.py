class Human:
    def work(self):
        print("i can run")

    def eat(self):
        print("i will eat")

class Male(Human):
    def __init__(self):
        self.num_eyes = 2

    def flirt(self):
        print("i can flirt")

    def work(self):
        super().work()
        print("i can code")

class Female (Human):
    def __init__(self):
        self.num_boobs = 2

    def sexy(self):
        print("aaro is too sexy")

    def hottie(self):
        print("pihu is too hottie")

    def work(self):
        super().work()
        print("i can do sex")


female_1=Female()
female_1.hottie()
print(female_1.num_boobs)
female_1.work()




male_1=Male()
male_1.work()
male_1.flirt()
print(male_1.num_eyes)

