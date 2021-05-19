
sex=input("enter ur sex (M/F) : ")
age=int(input("enter ur age"))
ms=input("enter ur ms (yes/no) : ")
if(sex=='F'):
    print("work only in urban areas")
elif(sex=='M') & (age>=20 and age<=40):
    print("work anywhere")
elif (sex=='M') &  (age>=40 and age<=60):
    print("work urban")
else:
    print("error")

