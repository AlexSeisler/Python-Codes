check=False
cord=[]
def bishop(twodlist):
    global check
    global cord
    for i in range(8):
        for j in range(8):
            if twodlist[i][j]=="B":
                for f in range(8):
                    
                    try:
                        if twodlist[i+f][j+f]!="K" and twodlist[i+f][j+f]!=0:
                            cord.append((i+f,j+f))
                        if twodlist[i+f][j+f]=="K":
                            check=True
                        if twodlist[i+f][j+f]==0 and i+f>=0 and i+f<8 and j+f>=0 and j+f<8:
                            twodlist[i+f][j+f]=1
                    except:
                        pass
                    try:
                        if twodlist[i-f][j-f]!="K" and twodlist[i-f][j-f]!=0:
                            cord.append((i-f,j-f))
                            
                        if twodlist[i-f][j-f]=="K":
                            check=True
                        if twodlist[i-f][j-f]==0 and i-f>=0 and i-f<8 and j-f>=0 and j-f<8:
                            twodlist[i-f][j-f]=1
                    except:
                        pass
                    try:
                        if twodlist[i+f][j-f]!="K" and twodlist[i+f][j-f]!=0:
                            cord.append((i+f,j-f))
                        if twodlist[i+f][j-f]=="K":
                            check=True
                        if twodlist[i+f][j-f]==0 and i+f>=0 and i+f<8 and j-f>=0 and j-f<8:
                            twodlist[i+f][j-f]=1
                    except:
                        pass
                    try:
                        if twodlist[i-f][j-f]!="K" and twodlist[i-f][j-f]!=0:
                            cord.append((i-f,j-f))
                        if twodlist[i-f][j+f]=="K":
                            check=True
                        if twodlist[i-f][j+f]==0 and i-f>=0 and i-f<8 and j+f>=0 and j+f<8:
                            twodlist[i-f][j+f]=1
                    except:
                        pass

    return twodlist
    
def rook(twodlist):
    global cord
    global check
    for i in range(8):
        for j in range(8):
            if twodlist[i][j]=="R":
                for f in range(8):
                    try:
                        if twodlist[i+f][j]!="K" and twodlist[i+f][j]!=0:
                            cord.append((i+f,j))
                            
                        if twodlist[i+f][j]=="K":
                            check=True
                        if twodlist[i+f][j]==0 and i+f>=0 and i+f<8 and j>=0 and j<8:
                            twodlist[i+f][j]=1
                    except:
                        pass
                    try:
                        if twodlist[i][j+f]!="K" and twodlist[i][j+f]!=0:
                            cord.append((i,j+f))
                        if twodlist[i][j+f]=="K":
                            check=True
                        if twodlist[i][j+f]==0 and i>=0 and i<8 and j+f>=0 and j+f<8:
                            twodlist[i][j+f]=1
                    except:
                        pass
                    try:
                        if twodlist[i][j-f]!="K" and twodlist[i][j-f]!=0:
                            cord.append((i,j-f))
                            
                        if twodlist[i][j-f]=="K":
                            check=True
                        if twodlist[i][j-f]==0 and i>=0 and i<8 and j-f>=0 and j-f<8:
                            twodlist[i][j-f]=1
                    except:
                        pass
                    try:
                        if twodlist[i-f][j]!="K" and twodlist[i-f][j]!=0:
                            cord.append((i-f,j))
                        
                        if twodlist[i-f][j]=="K":
                            check=True
                        if twodlist[i-f][j]==0 and i-f>=0 and i-f<8 and j>=0 and j<8:
                            twodlist[i-f][j]=1
                    except:
                        pass
    return twodlist

def pawn(twodlist):
    global check
    global cord
    for i in range(8):
        for j in range(8):
            if twodlist[i][j]=="P":
                try:
                    if twodlist[i-1][j-1]!="K" and twodlist[i-1][j-1]!=0:
                            cord.append((i-1,j-1))
                            
                    if twodlist[i-1][j-1]=="K":
                            check=True
                    if twodlist[i-1][j-1]==0 and i-1>=0 and i-1<8 and j-1>=0 and j-1<8:
                        twodlist[i-1][j-1]=1
                except:
                    pass
                try:
                    if twodlist[i-1][j+1]!="K" and twodlist[i-1][j+1]!=0:
                            cord.append((i-1,j+1))
                            
                    if twodlist[i-1][j+1]=="K":
                            check=True
                    if twodlist[i-1][j+1]==0 and i-1>=0 and i-1<8 and j+1>=0 and j+1<8:
                        twodlist[i-1][j+1]=1
                except:
                    pass
                
    return twodlist





