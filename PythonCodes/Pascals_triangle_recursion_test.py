#Pascals Triangle
def Pascals(x):
    #sets base
    if x==0:
        return [1]
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
#Prints multiple cases of Pascals function
total=[1]
User=int(input("Amount: "))
for i in range(User):
    
    total.append(x)
print("Pascal of 7: "+str(Pascals(User)))