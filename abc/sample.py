low = int(input("enter lower limit"))

up = int(input("enter upper limit"))

check = int(input("enter a number"))
count = 0
for i in range(low, up + 1):
    if (i % check == 0):
        count = count + 1

print(count)

#

# def countDivivsibles(A,B,M):
#     if(A%M==0):
#         return((B/M) - (A/M)) + 1
#     p
