dic={"empid":"1","name":"ammu","desig":"soft eng","salary":"10000"}
print(dic["name"])
print("company" in dic)

dic["company"]="abc"
print(dic)

dic["salary"]=15000
print(dic)

for i in dic:
      print(i,":",dic[i])
