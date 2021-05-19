#tuples
#...........
 #property 1

# tp=()
# print(type(tp))

# tp=tuple()       #using function

#property 2  #support heterogeneous data

tp1=(1,10,5,"ammu",True,False)
print(tp1)

#property 3   #insertion order preserved
#..........

tp2=(1,2,3,4,5,6,7,8,"ammu",True,False)
print(tp2)

#property 4   #support duplicate values
tp3=(1,2,2,3,4,55,5,"ammu,True,False")
print(tp3)

#property 5    #immutable
# tp3(2)=3
print(tp3)