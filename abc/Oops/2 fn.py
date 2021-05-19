class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printval(self,gender):
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
per=Person()
per.setval("ammu",22)
per.printval("female")

