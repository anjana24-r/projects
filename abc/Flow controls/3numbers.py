n1=int(input("enter num1"))
n2=int(input("enter num2"))
n3=int(input("enter num3"))
if(n1>n2) & (n1>n3):
    print(n1,"is greater")
elif(n2>n1) & (n2>n3):
    print(n2,"is greater")
else:
    print(n3,"is greater")
