class Vehicle:
    def details(self,type,wheel):
        self.type=type
        self.wheel=wheel

    def printdet(self):
        print(self.type)
        print(self.wheel)

class Bus(Vehicle):
    def det(self,regno,ownername):
        self.regno=regno
        self.ownername=ownername
    def prints(self):
        print(self.regno)
        print(self.ownername)
ve=Vehicle()
ve.details("bus","4whlr")
ve.printdet()
bu=Bus()
bu.det("KL09AB1234","jOHN")
bu.prints()
# em.details("ammu",22,"female")
# em.printdet()