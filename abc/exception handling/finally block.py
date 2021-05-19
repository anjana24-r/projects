
x=int(input("enter a number"))
y=int(input("enter a number"))
try:
    print(x/y)
except:
    print("zero division error")
finally:
    print("finaly block")

