#1 cc multiple pc

# class Parent:
#     def m1(self):
#         print("inside parent")
#
#
# class Child:
#     def m2(self):print("inside child class")
#
#
# class Subchild(Child,Parent):
#     def m3(self):
#        print("inside subchild")
#
# obj=Subchild()
# obj.m3()
# obj.m2()
# obj.m1()

# class Parent:
#     def m1(self):
#          print("Anjana")
#
# class Child:
#     def m2(self):
#         print("22 years")
#
# class Subchild(Child,Parent):
#     def m3(self):
#        print("python course")
#
# obj=Subchild()
# obj.m1()
# obj.m2()
# obj.m3()
a=int(input("enter"))
b=int(input("enter"))
class Parent:
     def m1(self):
        print(a)
class Child:
    def m2(self):
        print(b)
class Subchild(Child,Parent):
    def m3(self):
        c=a+b
        print(c)
obj=Subchild()

obj.m3()
