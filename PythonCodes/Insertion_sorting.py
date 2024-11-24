"""
A code showing the insertion sorting function. This is a 
method of splitting a given list into a sorted and unsorted 
sublist. By adding number by number into the sorted list then 
comparing the numbers in the sorted list you can sort the list.
"""
#Method to compare the new number in the sorted list to the index to the left of it returns the new sorted list
def check(unsorted):
    for i in range(1,len(unsorted)+1):
        #base case
        if i==len(unsorted):
            return unsorted
        #right spot
        elif unsorted[-i]>=unsorted[-i-1]:
            return unsorted
        #not right spot
        else:
            fill=unsorted[-i]
            fill1=unsorted[-i-1]
            unsorted[-i]=fill1
            unsorted[-i-1]=fill
#Main function that takes a list in splitting it to two sublists and using the insertion method to sort the list
def insertion(listed):
    #sets an empty list
  sort=[]
  #add the first element to the sorted list taking it out of the unsorted list
  sort.append(listed[0])
  listed.pop(0)
  print(sort)
  #loops through the unsorted list until its empty adding each element to the sorted list
  for i in range(len(listed)):
        sort.append(listed[0])
        listed.pop(0)
        #runs the sorted list through the check function to sort it
        sort=check(sort)
        print(sort)
  return sort
  
  
  
  
print(insertion([3,18,80,9,14,12,2,18,16]))
print()
print(insertion([1,2,3,4,5,6]))
print()
print(insertion([7]))
print()
print(insertion([6,6,5,4,4,3,2,2,1]))
print()
print(insertion([-3,8,-2,0,9,3,0,2]))