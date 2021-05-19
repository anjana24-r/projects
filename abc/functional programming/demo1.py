a = [9,5]
# print[id(x)]
# for x in a:
  # print (a)

for i in range(len(a)):
    a[i] += 1  # creates new integer, but updates mutable list

# print[id(x)]
for x in a:  # references are changed.
      print (a)
