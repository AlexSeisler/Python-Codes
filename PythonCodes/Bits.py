user=input("Input: ")
user=user.split(",")
string=user[0]
checklist=[]
checklist.append(string)
amount=int(user[1])
user.pop(0)
user.pop(0)
endlist=[]
answer=[]
while True:
    if len(checklist)==0:
        break
    else:
        string=checklist[0]
        
        if string.count("*")>=2:
            for i in range(len(string)):
                if string[i]=="*":
                    fill0=string[:i]+"0"+string[i+1:]
                    fill1=string[:i]+"1"+string[i+1:]
                    checklist.append(fill0)
                    checklist.append(fill1)
            checklist.pop(0)
        elif string.count("*")==1:
            for i in range(len(string)):
                if string[i]=="*":
                    fill0=string[:i]+"0"+string[i+1:]
                    fill1=string[:i]+"1"+string[i+1:]
                    endlist.append(fill0)
                    endlist.append(fill1)
                    checklist.pop(0)
        elif string.find("*")==-1:
            endlist.append(string)
            checklist.pop(0)
            
        for i in range(amount):
            if user[i] in endlist:
                answer.append(user[i])
if len(answer)==0:
    print("NONE")
else:
    answer=(set(answer))
    answer=", ".join(answer)
    print(answer)