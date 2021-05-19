# f=open("sample","r")
# #if we are reading from diff dir then absolute copy ,else give copy path
# for lines in f:
#     print(lines)
f=open("/home/ubuntu/Downloads/wget-log.1","r")
for l in f:
    print(l)