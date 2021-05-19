#nested if
#................................

n1=int(input("enter num1"))
n2=int(input("enter num2"))
n3=int(input("enter num3"))
if(n1>n2) & (n1>n3):
    if(n2>n3):
       print(n2,"is second largest")
    else:
        print(n3,"sec lar")
elif(n2>n3) & (n2>n1):
    if(n1>n3):
        print(n1,"sec lar")
    else:
        print(n3,"sec lar")
elif(n3>n1) & (n3>n2):
     if(n1>n2):
         print(n1,"sec lar")
     else:
         print(n2,"sec lar")