#functional programming

#used to reduce length of a code

#they are:-

#1.lambda functon

#2.map fn

#3.filter

#4.list comprehension

#....

#1.lambda function
#.....

#they are anonymous fn(nameless fn)
#
# def add(n1,n2):
#    return n1+n2
# print(add(10,30))

#use lambda fn
#
# f=lambda n1,n2 :n1+n2
# print(f(1,2))


#2.map
#..........
#every object we do operation to get a output (every object need an output then we use map fn)

#eg: lst=[10,20,30,40] ==>f(x) [100,400,900,1600]
 #[ab,cd,ef,gh,ij] ==>f(x) [AB,CD,EF,GH,IJ]  #for convert each lower case to upper

#3.filter
#....

#filter use to get an output based on a specific condition (operation is not performed to every object)

#[1,2,3,4,5,6,7,8,9,10] ==>f(x)=[2,4,6,8,10]    (filter only even no.)

#[ab,cd,ef]==>f(x)=[ab]  #start with a only


#syntax
#......

#map
#.......

#map(fn,iterable)

#filter
#..

#filter(fn,iterable)

#eg:square of every no. in the below list

#lst=[1,2,3,4,5,6,7]
# def sq(n1):
#     return n1*n1
#
# s=list(map(sq,lst))  #lst iterable  o/p should be list so list(map.....)

# print(s)

#above prgrm using lambda

# lst=[1,2,3,4,5,6,7,8,9,10]
# s=list(map(lambda num:num*num,lst))
# print(s)

#filter
#...

#finding even no. from below list

# lst=[1,2,3,4,5,6,7,8,9,10]
# def even(n1):
#     return n1%2==0
# ev=list(filter(even,lst))
# print(ev)

#using lambda

# s=list(filter(lambda n1:n1%2==0,lst))
# print(s)

#...................

#1 to 50

# lst=[]
# for i in range(1,51):
#     lst.append(i)
# print(lst)

#list comprehension

# lst=[i for i in range(1,51)]
# # print(lst)

#map function
#...........
# lst=[2,3,4,5,6,7]
# squares=list(map(lambda num:num**2,lst))
# print(squares)

# names=["ammu","anjana"]
# upp=list(map(lambda name:name.upper(),names))
# print(upp)


