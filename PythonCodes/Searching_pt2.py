"""
This code creates 3 functions two main ones that use the methods of Binary searching and
linear search then the third is to create a randomly generating list to the inputted size.
These functions are used in the main program to demenstrate the efficency of the different
search methods.
"""
#Imports the random module
import random
#A function using the Linear Searching method
def LinearSearch(UnsortedCompleteList,Item):
    try:
        #sorts the list (not needed
        CompleteList=sorted(UnsortedCompleteList)
        #initilizing variables
        checker=0
        count=0
        #A for loop used to loop through the list
        for i in range(len(CompleteList)):
            #adds one to count every action to tally comparisons made
            count=count+1
            #if Item is equal to checker variable the item is found and returned
            if CompleteList[i]==Item:
                checker=1
                return count
        #if not found returns -1
        if checker==0:
            return count
    except:
        return count
#A function using the Binary search method
def BinarySearch(UnsortedCompleteList,Item):
    try:
        #Sorts the list
        SortedCompleteList=sorted(UnsortedCompleteList)
        #Initilizes variables
        count=0
        #Sets low and high index counts
        low=0
        high=len(SortedCompleteList)
        if Target>high:
            return count
        #while loop to keep going until the entire list is disregarded or broken out of
        while low<=high:
    
            #Sets the checkValue variable to the middle index of the list
            middle=(low+high)//2
            checkValue=SortedCompleteList[middle]
    
            #Checks this variable actions as needed
            if checkValue==Item:
                count=count+1
                return count
            elif checkValue>Item:
                count=count+2
                high=middle-1
            else:
                count=count+3
                checkValue<Item
                low=middle+1
        return count
    except:
        return count
#A random list generator set to the users liking
def ListGenerator(ListSize):
    #Creates a list numerically to the users input
    list1=[]
    for i in range(1,ListSize+1):
        list1.append(i)
    #Gets a random number from this list setting it to the target
    global Target
    Target=random.choice(list1)
    Endlist=[]
    #Loops through the users amount and adds a random number 1-user to a list
    for i in range(ListSize):
        Endlist.append(random.choice(list1))
    Endlist=sorted(Endlist)
    #returns the entire new list
    return Endlist
endLinear=[]
endBinary=[]
#Users input
user=int(input("Enter the list size: "))
for i in range(50):
    UserList=ListGenerator(user)
    endLinear.append(LinearSearch(UserList,Target))
    endBinary.append(BinarySearch(UserList,Target))
endLinearCount=0
endBinaryCount=0
for i in range(50):
    endLinearCount=endLinearCount+endLinear[i]
    endBinaryCount=endBinaryCount+endBinary[i]
endLinearCount=endLinearCount/50
endBinaryCount=endBinaryCount/50 
print("Linear Average: "+str(endLinearCount))
print("Binary Average: "+str(endBinaryCount))