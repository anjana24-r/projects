#reduce()


import functools
# lst=[7,8,9,4,3,2]
# total=functools.reduce(lambda no1,no2:no1+no2,lst)
# print(total)
# highest=functools.reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
# print(highest)

#list comprehension
#........
# lst=[1,2,3,4,5]
# sq=[num**2 for num in lst]
# print(sq)

# fruits=["apple","orange","mango"]
# pairs=[(fruit,fruit) for fruit in fruits]
# print(pairs)
#
# l1=[10,20]
# l2=[30,40]
# p=[(n1,n2) for n1 in l1 for n2 in l2]
# print(p)

# l1=[1,2,3,4,5,6]
# evens=[num for num in l1 if num%2==0]
# print(evens)

lst=[7,8,9,4,3,2]
op=[num+1 if num>5 else num-1for num in lst]
print(op)