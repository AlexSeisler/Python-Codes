while True:
    check=False
    cords=[]
    peices="QRBPN"
    def moves(twodlist):
        global peices
        global check
        global cords
        for i in range(8):
            for j in range(8):
                if twodlist[i][j]=="R":
                    
                    for right in range(j+1,8):
                        if i<0 or right>=8:
                            break
                        pos=twodlist[i][right]
                        if pos==0:
                            twodlist[i][right]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((i,right))
                            break
                    for left in range(j-1,-1,-1):
                        if i<0 or left>=8:
                            break
                        pos=twodlist[i][left]
                        if pos==0:
                            twodlist[i][left]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((i,left))
                            break
                    for down in range(i+1,8):
                        if i<0 or down>=8:
                            break
                        pos=twodlist[down][j]
                        if pos==0:
                            twodlist[down][j]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((down,j))
                            break
                    for up in range(i-1,-1,-1):
                        if i<0 or up>=8:
                            break
                        pos=twodlist[up][j]
                        if pos==0:
                            twodlist[up][j]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((up,j))
                            break
                
                if twodlist[i][j]=="B":
                    for tl in range(i-1,-1,-1):
                        col= j-(i-tl)
                        
                        if tl<0 or col >=8:
                            break
                        pos=twodlist[tl][col]
                        if pos==0:
                            twodlist[tl][col]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((tl,col))
                            break
                    for tr in range(i-1,-1,-1):
                        col= j +(i-tr)
                        
                        if tr<0 or col >=8:
                            break
                        pos=twodlist[tr][col]
                        if pos==0:
                            twodlist[tr][col]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((tr,col))
                            break
                    for bl in range(i+1,8):
                        col= j-(bl-i)
                        
                        if bl<0 or col >=8:
                            break
                        pos=twodlist[bl][col]
                        if pos==0:
                            twodlist[bl][col]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((bl,col))
                            break
                    for br in range(i+1,8):
                        col=j+(br-i)
                        
                        if br<0 or col >=8:
                            break
                        pos=twodlist[br][col]
                        if pos==0:
                            twodlist[br][col]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((br,col))
                            break
                if twodlist[i][j]=="Q":
                    for right in range(j+1,8):
                        if i<0 or right>=8:
                            break
                        pos=twodlist[i][right]
                        if pos==0:
                            twodlist[i][right]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((i,right))
                            break
                    for left in range(j-1,-1,-1):
                        if i<0 or left>=8:
                            break
                        pos=twodlist[i][left]
                        if pos==0:
                            twodlist[i][left]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((i,left))
                            break
                    for down in range(i+1,8):
                        if i<0 or down>=8:
                            break
                        pos=twodlist[down][j]
                        if pos==0:
                            twodlist[down][j]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((down,j))
                            break
                    for up in range(i-1,-1,-1):
                        if i<0 or up>=8:
                            break
                        pos=twodlist[up][j]
                        if pos==0:
                            twodlist[up][j]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((up,j))
                            break
                
                    for tl in range(i-1,-1,-1):
                        col= j-(i-tl)
                        
                        if tl<0 or col >=8:
                            break
                        pos=twodlist[tl][col]
                        if pos==0:
                            twodlist[tl][col]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((tl,col))
                            break
                    for tr in range(i-1,-1,-1):
                        col= j +(i-tr)
                        
                        if tr<0 or col >=8:
                            break
                        pos=twodlist[tr][col]
                        if pos==0:
                            twodlist[tr][col]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((tr,col))
                            break
                    for bl in range(i+1,8):
                        col= j-(bl-i)
                        
                        if bl<0 or col >=8:
                            break
                        pos=twodlist[bl][col]
                        if pos==0:
                            twodlist[bl][col]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((bl,col))
                            break
                    for br in range(i+1,8):
                        col=j+(br-i)
                        
                        if br<0 or col >=8:
                            break
                        pos=twodlist[br][col]
                        if pos==0:
                            twodlist[br][col]=1
                            continue
                        elif pos == "K":
                            check = True
                            break
                        elif str(pos) in peices:
                            cords.append((br,col))
                            break
                    try:
                        if twodlist[i+1][j]!=1 and i+1>=0 and i+1<8 and j>=0 and j<8:
                            pos=twodlist[i+1][j]
                            if pos==0:
                                twodlist[i+1][j]=1
                                continue
                            elif pos == "K":
                                check = True
                                break
                            elif str(pos) in peices:
                                cords.append((i+1,j))
                                break
                    except:
                        pass
                    try:
                        if twodlist[i-1][j]!=1 and i-1>=0 and i-1<8 and j>=0 and j<8:
                            pos=twodlist[i-1][j]
                            if pos==0:
                                twodlist[i-1][j]=1
                                continue
                            elif pos == "K":
                                check = True
                                break
                            elif str(pos) in peices:
                                cords.append((i-1,j))
                                break
                    except:
                        pass
                    try:
                        if twodlist[i][j+1]!=1 and i>=0 and i<8 and j+1>=0 and j+1<8:
                            pos=twodlist[i][j+1]
                            if pos==0:
                                twodlist[i][j+1]=1
                                continue
                            elif pos == "K":
                                check = True
                                break
                            elif str(pos) in peices:
                                cords.append((i,j+1))
                                break
                    except:
                        pass
                    try:
                        if twodlist[i][j-1]!=1 and i>=0 and i<8 and j-1>=0 and j-1<8:
                            pos=twodlist[i][j-1]
                            if pos==0:
                                twodlist[i][j-1]=1
                                continue
                            elif pos == "K":
                                check = True
                                break
                            elif str(pos) in peices:
                                cords.append((i,j-1))
                                break
                    except:
                        pass
                    try:
                        if twodlist[i-1][j-1]!=1 and i-1>=0 and i-1<8 and j-1>=0 and j-1<8:
                            pos=twodlist[i-1][j-1]
                            if pos==0:
                                twodlist[i-1][j-1]=1
                                continue
                            elif pos == "K":
                                check = True
                                break
                            elif str(pos) in peices:
                                cords.append((i-1,j-1))
                                break
                    except:
                        pass
                    try:
                        if twodlist[i+1][j-1]!=1 and i+1>=0 and i+1<8 and j-1>=0 and j-1<8:
                            pos=twodlist[i+1][j-1]
                            if pos==0:
                                twodlist[i+1][j-1]=1
                                continue
                            elif pos == "K":
                                check = True
                                break
                            elif str(pos) in peices:
                                cords.append((i+1,j-1))
                                break
                    except:
                        pass
                    try:
                        if twodlist[i+1][j+1]!=1 and i+1>=0 and i+1<8 and j+11>=0 and j+1<8:
                            pos=twodlist[i+1][j+1]
                            if pos==0:
                                twodlist[i+1][j+1]=1
                                continue
                            elif pos == "K":
                                check = True
                                break
                            elif str(pos) in peices:
                                cords.append((i+1,j+1))
                                break
                    except:
                        pass
                    try:
                        if twodlist[i-1][j+1]!=1 and i-1>=0 and i-1<8 and j+1>=0 and j+1<8:
                            pos=twodlist[i-1][j+1]
                            if pos==0:
                                twodlist[i-1][j+1]=1
                                continue
                            elif pos == "K":
                                check = True
                                break
                            elif str(pos) in peices:
                                cords.append((i-1,j+1))
                                break
                    except:
                        pass
                if twodlist[i][j]=="N":
    
                    moves = [(-2, -1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
                    for n in range(len(moves)):
                        row=moves[n][0]
                        colum=moves[n][1]
                        row1=row+i
                        colum1=colum+j
                        if (row1<0 or row1>7)or(colum1<0 or colum1>7):
                            continue
                            
                        try:
                            
                            pos=twodlist[row1][colum1]
                            
                            if pos==0:
                                twodlist[row1][colum1]=1
                                continue
                            elif pos == "K":
                                check = True
                                continue
        
                            elif str(pos) in peices:
                                cords.append((row1,colum1))
                                continue
                        except:
                            pass
    
                if twodlist[i][j]=="P":
                    try:
                        row1=i-1
                        colum1=j-1
                        pos=twodlist[i-1][j-1]
                        if (row1<0 or row1>7)or(colum1<0 or colum1>7):
                            pass
                        
                        elif pos==0:
                            twodlist[i-1][j-1]=1
                        elif pos == "K":
                            check = True
                        elif str(pos) in peices:
                            cords.append((i-1,j-1))
                    except:
                        pass
                    try:
                        row1=i-1
                        colum1=j+1
                        pos=twodlist[i-1][j+1]
                        if (row1<0 or row1>7)or(colum1<0 or colum1>7):
                            pass
                        
                        elif pos==0:
                            twodlist[i-1][j+1]=1
                        elif pos == "K":
                            check = True
                        elif str(pos) in peices:
                            cords.append((i-1,j+1))
                    except:
                        pass
                    
                    
                    
                    
                            
        return twodlist
    def king_check(peices_list):
        global check
        global cords
        global peices
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
        
    
        twoD=moves(twoD)
    
        
        
        
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
        for i in range(len(cords)):
            x=cords[i][0]
            y=cords[i][1]
            twoD[x][y]=1
        
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

#Rh8 Qh2 Be8 Rg1 Kh4
#Ba1 Rf6 Rg2 Qc1 Ke3
#Rc8 Qc3 Re4 Bh5 Kf7
#Kd6 Qf5 Be4 Rc7 Re1 Ba5
#Rb8 Ka3 Qe5 Bd1 Bc3 Rh3
#Rh8 Qa8 Bh2 Kc7 Bd7 Rb2

#Bf8 Rb8 Pc5 Qh7 Kc6 Bf1 Pb5
#Ba2 Pg5 Re3 Qd8 Pd5 Kf7 Ph6

#Kb8 Qb7 Nb5 Nd6
#Ra1 Ka8 Nc8 Nd7 Bg1 Qe8 Pa6 Rh8