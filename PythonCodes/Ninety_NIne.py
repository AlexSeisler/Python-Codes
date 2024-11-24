total1=1
c=0
def check(c):
    global total, total1
    
    if total>=100:
        if total1%2==1:
            print (str(total)+", Player")
            exit()
        else:
            print (str(total)+", Dealer")
            exit()
    total1=total1+1


    if c==1:
        total=total+1
    elif c==2:
        total=total+2
    elif c==3:
        total=total+3
    elif c==4:
        total=total+4
    elif c==5:
        total=total+5
    elif c==6:
        total=total+6
    elif c==7:
        total=total+7
    elif c==8:
        total=total+8
    elif c==9:
        total=total+0
    elif c==10:

        total=total-10
    elif c==11:

        total=total+11
    elif c==12:

        total=total+12
    elif c==13:

        total=total+13
    elif c==14 and total<86:
        total=total+14
    elif c==14:
        total=total+1
    return total

        

def ninty(inpu):
    global total, total1
    total=inpu[0]
    
    
    for i in range(len(inpu)):
        if inpu[i]=="T":
            inpu[i]=10
        if inpu[i]=="J":
            inpu[i]=11
        if inpu[i]=="Q":
            inpu[i]=12
        if inpu[i]=="K":
            inpu[i]=13
        if inpu[i]=="A":
            inpu[i]=14
    cardp=[]
    #Adds original cards to the players hands
    cardp.append(inpu[1])
    cardp.append(inpu[2])
    cardp.append(inpu[3])

    #First player turn
    cardp.sort()

    c=cardp[-1]
    check(c)
    
    cardp.pop(-1)
    cardp.append(inpu[4])
    #First dealers turn
    c=inpu[5]
    check(c)
    #players second turn
    cardp.sort()
    c=cardp[-1]
    check(c)
    cardp.pop(-1)
    cardp.append(inpu[6])

    #dealers second turn
    c=inpu[7]
    check(c)

    #Players third turn
    cardp.sort()
    c=cardp[-1]
    check(c)
    cardp.pop(-1)
    cardp.append(inpu[8])


    #Dealers third turn
    c=inpu[9]
    check(c)


    #Players last drawing
    cardp.sort()
    c=cardp[-1]
    check(c)
    cardp.pop(-1)
    cardp.append(inpu[10])
    
    check(c)
    

    
    


#ninty([75,7,3,8,8,7,"T",5,9,"A",6])

#ninty([80,9,"T",7,8,"K","A",3,5,"Q","T"])

#ninty([94,4,2,2,7,"T",3,"A",5,"J","K"])

#ninty([80,6,6,4,"T",9,8,6,5,"Q","K"])

#ninty([90,"T",8,5,9,9,"Q","K","A","J",8])
#ninty([65,5,6,7,8,9,"T","J","Q","K","A"])
#ninty([74,"A",2,9,"T",9,7,"A",9,8,"A"])
#ninty([55,"A","K","Q","J","T","A","K","Q","J","T"])
#ninty([59,"A","T","K","A","Q","A","T",7,9,4])
ninty([70,"T","Q",9,9,"A","Q","J","K","Q","T"])