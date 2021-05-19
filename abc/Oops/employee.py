class Employee:
    def empdet(self, name,id,desig,salary,company):
        self.name = name
        self.id = id
        self.desig=desig
        self.salary=salary
        self.company=company

    def printval(self, gender):
        self.gender = gender
        print(self.name)
        print(self.id)
        print(self.desig)
        print(self.salary)
        print(self.company)
        print(self.gender)


em= Employee()
em.empdet("ammu", 22,"manager",600000,"abc")
em.printval("female")
