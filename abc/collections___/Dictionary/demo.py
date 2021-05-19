#Dictionary
#..........

#property 1 - how to define

dic={}

#value is stored in dictionary by "key-value pairs".

#key-value pairs
#..........

#name:luminar,loc:Kakanad,course:python

#key:name,loc,course
#value:luminar.Kakanad,python

# dic={"name":"luminar","loc":"kakanad","couse":"python","marks":100,"data":10.70}
# print(dic)

#property 2 support heterogeneous data
# eg: refer above dic

#property 3 - insertion order preserved
#eg:refer above example dic

#property 4 - doesn't support duplicate key but suppport duplicate value i.e it print kakanad(value) but not age(key)

dict={"name":"luminar","loc":"kakanad","age":22,"marks":30,"place":"kakanad"}
# print(dict)

#property 5 - mutable

# value is collected by it's corresponding key
# print(dict["name"])
# print(dict["loc"])

#iterate key value pairs

# for i in dict:
#      print(i,":",dict[i])

#MUTABLE
#....
# dict["age"]=40
# print(dict)
# dict["marks"]=50
# print(dict)
# dict["marks"]+=50
# print(dict)

#for DELETING USE DEL

del dict["name"]
print(dict)

#pop


#total 150

#we have to check the key total in the dict
print("total" in dict)

#add to the list
dict["total"]=150
print(dict)


