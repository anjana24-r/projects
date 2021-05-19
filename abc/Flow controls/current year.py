cy=int(input("enter current year"))
cm=int(input("enter current month"))
cd=int(input("enter current date"))
by=int(input("enter born year"))
bm=int(input("enter born month"))
bd=int(input("enter born date"))
if(bd==cd) & (bm==cm):
    age=cy-by
    print(age,"years old")
else:
    cy-=1
    age=cy-by
    print(age)
