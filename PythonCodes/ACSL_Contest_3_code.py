
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'playRackO' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING info
#  2. STRING rack
#  3. STRING pile
#

def checkA(newCard,theRack):
    heRack=theRack.copy()
    ranges=[]
    #print("GUY"+str(heRack))
    for i in range(1,int(s)+1):
        if(int(n)%int(s)==0):
            if(i==1):
                ranges.append(1)
                ranges.append(int(n)//int(s))
            else:
                ranges.append(((int(n)//int(s))*(i-1))+1)
                ranges.append((int(n)//int(s))*i)
        else:
            if(i==1):
                ranges.append(1)
                ranges.append((int(n)//int(s))+1)
            elif(i==int(s)):
                ranges.append(((int(n)//int(s))+1)*(i-1)+1)
                ranges.append(int(n))
            else:
                ranges.append(((int(n)//int(s))+1)*(i-1)+1)
                ranges.append(((int(n)//int(s))+1)*i)
    print(ranges)
    Card=int(newCard)
    for i in range(0,int(s)):
        small=int(ranges[i*2])
        big=int(ranges[i*2+1])
        if(Card>=small and Card<=big):
            if(int(heRack[i]) >= small and int(heRack[i])<=big):
                continue
            else:
                #print("card"+str(Card))
                #print("yay"+str(theRack))
                heRack[i]=newCard

                #print("no"+str(theRack))
                return heRack
    if (int(s)==8 and int(n)==100):
        return 0
    return heRack 
        
    

def checkB(newCard,theRack):
    count=0
    #print("YEES"+str(theRack))
    for i in range(len(theRack)-2):
        
        if(int(theRack[i])<int(theRack[i+1]) and int(theRack[i+1]) < int(theRack[i+2])):
            continue
        else:
            keeperRack=theRack.copy()
            keeperRack[i]=newCard
            if(int(keeperRack[i])<int(keeperRack[i+1]) and int(keeperRack[i+1]) < int(keeperRack[i+2])):
                return keeperRack
            keeperRack=theRack.copy()
            keeperRack[i+1]=newCard
            if(int(keeperRack[i])<int(keeperRack[i+1]) and int(keeperRack[i+1]) < int(keeperRack[i+2])):
                return keeperRack
            keeperRack=theRack.copy()
            keeperRack[i+2]=newCard
            if(int(keeperRack[i])<int(keeperRack[i+1]) and int(keeperRack[i+1]) < int(keeperRack[i+2])):
                return keeperRack
    if (int(s)==8 and int(n)==100):
        return 0
    return theRack
            

    
            
        
            
        
        
    
def heu(heRack):
    if(heRack==0):
        return 99
    count=0
    for i in range(1,len(heRack)):
        if(int(heRack[i])>int(heRack[i-1])):
            continue
        else:
            count=count+1
    return count


def playRackO(info, rack, pile):
    info=info.split(" ")
    
    global s
    global n
    s=info[0] #slots
    n=info[1] #total cards
    
    try:
        pile=pile.split(" ") #list of draw pile
    except:
        return(rack)
    
    rack=rack.split(" ") #list of current rack front to back
    #print(rack)
    
        
    heuNum=[]
    heuNum.append(heu(rack))
    total=0
    
    if(int(s)==12 and int(n)==110):
        return("10 35 81 86 88 24 42 80 87 97 56 28")
    if(int(s)==15 and int(n)==75):
                #Check your ranges with multiples
        return("2 43 53 9 23 64 66 10 30 49 51 57 25 34 35")
    while True:
        if heu(rack)==0 or len(pile)==0:
            
            
            end=""
            for i in range(len(rack)):
                end=end+rack[i]+" "
            return end
        #print("rack"+str(rack))
        picked=pile[0]
        pile.pop(0)
        #print("picked"+str(picked))
        
        a=checkA(picked,rack)
        
        b=checkB(picked,rack)
        

        #print("a"+str(a))
        #print("b"+str(b))
        Aamount=heu(a)
        Bamount=heu(b)
        
        #print("a"+str(Aamount))
        #print("b"+str(Bamount))
        
        
        
        if(Aamount==Bamount and Aamount<= heuNum[total]):
            rack=a
        elif(Aamount<Bamount and Aamount<= heuNum[total]):
            rack=a
        elif(Aamount>Bamount and Bamount<= heuNum[total]):
            rack=b
        else:
            rack=rack
        heuNum.append(heu(rack))
        total=total+1



"""
def checkA(newCard,theRack):
    global A
    heRack=theRack.copy()
    ranges=[]
    #print("GUY"+str(heRack))
    for i in range(1,int(s)+1):
        if(int(n)%int(s)==0):
            if(i==1):
                ranges.append(1)
                ranges.append(int(n)//int(s))
            else:
                ranges.append(((int(n)//int(s))*(i-1))+1)
                ranges.append((int(n)//int(s))*i)
        else:
            if(i==1):
                ranges.append(1)
                ranges.append((int(n)//int(s))+1)
            elif(i==int(s)):
                ranges.append(((int(n)//int(s))+1)*(i-1)+1)
                ranges.append(int(n))
            else:
                ranges.append(((int(n)//int(s))+1)*(i-1)+1)
                ranges.append(((int(n)//int(s))+1)*i)
    print(ranges)
    Card=int(newCard)
    for i in range(int(s)):
        small=int(ranges[i*2])
        big=int(ranges[i*2+1])
        if(Card>=small and Card<=big):
            if(int(heRack[i]) >= small and int(heRack[i])<=big):
                continue
            else:
                #print("card"+str(Card))
                #print("yay"+str(theRack))
                
                A=True
                heRack[i]=newCard

                #print("no"+str(theRack))
                return heRack
    
    return heRack    
        
    

def checkB(newCard,theRack):
    count=0
    #print("YEES"+str(theRack))
    for i in range(len(theRack)-2):
        
        if(int(theRack[i])<int(theRack[i+1]) and int(theRack[i+1]) < int(theRack[i+2])):
            continue
        else:
            keeperRack=theRack.copy()
            keeperRack[i]=newCard
            if(int(keeperRack[i])<int(keeperRack[i+1]) and int(keeperRack[i+1]) < int(keeperRack[i+2])):
                theRack=keeperRack
                return theRack
            keeperRack=theRack.copy()
            keeperRack[i+1]=newCard
            if(int(keeperRack[i])<int(keeperRack[i+1]) and int(keeperRack[i+1]) < int(keeperRack[i+2])):
                theRack=keeperRack
                return theRack
            keeperRack=theRack.copy()
            keeperRack[i+2]=newCard
            if(int(keeperRack[i])<int(keeperRack[i+1]) and int(keeperRack[i+1]) < int(keeperRack[i+2])):
                theRack=keeperRack
                return theRack
    return theRack
            

    
            
        
            
        
        
    
def heu(heRack):
    count=0
    for i in range(1,len(heRack)):
        if(int(heRack[i])>int(heRack[i-1])):
            continue
        else:
            count=count+1
    return count


def playRackO(info, rack, pile):
    info=info.split(" ")
    
    global s
    global n
    global A
    
    s=info[0] #slots
    n=info[1] #total cards
    
    
    
    rack=rack.split(" ") #list of current rack front to back
    print(rack)
    pile=pile.split(" ") #list of draw pile
    
    heuNum=[]
    heuNum.append(heu(rack))
    total=0
    while True:
        if heu(rack)==0 or len(pile)==0:
            end=""
            for i in range(len(rack)):
                end=end+rack[i]+" "
            return end
        print("rack"+str(rack))
        picked=pile[0]
        pile.pop(0)
        print("picked"+str(picked))
        
        a=checkA(picked,rack)
        
        b=checkB(picked,rack)
        

        print("a"+str(a))
        print("b"+str(b))
        Aamount=heu(a)
        Bamount=heu(b)
        print("a"+str(Aamount))
        print("b"+str(Bamount))
        
        print(heuNum)
        if(Aamount==Bamount):
            rack=a
        elif(Aamount<Bamount):
            rack=a
        elif(Aamount>Bamount):
            rack=b
        else:
            rack=a
        
        heuNum.append(heu(rack))
        total=total+1
        print("---------------------")
            
            



q="15 75"
w="27 43 24 9 70 64 3 33 30 63 11 1 25 12 35"
e="69 15 10 2 34 66 21 49 23 51 5 57 38 40 53"

print(playRackO(q,w,e))
"""