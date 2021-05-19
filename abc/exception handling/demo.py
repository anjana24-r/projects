# a=int(input("enter a number"))
# b=int(input("enter a number"))
# #print(a/b)
#
#
# #5/0 --> zero division error
# #to solve unexpected error - error handling
# #An exception is a Python object that represents an error.
#
# try: #chance of exception is in try
#     print(a/b)
#
# except:#if error comes what to do
#
#     print("exception occurs")
#try block always work
#except:- if ecception occur in try what want to print

#index out of range error
#...............

# a=[1,2,3]
# #print(a[6])
# b=int(input("enter an index"))
# try:
#     print(a[b])
# except:
#     print("index error occured")

#finally block
#.................

#content will work all the time


a=[1,2,3]
#print(a[6])
b=int(input("enter an index"))
try:
    print(a[b])
except:
    print(" index error occured")
finally:
    print("inside finally")

#try and finally work all the time but except work only if exception occur

