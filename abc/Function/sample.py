#import Function.abc123
# addition=Function.abc123.sum(5,6)
# print(addition)
# subt=Function.abc123.sub(20,10)
# print(subt)
# m=Function.abc123.mul(2,3)
# print(m)
# d=Function.abc123.div(20,10)
# print(d)


#syntax
#..........

#import package.module

#variable=package.module.fname(argument)

# import Function.cube
# abc=Function.cube.cube(2)
# print(abc)

#to recover from this drawback(we can print all from modules)
#...........

from Function.abc123 import*    # * - from all
addi=sum(20,30)
print(addi)
subi=sub(20,5)
print(subi)
m=mul(2,3)
print(m)
d=div(90,45)
print(d)

