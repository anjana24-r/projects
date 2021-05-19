low=int(input("enter lower limit"))
up=int(input("enter up limit"))
evensum=0
oddsum=0
for i in range(low,(up+1)):
             if(i%2==0):
                evensum+=i
             else:
                 oddsum+=i
print(evensum)
print(oddsum)
