class Book:
    def prop(self):
        print("Django")
    def read(self):
        print("couse")
class Read(Book):
    def read(self):
        print("python")
r=Read()
r.read()