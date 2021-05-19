#to store element
#push - add elements to stack (end of stack)
#pop - delete elements from stack(top of stack)
#LIFO - last in first out

stk=[]
size=int(input("enter the size"))
top=0
n=0
def push():
    global top,size
    if top>=size:
        print("stack is full")
    else:
        p=int(input("enter the element to push"))
        stk.append(p)
        top+=1
        print(stk)
def pop():
    global top,size
    if top<=0:
        print("stack is empty")
    else:
        stk.pop()
        top-=1
        print(stk)
while n!=1:
    print("enter operation want to perform")
    opt=int(input("press::1)push 2)pop"))
    if opt==1:
        push()
    elif opt==2:
        pop()