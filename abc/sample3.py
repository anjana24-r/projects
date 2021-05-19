evensum=0
oddsum=0

def find_sum(num,i):

    num = num+i
    return num

for i in range(1,101):
    if((i%2)==0):
        evensum = find_sum(evensum,i)
    else:
        oddsum = find_sum(oddsum,i)


print("evensum=",evensum)
print("oddsum=",oddsum)

