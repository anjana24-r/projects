# def factorial():
#
#     n=int(input("enter a number"))
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
# factorial()

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial(3)
#
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# number=int(input("enter a number"))
# res=factorial(number)
# print("fact=",res)