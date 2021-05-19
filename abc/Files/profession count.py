f=open("/home/ubuntu/Downloads/customer","r")
dic={}

for lines in f:
    #pcount = data[-2]
    data=lines.rstrip("\n").split(",")
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
for k,v in dic.items():
    print(k,",",v)




