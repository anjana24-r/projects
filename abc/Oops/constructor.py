class Person:
    def __init__(self,name,age,gender):      #setval replace bt init initialiazation
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name,self.age,self.gender)
pe=Person("ammu",22,"female")

pe.printval()

#constructor to initialise instance variables
#constructor automatically invoke when creating object