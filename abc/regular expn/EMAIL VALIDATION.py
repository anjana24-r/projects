import re
n=input("enter a string")
x="([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")