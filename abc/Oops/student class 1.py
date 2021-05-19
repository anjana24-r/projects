class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
    def printval(self):
        print("name=",self.name)
        print("rollno=",self.rollno)
        print("course=",self.course)
        print("mark=",self.mark )
    def __str__(self):
        return self.name

lst=[]
f=open("student1","r")
for lines in f:
    data=lines.split(",")
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=int(data[3])
    obj=Student(name,rollno,course,mark)
    lst.append(obj)
for i in lst:
   if i.marks>190:
       print(i)