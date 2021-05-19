#polymorphism - ability to have many forms
#overloading - same methd name diff parameter
#overriding - same method name same no:of argument

#overriding
#......

class Parent:     #child class work
    def prop(self):
        print("abc")
    def marry(self):
        print("def")
class Child(Parent):
    def marry(self):
        print("fgh")
c=Child()
c.marry()