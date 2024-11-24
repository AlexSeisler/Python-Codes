#Pascals Triangle
def Pascals(x):
    global ans
    #sets base
    if x==0:
        return [[1]]
    #runs unless base number is reached
    else:
        # sets a new list to the base to build off of
        new=[1]
        #sets a variable to the previous functions numbers
        ans=Pascals(x-1)
        #sets a variable to the last number in that variable
        last=ans[-1]
        #Loops through the previous set of numbers 
        for i in range(len(ans)-1):
            #sets another variable to the number and the next number in the sequence 
            num=last[i]+last[i+1]
            #adds it to the list
            new.append(num)
        #adds the ending 1 onto the list
        new.append(1)
        #adds the completed list to the end list
        ans.append(new)
        #returns the final result
        
        return ans


fib=[1,1]
for i in range(1000):
    fib.append(fib[i]+fib[i+1])


user=int(input("Amount: "))
Pascals(fib.index(user))
list1=[]
y=fib.index(user)
x=0

for i in range(fib.index(user)):
    try:
        list1.append(ans[y][x])
        y=y-1
        x=x+1
    except:
        break
odd=0
even=0
largest=-9999
for i in range(len(list1)):
    if list1[i]%2==0:
        even=even+1
    if list1[i]%2==1:
        odd=odd+1
    if list1[i]>largest:
        largest=list1[i]
print(str(odd)+" "+str(even)+" "+str(largest))