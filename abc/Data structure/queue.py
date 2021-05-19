#FIFO - first in first out
#enqueue - to add element
#dequeue - to delete from queue
que=[]
size=int(input("enter the size"))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que
    if rear>=size:
        print("queue is full")
    else:
        p=int(input("enter the element to be insert"))
        que.insert(rear,p)
        rear+=1
        for i in range(front,rear):
            print(que[i])
def delete():
    global front,rear,size,que
    if rear==front:
        print("queue empty")
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])
while n!=1:
    print("enter operation")
    opt=int(input("1)insert\n2)delete"))
    if opt==1:
        insert()
    elif opt==2:
        delete()