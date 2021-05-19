#functions.....

#block of stmt that together performs single or grp of task.

#print()
#input()
#range()
#type
# a=10
# print(type(a))

# a=10.0
# print(type(a))

#syntax

#def fnname(argument1,argument2):
    #fn stmt

#call() #using fn name

#1. fn without argument and no return type

#2.fn with argument and no return type

#3.fn with argument and return type

#........................

#1. fn without arguments and no return type
#
def add():
    num1=int(input("enter number1"))
    num2=int(input("enter number2"))
    sum=num1+num2
    print(sum)
add()

add()

# def sub():
#     num1=int(input("enter number1"))
#     num2=int(input("enter number2"))
#     diff=num1-num2
#     print(diff)
# sub()

# def pro():
#     num1=int(input("enter number1"))
#     num2=int(input("enter number2"))
#     pro=num1*num2
#     print(pro)
# pro()

# def div():
#     num1=int(input("enter number1"))
#     num2=int(input("enter number2"))
#     div=num1/num2
#     print(div)
# div()

#functional programming

    #to reduce code length

    #lambda - unknown fn(annonymous fn)
    #map
    #filter
    #reduce
    #list comprehension

# f=lambda n1,n2:n1+n2
# print(f(10,20))

#2.fn with arguments and no return type

# def sum(n1,n2):
#     sum=n1+n2
#     print(sum)
# sum(10,20)
# sum(3,9)

#3.fn with argument and return type

# def sum(n1,n2):
#     sum=n1+n2
#     return sum
# data=sum(10,20)
# print(data)
# data1=sum(20,30)
# print(data1)

def dif(n1,n2):
    diff=n1-n2
    return diff
data=dif(20,10)
print(data)
data1=dif(30,10)
print(data1)