import re
n=input("enter phno")
x='[+][9][1]\d{10}$'    # $ is used to represent end
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")             