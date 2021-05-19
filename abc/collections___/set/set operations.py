#union
#intersection
#difference

st1={1,2,3,4,5}
st2={4,5,6,7,8}

#union  - combine both sets by removing duplicates in it

st3=st1.union(st2)
print(st3)

#intersection - display common elements from both the sets

st4=st1.intersection(st2)
print(st4)

#differnce - element present in set1 not in set2(set1 - set2)

st5=st1.difference(st2)
print(st5)

