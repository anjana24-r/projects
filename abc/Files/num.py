f=open("numbers","r")
lst=[]

for num in f:
    lst.append(int(num.rstrip("\n")))
print(lst)

print(sum(lst))

#to remove end char use rstrip
#int(num.rdtrip......to get sum it will treat as num else string)
#lstrip - to remove first char

data="hi"
d1=data.lstrip("h")
print(d1)

