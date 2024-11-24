""" #1. Memoization is used when making a recursive function, a recursive 
function repeats every possible calculation until it gets to its base 
case to then solve the answer. When using memoization we can change 
how the recursive function finds its data. This is done with a 
dictionary where we store all the recursive functions calculations 
only making it need to calculate each set one time. This allows the 
recursive function to run with a lot bigger numbers and break down the 
time it will take to complete the recursive function.
"""
user=input("1:Fibinacci or 2:Pascals")
user1=int(input("How many times: "))
user2=int(input("What input number: "))
if user== "1":
    for i in range(user1):
        #fibinacci
        dicfib={}
        value=0
        def fib(n):
            if n in dicfib:
                return dicfib[n]
            if n==1:
                value=1
            elif n==2:
                value=2
            elif n>2:
                value =  fib(n -1)+fib(n -2)
            dicfib[n] = value
            return value
        print(fib(user2))
elif user=="2":
    for i in range(user1):
        #pascal
        dicpas={}
        end=[[1]]
        def triangle(n):
            if n in dicpas:
                return dicpas[n]
            if n == 0:
                return []
            elif n == 1:
                return [1]
            else:
                new_row = [1]
                last_row = triangle(n-1)
                for i in range(len(last_row)-1):
                    new_row.append(last_row[i] + last_row[i+1])
                new_row += [1]
            dicpas[n]=new_row
            end.append(new_row)
            return new_row
        triangle(user2)
        print (end)