#a="hello world"
# for st in a:
#     print(st)

# present or not
#..........


# a="hello world"
# flag=0
# b=input("type here")
# for i in a:
#     if i==b:
#         flag=1
# if flag==1:
#         print("present")
# else:
#     print("not present")

#in and not in
#..........

# a="abcd"
# b="abjhuyrt"
# for i in a:
#     if i not in b:
#         print(i)

#..move unique elements

# a="helloo"
# b=""
# for i in a:
#     if i not in b:
#       b+=i
# print(b)


#count the element
#.....

# a=input("enter string")
# b=input("enter element to count")
# count=0
# for i in a:
#     if i in b:
#         count += 1
# print("count is",count)

#count vowels
#.......
# a=input("enter the string")
# count=0
# for i in a:
#     if i in "AEIOUaeiou":
#         count+=1
# print("count of vowels in ",a,"is=",count)

#remove punctiations
#....................
# p=";!@#$%<>{}\\,"
# a=input("enter a string")
# no_p=""
# for char in a:
#     if char not in p:
#         no_p=no_p+char
# print(no_p)

#calculator operations
#...........
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select operations")
print("1.Add")
print("2.subtraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("enter the choice")
    if choice in('1','2','3','4'):
        num1=float(input("enter a number"))
        num2=float(input("enter a number"))
        if choice=='1':
            print(add(num1,num2 ))
        elif choice=='2':
            print(sub(num1,num2))
        elif choice=='3':
            print(mul(num1,num2))
        elif choice =='4':
            print(div(num1,num2))
        break
    else:
        print("invalid")

