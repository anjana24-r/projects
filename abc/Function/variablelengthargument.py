# def add(*args):
#     res=0
#     for num in args:
#         res+=num
#     return res
# print(add(10,20,30,40))


# def print_employee(**kwargs):
#     for k,v in kwargs.items():
#         print(k,"=>",v)
#
# print_employee(id=100,place="thrissur",job="kakkanad")
#
# def print_employee(**abc):
#     for k,v in abc.items():
#         print(k,"=>",v)
#
# print_employee(id=100,place="thrissur",job="kakkanad")

# def print_employee(**kwars):
#     print(kwars)
# print_employee(id=1000,name="ammu",salary=5000)

employees={
    1000:{"eid":1000,"name":"ammu","salary":25000,"des":"dev"},
    1001:{"eid":1001,"name":"arun","salary":22000,"des":"dev"},
    1002:{"eid":1002,"name":"ram","salary":26000,"des":"qa"},
    1003: {"eid": 1003, "name": "rami", "salary": 26000, "des": "qa"},
}

def print_employee(**kwars):
    id=kwars["id"]
    prop=kwars["prop"]
    if id in employees:
         print(employees[id]["name"])
         print(employees[id][prop])
    else:
        print("invalid id")



print_employee(id=1001,prop="salary")