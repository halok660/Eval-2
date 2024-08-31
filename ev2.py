def addi(dict):
    name=input("Enter name ")
    id=int(input("enter ID "))
    dict[name]=id
    
def upd(dict):
    name=input("enter name")
    id=int(input("entr id"))
    if name in dict:
        dict[name]=id
    
def dele(dict):
    name=input("Enter name ")
    if name in dict:
        dict.pop(name)
    
    
def shows(dict):
    print(dict)

def search(dict):
    name=input("enter name")
    id=int(input("entr id"))
    if name=='0':
        if id in dict:
            print("true")
        else:
            print("false")
    else:
        if name in dict:
            print("true")
        else:
            print("false")

    



dict={}
i=int(input("Enter input"))
while i != -11:
    if i==1:
        addi(dict)
    elif i==2:
        upd(dict)
    elif i==3:
        search(dict)
    elif i==4:
        shows(dict)
    
    i=int(input("Enter i"))
