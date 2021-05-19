#x='[abc]' either a b or c
#x='[^abc]' excepta b c
#x='[a-z]' a to z
#x='[A-Z]' - A to Z
#x='[a-zA-Z]' both lower and upper case
#x='[0-9]' check digits
#x='[^a-zA-Z0-9]' special symbols only
#x='\s' check space
#x='\d' check digits
#x='\D' except digits
#x='\w' all words except special characters
#x='\W' for special characters

#examples
#....

#x='[abc]'
#...

import re
x='[abc]'
matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
for match in matcher:
    print(match.start())
    print(match.group())

#except abc
#...........

# import re
# x='[^abc]'
# matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())


#a to z
#........

#
# import re
# x='[a-z]'
# matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())

#A-Z
#.....

# import re
# x='[A-Z]'
# matcher=re.finditer(x,"abtA%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())

#[a-zA-Z]
#.....
#
# import re
# x='[a-zA-Z]'
# matcher=re.finditer(x,"abtA%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())

#[0-9]
#....

# import re
# x='[0-9]'
# matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())

#[^A-Za-z0-9]
#......

# import re
# x='[^A-Aa-z0-9]'
# matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())

#\s -check space
#....

# import re
# x='\s'
# matcher=re.finditer(x,"abt c%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())

#\d  -check digits
#.....


# import re
# x='\d'
# matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())

#\D - except digits
#......

# import re
# x='\D'
# matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())
#

# '\w -ONLY WORDS EXCEPT SPECIAL CHARACTER
#........

# import re
# x='\w'
# matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())

#'\w' - SPECIAL CHARACTERS
#....

# import re
# x='\W'
# matcher=re.finditer(x,"abtc%67")   #0-a,1-b,3-c
# for match in matcher:
#     print(match.start())
#     print(match.group())



