class Human:
    def eat(self):
        print("I can eat")

    def work(self):
        print("I can work")



class Male(Human):
    pass

    def flirt(self):
        print("I can flirt")

    def work(self):
        super().work()
        print("Ican run")


male_1 = Male()
male_1.eat()
male_1.flirt()
male_1.work()




