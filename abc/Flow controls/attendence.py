held=int(input("number of classes held"))
att=int(input("attendence"))
per=(att/held)*100
if(per>=75):
    print("allowed")
else:
    print("not allowed")
