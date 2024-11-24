"""
This code is a mix of 4 different functions, each do their own thing. 
A summation, Factorial, Fibbonaci, and a Pascals Triangle 
function. Each have a set ending variable and elif else 
statment to keep calling the function until the value reaches 
the base value then returns the ending answer.
"""
#Base variable of 1 otherwise it subtracts one from the starting number adding itself to the total
#Summation
def summation(x):
    if x==1:
        return x
    else:
        return summation(x-1)+x
#Prints multiple cases of the summation function
print("Summation of 5: "+str(summation(5)))
print("Summation of 7: "+str(summation(7)))
print("Summation of 10: "+str(summation(10)))
#Base variable of 1 otherwise it subtracts one from the starting number multiplying itself to the total
#factorial
def factorial(x):
    if x==1:
        return x
    else:
        return factorial(x-1)*x
#Prints multiple functions of the factorial function
print("Factorial of 5: "+str(factorial(5)))
print("Factorial of 7: "+str(factorial(7)))
print("Factorial of 10: "+str(factorial(10)))

#Has a base value of one then any other number till then adds the previous two numbers together and adds it to the sequence
#fibbonaci
def fib(x):
    if x<=1:
        return x
    else:
        return (fib(x-1) + fib(x-2))

#Prints multiple cases of the fib function
print("Fibbinacci of 5: "+str(fib(5)))
print("Fibbinacci of 7: "+str(fib(7)))
#Loops through the function 15 times and prints the 15 numbers of fibbanaci
print("Fibbinacci numbers 1-15: ")
for i in range(15):
    print("#"+str(i+1)+": "+str(fib(i)))


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
print("Pascal of 7: "+str(Pascals(7)))
print("Pascal of 10: "+str(Pascals(10)))
print("Pascal of 15: "+str(Pascals(15)))