f=open("news cut","r")
dic={}
for lines in f:
    data=lines.rstrip("\n").split(" ")

    for word in data:
        if(word not in dic):
            dic[word]=1
        else:
            dic[word]+=1
for k,v in dic.items():
    print(k,",",v)
#print(dic)