f=open("/home/ubuntu/Downloads/Temperature","r")
lst=[]
dic={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    if(data[0] not in dic):
        year=data[0]
        dic[year]=data[1]
    else:
        year=data[0]
        temp=int(data[1])
        if(int(dic[year])<temp):
            dic[year]=str(temp)
for i in dic:
    print(i,":",dic[i])


