"""
This code demonstrates the raw method of selection sorting
"""

#Sets a Sort function taking in one parameter, a list of numbers 
def Sort(lists):
    #prints used to display input to user
    print("Start: "+str(lists))
    #keeping a variable used to track the indexs used already
    count=0
    #A nested for loop to loop through each iteration of the list
    for j in range(len(lists)):
        #initializes the lowest variable with a very high number
        lowest=9999
        for i in range(count,len(lists)):
            #for each item in the list it checks it towards the lowest variable 
            #if the items lower sets the new value keeping track of the index
            if lists[i]<lowest:
                lowest=lists[i]
                fill=lists[count]
                fillI=i
            else:
                #else trys next index
                continue
        #Using the tracked indexs and values replaces the indexes
        lists[count]=lowest
        lists[fillI]=fill
        #displays list to user after changes
        print("Step "+str(count)+": "+str(lists))
        count=count+1
    #returns sorted list
    return ("Sorted list: "+str(lists))
#Calls functions
print(Sort([3, 18, 80, 9, 14, 12, 2, 18, 16])) 
print("")
print(Sort([1, 2, 3, 4, 5, 6]))
print("")
print(Sort([7]))
print("")
print(Sort([6, 6, 5, 4, 4, 3, 2, 2, 1]))
print("")
print(Sort([-3, 8, -2, 0, 9, 3, 0, 2]))
print("")