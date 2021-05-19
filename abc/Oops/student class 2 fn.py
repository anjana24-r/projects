class Student:
    def setval(self,name,rollno,course):
        self.name=name
        self.rollno=rollno
        self.course=course
    def printval(self,gender):
        self.gender=gender
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.gender)
su=Student()
su.setval("ammu",22,"CSE")
su.printval("female")
