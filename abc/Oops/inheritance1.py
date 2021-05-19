class Person:
    def permet(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name,self.age,self.gender)
class Parent(Person):      #single inheritance person-parent
    def parmet(self,job,place,salary):
        self.job=job
        self.place=place
        self.salary=salary
        print(self.job,self.place,self.salary)
class Child(Person):    #single inheritance
    def chmet(self,school):
        self.school=school
        print(self.school)
class Student(Child):    #multilevel inheritance
    def stmet(self,rollno):
        self.rollno=rollno
        print(self.rollno)