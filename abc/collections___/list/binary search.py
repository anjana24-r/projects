#Binary search

#Algorithm
#.........

#list=[2,4,7,1,5]

#1. sort the given array
#list=[1,2,4,5,7]

#2. low=0

#upper=len(list)-1

#3.calculate mid of list
#mid=low+upper//2    (mid=0+4=4 4//2 =2) (mid = 2)

#4.condition
#...

#* mid<search element   then  low=mid+1
#* mid>serch element    then  upper=mid-1
#* mid=search element   then  element found(element=list[mid]

lst=[2,5,1,6,7,4]
lst.sort()
print(lst)
low=0
upp=len(lst)-1
flag=0
element=int(input("enter the element to be search"))
while(low<=upp):
    mid=(low+upp)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=1

if(flag>0):
    print("element found")
else:
    print("not found")


