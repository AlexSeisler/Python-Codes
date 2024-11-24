def Password(string,multiple):
    answers=[]
    fullstring=""
    count=0
    for i in range(multiple):
        fullstring=fullstring+string
    
    for j in range(len(fullstring)):
    
        for i in range(len(fullstring)):
            count=count+1
            if fullstring[i] in answers:
                m=0
            else:
                answers.append(fullstring[i])
            if fullstring[i:i+count] in answers:
                m=0
            else:
                answers.append(fullstring[i:])
            
            if fullstring[:i] in answers:
                m=0
            else:
                answers.append(fullstring[:i])
            if fullstring[i+j:i+count] in answers:
                m=0
            else:
                answers.append(fullstring[i+j:i+count])
    return len(answers)
    
    
    
    
    
    
user=input("string multiple:    ")
user=user.split(" ")
print(Password((user[0]),int(user[1])))