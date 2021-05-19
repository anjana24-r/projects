f=open("/home/ubuntu/Downloads/customer","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
    fname=data[1]
    em=data[4]
    age=data[3]
    cou=data[-1]
    lst=([fname,age,cou])
    for i in lst:
        if(em=='doctor'):
             print(lst)
        else:
             pass
