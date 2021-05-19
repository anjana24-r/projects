class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def printval(self):
        print("name",self.name)
        print("type",self.type)
class Dog(Animal):
    def __init__(self,bark,name,type):
        super().__init__(name,type)
        self.bark=bark

    def print(self):
        print(self.bark)

        print(self.name,self.type)
dg=Dog("bark","tom","domestic animal")
dg.printval()
dg.print()
