# lst=[['1001',"ammu",22,1000],
#      ['1002',"anjana",23,2000],
#      ['1003,"arun',24,3000]]
# print(lst)                    #nested list


# lst=[['1001',"ammu",22,1000],
#      ['1002',"anjana",23,2000],
#      ['1003,"arun',24,3000]]
# for i in lst:
#       print(i)               #iterate each one


# lst=[['1001',"ammu",22,1000],
#      ['1002',"anjana",23,2000],
#      ['1003,"arun',24,3000]]
# for i in lst:
#       print(i[1])               #print only employee names


lst=[['1001',"ammu",22,1000],
     ['1002',"anjana",23,2000],
     ['1003,"arun',24,3000]]

#for i in lst:
#     if(i[3]>2000):
#            print(i[1])
#            sum=0
for i in lst:
    sum=0
    sum=sum+i[3]
