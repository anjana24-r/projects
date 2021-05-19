# lst=[7,8,9,4,3,2]
#print list of even numbers
# evens=list(filter(lambda number:number%2==0,lst))
# print(evens)

#filter out number>5

# nums=list(filter(lambda number:number>5,lst))
# print(nums)

employees=[
{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
{"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
{"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
{"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
{"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"},
]

#print all employees designation==developer



# dev=list(filter(lambda emp:emp["designation"]=="developer",employees))
# dev_names=list(map(lambda emp:emp["name"],dev))
# print(dev_names)
