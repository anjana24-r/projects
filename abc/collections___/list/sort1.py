#sort without using function
numlist=[]
num=int(input("no of list elements"))
for i in range(1,num+1):
    value=int(input("enter value of elements: " ))
    numlist.append(value)
for i in range(num):
    for j in range(i+1,num):
        if(numlist[i]>numlist[j]):
            temp=numlist[i]
            numlist[i]=numlist[j]
            numlist[j]=temp

print("after sorting:",numlist)