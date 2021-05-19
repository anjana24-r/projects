#linear search
#............

list=[1,2,3,4]
a=int(input("enter element to be search"))
flag=0
for i in list:
    if (i==a):
        flag=1
        break

    else:
       pass
if (flag>0):
    print("element found")
else:
    print("not found")

#drawback - complexity