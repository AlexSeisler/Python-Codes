"""
This code is a function using the bubble sort method and demonstrating how it 
works. Bubble sort is a method that loops through every element of a list 
and compares each element to the next element in the list. If it is 
greater than the next element they swap otherwise continue.It loops back to 
the start of the list until no more comparisions return false and breaks out 
of the loop returning the sorted list.
"""
def bubble(listed):
    count=1
    #while loop to keep going until no comparisions are made
    while count>0:
        count=0
        #loops through each element in the list
        for i in range(len(listed)-1):
            #compares the current elment to the next element if the next element is greater it continues
            if listed[i]<=listed[i+1]:
                continue
            #otherwise it flips the two indexs and adds 1 to count
            else:
                current=listed[i]
                future=listed[i+1]
                listed[i+1]=current
                listed[i]=future
                count=count+1
        #prints each iteration
        print(listed)
    return ("Final: "+str(listed))


print(bubble([3,18,80,9,14,12,2,18,16]))
print()
print(bubble([1,2,3,4,5,6]))
print()
print(bubble([7]))
print()
print(bubble([6,6,5,4,4,3,2,2,1]))
print()
print(bubble([-3,8,-2,0,9,3,0,2]))