class Human:
    def __init__(self):
        self.num_eyes = 2
        self.num_heart = 1

    def work(self):
        print("I can run")

    def fuck(self):
        print("I can fuck")


class Male:
    def sleep(self):
        print("i can sleep")

    def work(self):
        print("I can code")


class Boy(Human, Male):
    def dance(self):
        print("Ican dance")

    def work(self):
        print("I can sing")


boy_1 = Boy()
boy_1.work()
male_1 = Male()
male_1.work()
print(boy_1.num_heart)

