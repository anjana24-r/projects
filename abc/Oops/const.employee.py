class Employee:
    def __init__(self, name,id,desig,salary,company):
        self.name = name
        self.id = id
        self.desig=desig
        self.salary=salary
        self.company=company

    def printval(self):
        print(self.name,self.id,self.desig,self.salary,self.company)


em= Employee("ammu\n","1022\n","Software Engineer\n","30000\n","Tcs")

em.printval()
