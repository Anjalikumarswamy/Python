#class 

class Dog:
    #creating method
    def __init__(self,name):
        self.name = name
        print("Object with name : {}".format(name))

    def __str__(self):
        return self.name
    
    #when we are creating method in class first paramter is self.
    def talk(self):
        print("woof")

    def printName(self):
        print("My Name is : {}".format(self.name)) #{} - data to be replaced

dog = Dog("Bruno") #object creation
dog1 = Dog("Panda")
dog.talk()
dog1.talk()
dog.printName()
dog1.printName()

print(dog) #printing dog object