#class syntax
#...

# class classname:   #class nam eshould strt with capital letter
#attributes - variables
#methods - fn

class Person:
    def print(self,name,age,gender): #name,age...attribute
        self.name=name
        self.age=age
        self.gender=gender
        print("inside print method\n",self.name,self.age,self.gender)
#object creation
pe=Person()  #reference for obj creation
pe.print("ammu",22,"female")
re=Person()
re.print("anjana",22,"female")
