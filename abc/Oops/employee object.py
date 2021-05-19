class Employee:
    def setval(self,ename,id,salary):
        self.ename=ename
        self.id=id
        self.salary=salary
        print(self.ename,self.id,self.salary)
    def __str__(self):
        return self.ename + str(self.id)
em=Employee()
em.setval("anjana",123,30000)
print(em)