#pattern matching

#mail id,phn no -uses of pattern matching

#re --package for matching

#pgm for searching ab in ababbaa-finditer

# import re
# count=0
# matcher = re.finditer('ab','ababaaa')   #matcher variable name
# for match in matcher:
#     count+=1
# print("count=",count)

import re
count=0
matcher = re.finditer('ab','ababaaa')   #matcher variable name
for match in matcher:
    print("match available at",match.start())  #return positions
    print("group=",match.group())   #which object find match
    count+=1
print("count=",count)
