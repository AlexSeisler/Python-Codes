"""This code takes the game of hanoi towers and solves it 
using recursive functions."""


#Sets a function using four parameters x which is the size of the 
#tower then 3 other paremeters a,b,c which represent the three pegs 
#of the board
def hanoi(x,a,b,c):
    #sets a base case that if x equals 1 it returns the smallest pegs move 
    if x==1:
        print("move "+str(x) + " from  "+ str(a)+" to "+str(c))
        return
    #Moves the towers size minus one to the next peg using the last peg as a alternative
    hanoi(x-1,a,c,b)
    print("move "+str(x)+" from "+str(a)+" to "+str(c))
    hanoi(x-1,b,a,c)
#asks the user for an input which is the size of the hanoi tower
user=int(input("What is the size?: "))
#Calls the tower function using Left Middle and Right for my tower pegs
hanoi(user,"L","M","R")