def knight(twodlist):
    global check
    for i in range(8):
        for j in range(8):
            if twodlist[i][j]=="N":
                try:
                    if twodlist[i+2][j+1]!="K" and twodlist[i+2][j+1]!=0:
                            cord.append((i+2,j+1))
                            
                    if twodlist[i+2][j+1]=="K":
                        check=True
                    if twodlist[i+2][j+1]==0 and i+2>=0 and i+2<8 and j+1>=0 and j+1<8:
                        twodlist[i+2][j+1]=1
                except:
                    pass
                try:
                    if twodlist[i+2][j-1]!="K" and twodlist[i+2][j-1]!=0:
                            cord.append((i+2,j-1))
                            
                    if twodlist[i+2][j-1]=="K":
                        check=True
                    if twodlist[i+2][j-1]==0 and i+2>=0 and i+2<8 and j-1>=0 and j-1<8:
                        twodlist[i+2][j-1]=1
                except:
                    pass
                try:
                    if twodlist[i+1][j-2]!="K" and twodlist[i+1][j-2]!=0:
                            cord.append((i+1,j-2))
                            
                    if twodlist[i+1][j-2]=="K":
                        check=True
                    if twodlist[i+1][j-2]==0 and i+1>=0 and i+1<8 and j-2>=0 and j-2<8:
                        twodlist[i+1][j-2]=1
                except:
                    pass
                try:
                    if twodlist[i+1][j+2]!="K" and twodlist[i+1][j+2]!=0:
                            cord.append((i+1,j+2))
                            
                    if twodlist[i+1][j+2]=="K":
                        check=True
                    if twodlist[i+1][j+2]==0 and i+1>=0 and i+1<8 and j+2>=0 and j+2<8:
                        twodlist[i+1][j+2]=1
                except:
                    pass
                
                try:
                    if twodlist[i+2][j+1]!="K" and twodlist[i+2][j+1]!=0:
                            cord.append((i+2,j+1))
                    if twodlist[i-1][j+2]=="K":
                        check=True
                    if twodlist[i-1][j+2]==0 and i-1>=0 and i-1<8 and j+2>=0 and j+2<8:
                        twodlist[i-1][j+2]=1
                except:
                    pass
                try:
                    if twodlist[i-1][j-2]=="K":
                        check=True
                    if twodlist[i-1][j-2]==0 and i-1>=0 and i-1<8 and j-2>=0 and j-2<8:
                        twodlist[i-1][j-2]=1
                except:
                    pass
                try:
                    if twodlist[i-2][j+1]=="K":
                        check=True
                    if twodlist[i-2][j+1]==0 and i-2>=0 and i-2<8 and j+1>=0 and j+1<8:
                        twodlist[i-2][j+1]=1
                except:
                    pass
                try:
                    if twodlist[i-2][j-1]=="K":
                        check=True
                    if twodlist[i-2][j-1]==0 and i-2>=0 and i-2<8 and j-1>=0 and j-1<8:
                        twodlist[i-2][j-1]=1
                except:
                    pass
    return twodlist

def queen(twodlist):
    global check
    for i in range(8):
        for j in range(8):
            if twodlist[i][j]=="Q":
                try:
                    if twodlist[i+1][j]=="K":
                        check=True
                    if twodlist[i+1][j]==0 and i+1>=0 and i+1<8 and j>=0 and j<8:
                        twodlist[i+1][j]=1
                except:
                    pass
                try:
                    if twodlist[i-1][j]=="K":
                        check=True
                    if twodlist[i-1][j]==0 and i-1>=0 and i-1<8 and j>=0 and j<8:
                        twodlist[i-1][j]=1
                except:
                    pass
                try:
                    if twodlist[i][j+1]=="K":
                        check=True
                    if twodlist[i][j+1]==0 and i>=0 and i<8 and j+1>=0 and j+1<8:
                        twodlist[i][j+1]=1
                except:
                    pass
                try:
                    if twodlist[i][j-1]=="K":
                        check=True
                    if twodlist[i][j-1]==0 and i>=0 and i<8 and j-1>=0 and j-1<8:
                        twodlist[i][j-1]=1
                except:
                    pass
                try:
                    if twodlist[i-1][j-1]=="K":
                        check=True
                    if twodlist[i-1][j-1]==0 and i-1>=0 and i-1<8 and j-1>=0 and j-1<8:
                        twodlist[i-1][j-1]=1
                except:
                    pass
                try:
                    if twodlist[i+1][j-1]=="K":
                        check=True
                    if twodlist[i+1][j-1]==0 and i+1>=0 and i+1<8 and j-1>=0 and j-1<8:
                        twodlist[i+1][j-1]=1
                except:
                    pass
                try:
                    if twodlist[i+1][j+1]=="K":
                        check=True
                    if twodlist[i+1][j+1]==0 and i+1>=0 and i+1<8 and j+11>=0 and j+1<8:
                        twodlist[i+1][j+1]=1
                except:
                    pass
                try:
                    if twodlist[i-1][j+1]=="K":
                        check=True
                    if twodlist[i-1][j+1]==0 and i-1>=0 and i-1<8 and j+1>=0 and j+1<8:
                        twodlist[i-1][j+1]=1
                except:
                    pass
                for f in range(8):
                    try:
                        if twodlist[i+f][j]=="K":
                            check=True
                        if twodlist[i+f][j]==0 and i+f>=0 and i+f<8 and j>=0 and j<8:
                            twodlist[i+f][j]=1
                    except:
                        pass
                    try:
                        if twodlist[i][j+f]=="K":
                            check=True
                        if twodlist[i][j+f]==0 and i>=0 and i<8 and j+f>=0 and j+f<8:
                            twodlist[i][j+f]=1
                    except:
                        pass
                    try:
                        if twodlist[i][j-f]=="K":
                            check=True
                        if twodlist[i][j-f]==0 and i>=0 and i<8 and j-f>=0 and j-f<8:
                            twodlist[i][j-f]=1
                    except:
                        pass
                    try:
                        if twodlist[i-f][j]=="K":
                            check=True
                        if twodlist[i-f][j]==0 and i-f>=0 and i-f<8 and j>=0 and j<8:
                            twodlist[i-f][j]=1
                    except:
                        pass
                    
                    
                    
                    try:
                        if twodlist[i+f][j+f]=="K":
                            check=True
                        if twodlist[i+f][j+f]==0 and i+f>=0 and i+f<8 and j+f>=0 and j+f<8:
                            twodlist[i+f][j+f]=1
                    except:
                        pass
                    try:
                        if twodlist[i-f][j-f]=="K":
                            check=True
                        if twodlist[i-f][j-f]==0 and i-f>=0 and i-f<8 and j-f>=0 and j-f<8:
                            twodlist[i-f][j-f]=1
                    except:
                        pass
                    try:
                        if twodlist[i+f][j-f]=="K":
                            check=True
                        if twodlist[i+f][j-f]==0 and i+f>=0 and i+f<8 and j-f>=0 and j-f<8:
                            twodlist[i+f][j-f]=1
                    except:
                        pass
                    try:
                        if twodlist[i-f][j+f]=="K":
                            check=True
                        if twodlist[i-f][j+f]==0 and i-f>=0 and i-f<8 and j+f>=0 and j+f<8:
                            twodlist[i-f][j+f]=1
                    except:
                        pass
                    
                    
    return twodlist
                    



