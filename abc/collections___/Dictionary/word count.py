# word count=each word how much times it read

line="hai hello hai hello"
#hai=2
#hello=2

#split fn = to collect word

words=line.split(" ")
# print(words)

dic={}
for word in words:
    if(word not in dic):
        dic[word]=1
    else:
        dic[word]+=1
print(dic)
