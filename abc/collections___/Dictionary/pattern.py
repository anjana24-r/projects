pattern="ABCDBCA"
for char in pattern:
    print(char)
dic={}
for char in pattern:
    if(char not in dic):
        dic[char]=1
    else:
        print("first recursive chAr",char)
        break