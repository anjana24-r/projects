import re
n=input("enter a string")
x='(^a[a-zA-Z0-9\W]*b$)'   # *ab 0 refers to nothing can come
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")