# import re
# n="hello"
# x='\w*'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re
n="57kg"
x='\d{2}[a-z]{2}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
