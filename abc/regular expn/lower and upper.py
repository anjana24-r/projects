import re
n=input("enter a string")
x="([a-zA-Z]+\d{1}$)"    # $ is used to represent end
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")


