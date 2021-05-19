
#x='a+'  a including group ( a must be there)
#x='a*' count including zero no. of a
#x='a?' count a as each including zero no.of a
#x='a{2}' no.of position(2 position here)
#x='a{2,3} min 2a and max 3a
#x='^a'  check starting with a
#x='a$'  check ending with a


#x='a+'
#....

# import re
# x="a+"
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x='a*'
#........

# import re
# x="a*"
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x='a?'
#.........

# import re
# x="a?"
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x='a{2}'
#....

# import re
# x="a?"
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x='a{2,3}
#..........

# import re
# x="a{2,3}"
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x='^a'
#......

# import re
# x="^a"   #whole string consider
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#x='a$'
#......

import re
x="a$"
r='aaa abc aaaa cga'
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())