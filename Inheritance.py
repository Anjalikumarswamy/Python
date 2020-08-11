class Person: 
    def __init__(self, name):
        self.name = name
    
    def SayName(self):
        print("My name is : {}".format(self.name))

class Engineer(Person):   # single inheritance 
    def __init__(self,name):
        super().__init__(name)
        self.profession = "Engineer"

    def sayProfession(self):
        print(self.profession)

class Doctor(Person):  # hirearchical Inheritance
    def __init__(self,name):
        super().__init__(name)
        self.profession = "Doctor"

    def sayProfession(self):
        print(self.profession)


engineer = Engineer("John")
doctor = Doctor("Jane")
engineer.SayName()
engineer.sayProfession()
doctor.SayName()
doctor.sayProfession()

