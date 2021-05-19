low=int(input("enter lowlimit"))
up=int(input("enter uplimit"))
sum=0
avg=0
for i in range(low,up+1):
    sum=sum+i
    avg=(sum/i)
print("sum=",sum)
print("avg=",avg)