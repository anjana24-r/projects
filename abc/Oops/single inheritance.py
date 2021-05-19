#single inheritance
#1 cc 1 pc
# class Person:   #parent class/base class/super class
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printdet(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
# #child class creation
# class Student(Person):  #child class/sub class/derived class  #inheriting class name in bracket
#     def det(self,rollno,school):
#         self.rollno=rollno
#         self.school=school
#     def prints(self):
#         print(self.rollno)
#         print(self.school)
# per=Person()
# per.details("ammu",22,"female")
# per.printdet()
# st=Student()
# st.det(22,"bss")
# st.prints()
# st.details("ammu",22,"female")
# st.printdet()

#.......
#person employee
#........

class Person:
    def details(self,name,age,gender): #not necessary to use self itself can use anyothe thing
        self.name=name
        self.age=age
        self.gender=gender
    def printdet(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def det(self,desig,salary):
        self.desig=desig
        self.salary=salary
    def prints(self):
        print(self.desig)
        print(self.salary)
per=Person()
per.details("ammu",22,"female")
per.printdet()
em=Employee()
em.det("software Engineer",45000)
em.prints()
em.details("ammu",22,"female")
em.printdet()