def king_check(peices_list):
    global check
    twoD=[]
    ylist=[]
    xlist=[]
    peices_fixed=[]
    positions="abcdefgh"
    endlist=[]
    movable=False
    for i in range(8):
        
        twoD.append([0,0,0,0,0,0,0,0])
    for i in range(len(peices_list)):
        peice=peices_list[i][0]
        x=peices_list[i][1]
        x=positions.find(x)
        
        xlist.append(x)
        y=peices_list[i][2]
        y=int(y)
        y=9-y
        y=int(y)-1
        
        ylist.append(y)
        twoD[int(y)][int(x)]=peice
        
        
        
        endlist.append(peice+str(x)+str(y))
    twoD=bishop(twoD)
    twoD=rook(twoD)
    twoD=queen(twoD)
    twoD=pawn(twoD)
    twoD=knight(twoD)
    
    
    
    for i in range(8):
        for j in range(8):
            if twoD[i][j]=="K":
                try:
                    if twoD[i+1][j]!=1 and i+1>=0 and i+1<8 and j>=0 and j<8:
                        movable=True
                except:
                    pass
                try:
                    if twoD[i-1][j]!=1 and i-1>=0 and i-1<8 and j>=0 and j<8:
                        movable=True
                except:
                    pass
                try:
                    if twoD[i][j+1]!=1 and i>=0 and i<8 and j+1>=0 and j+1<8:
                        movable=True
                except:
                    pass
                try:
                    if twoD[i][j-1]!=1 and i>=0 and i<8 and j-1>=0 and j-1<8:
                        movable=True
                except:
                    pass
                try:
                    if twoD[i-1][j-1]!=1 and i-1>=0 and i-1<8 and j-1>=0 and j-1<8:
                        movable=True
                except:
                    pass
                try:
                    if twoD[i+1][j-1]!=1 and i+1>=0 and i+1<8 and j-1>=0 and j-1<8:
                        movable=True
                except:
                    pass
                try:
                    if twoD[i+1][j+1]!=1 and i+1>=0 and i+1<8 and j+11>=0 and j+1<8:
                        movable=True
                except:
                    pass
                try:
                    if twoD[i-1][j+1]!=1 and i-1>=0 and i-1<8 and j+1>=0 and j+1<8:
                        movable=True
                except:
                    pass
    
    
    
    for i in range(8):
        print(twoD[i])
    
    
    #check = in check
    #movable has a move
    if check==True and movable==True:
        return "Check"
    elif check==True and movable==False:
        return "Checkmate"
    elif check==False and movable==True:
        return "Safe"
    elif check==False and movable==False:
        return "Stalemate"
        
    
user=input("Enter Peices: ")
user=user.split(" ")
print(king_check(user))


#Ba1 Rd3 Rg7 Qb3 Ke6
#Rc1 Kd8 Qb6 Re5 Bh3
#Qf4 Be5 Rc1 Kd3
#Ra1 Pb5 Pc5 Rc3 Bd6 Qg4 Kb7
#Ka4 Be8 Rh5 Qf8 Nb6 Nd2 Pc5 Pa3 Bc3
#reverted to 6:40
#8:04 finished but failed
#This code will not work if the peice that is the empty space is protected