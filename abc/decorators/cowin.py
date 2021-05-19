def vaccination_portal(**kwargs):
    true=0
    false=0

    # print("request is allowed location ekm")
name=input("enter a name")
age=int(input("enter age "))
address=input("enter address")
health_issues=str(input("enter true/false"))
if (age>=25 or health_issues=="true"):
    print("request is allowed location ekm")
else:
    pass




#age above 65 or health issues = true allowed