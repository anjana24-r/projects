employees=[
{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
{"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
{"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
{"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
{"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},

]
#print employee names

# emp_names=list(map(lambda emp:emp["name"],employees))
# print(emp_names)

#print employee salary


#
# emp_sal=list(map(lambda emp:emp["salary"],employees))
# print(emp_sal)

# enames=[emp["name"] for emp in employees]
# print(enames)
dev=[emp for emp in employees if emp["designation"]=="developer"]
print(dev)
sal=max([emp["salary"] for emp in employees])
print(sal)