def is_member(value, iterable):
    for item in iterable:
        if value is item or value == item:
            return True
    return False
#12
A=""
B="PLEASEEXCUSEMYDEARAUNTSALLY"
for i in range(len(B)-1):
    if B[i]==B[i+1]:
        A=A+B[i]
    if B[i]=="A"or B[i]=="E":
        A=B[i]+A
print("#12: "+str(A))
#AAAEEEEAEEL


#24
N=""
M=""
A="MISSISSIPPIMISSOURIRIVERS"
for i in range(0,len(A)-1,2):
    if A[i]==A[i+1]:
        N=N+A[i]
    if A[i]>A[i+1]:
        N=N+A[i+1]+A[i]
for j in range(len(N)):
    if ((N[j]>"E")and N[j]<="M"):
        M=M+N[j]
list1=[]
for t in range(len(M)):
    if is_member(M[t],list1)==False:
        list1.append(M[t])
    else:
        continue
    
print("#24: "+str(len(list1)))
#IMI==2

#28
N=""
M=""
A="UNITEDSTATESSPACEANDROCKETCENTER"
for i in range(len(A)-1):
    if A[i]!="E"or A[i]!="S":
        N=N+A[i]
for i in range(0,len(N)-1,2):
    if N[i]>N[i+1]:
        M=M+N[i+1]
    else:
        M=M+N[i]

list1=[]
for t in range(len(M)):
    if is_member(M[t],list1)==False:
        list1.append(M[t])
    else:
        continue  
print("#28: "+str(len(list1)))

#32
N=""
M=""
A="BASEBALLFOOTBALLBASKETBALL"
for i in range(len(A)):
    try:
        if A[i]!=A[i+1]:
            N=N+A[i]
    except:
        continue
for i in range(len(N)):
    if N[i]>"B":
        M=M+N[i]
list1=[]
for t in range(len(M)):
    if is_member(M[t],list1)==False:
        list1.append(M[t])
    else:
        continue 
print("#32: "+str(len(list1)))
#Extra
#36
N=""
A="NORTHHAVENHIGH"
B="CONNECTICUTUSA"
M=""
for i in range(len(A)):
    if A[i]<B[i]:
        N=N+A[i]
    else:
        N=N+B[i]
for i in range(len(N)):
    if N[i]>"C":
        M=M+N[i]
print("#36: "+str(len(M)))