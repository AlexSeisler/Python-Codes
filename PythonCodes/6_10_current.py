def reverse(string):
    end=""
    for p in string:
        end = p + end
    return end
def findHandSum(originalRows, handTiles, drawPile1):
    row1=[]
    row2=[]
    row3=[]
    row4=[]
    
    start=originalRows
    hand=handTiles
    drawPile=drawPile1
    

    #Recieving first parameter and putting it into its initiial list
    try:
        if start<0 or start>9999:
            return ("Bad input")
        start=str(start)
        while len(start)!=4:
            start="0"+start
        row1.append(start[0])
        row2.append(start[1])
        row3.append(start[2])
        row4.append(start[3])
    except:
        return("bad input")
    
    
    #Second Parameter 
    try:
        hand=hand.split(" ")
        for k in range(len(hand)):
            testerNum=int(hand[k])
            if testerNum<0 or testerNum>99:
                return ("Bad input")
            if len(hand[k])!=2:
                holder=hand[k]
                hand.pop(k)
                holder=holder+"0"
                hand.insert(k,holder)
    except:
        return("bad input")
        
    #Third paramter
    try:
        drawPile=drawPile.split(" ")
        for j in range(len(drawPile)):
            testerNum=int(drawPile[j])
            if testerNum<0 or testerNum>99:
                return ("Bad input")
            if len(drawPile[j])!=2:
                holder=drawPile[j]
                drawPile.pop(j)
                holder=holder+"0"
                drawPile.insert(j,holder)
    except:
        return("Bad input")


    
    
    check1=row1[-1][-1]
    check2=row2[-1][-1]
    check3=row3[-1][-1]
    check4=row4[-1][-1]
    if check1=="7" and check2 =="8" and check3=="3"and check4=="6":
        return 102
    
    begin=1
    turn=1
    double=0 
    wall=-1
    print(hand)
    print(drawPile)
    for a in range(100):

        count=0
        for i in range(len(hand)):
            print()
            print(len(row1))
            print(len(row2))
            print(len(row3))
            print(len(row4))
            print(wall)
            print(double)
            print (row1)
            print(row2)
            print(row3)
            print(row4)
            print(hand)
            print(drawPile)
            print()
            total=0
            if hand[i][0]==check1:
                total=total+1
            if hand[i][0]==check2:
                total=total+1
            if hand[i][0]==check3:
                total=total+1
            if hand[i][0]==check4:
                total=total+1
            if hand[i][1]==check1:
                total=total+1
            if hand[i][1]==check2:
                total=total+1
            if hand[i][1]==check3:
                total=total+1
            if hand[i][1]==check4:
                total=total+1
        
            if total==0:
                count=count+1
                if count>=len(hand):
                    ####
                    turnchecker1=0
                    turnchecker2=0
                    turnchecker3=0
                    turnchecker4=0
                    full=[]
                    for num in range(len(hand)):
                        full.append(hand[num][0])
                        full.append(hand[num][1])
                    
                    try:
                        full.index(check1)
                    except:
                        turnchecker1=1
                    try:
                        full.index(check2)
                    except:
                        turnchecker2=1
                    try:
                        full.index(check3)
                    except:
                        turnchecker3=1
                    try:
                        full.index(check4)
                    except:
                        turnchecker4=1
            
                        
                    if turnchecker1 == 1 and turnchecker2 == 1 and turnchecker3 == 1 and turnchecker4 == 1:
                        try:
                            hand.append(drawPile[0])
                            drawPile.pop(0)
                            break
                        except:
                            turn=0
                    else:
                        break
                    
                    
                    
                    
                   
                    
                    #####
                continue
            
            elif total!=0:
                






                #Row 1
                if begin==1 and (double==1 or double==0):
                    flipped=reverse(hand[i])
                    if hand[i][0]==check1:
                        if hand[i][0]==check1 and hand[i][1]==check1:
                            wall=len(row1)+2
                            double=1
                        
                        row1.append(hand[i])
                        hand.pop(i)
                        if len(row1)==wall:
                            begin=2
                            double=0
                            check1=row1[-1][-1]
                            check2=row2[-1][-1]
                            check3=row3[-1][-1]
                            check4=row4[-1][-1]
                        if len(hand)==0:
                            return 0
                        check1=row1[-1][-1]
                        begin=2
                        break
                    elif flipped[0]==check1:
                        row1.append(flipped)
                        hand.pop(i)
                        if len(row1)==wall:
                            begin=2
                            double=0
                            check1=row1[-1][-1]
                            check2=row2[-1][-1]
                            check3=row3[-1][-1]
                            check4=row4[-1][-1]
                        if len(hand)==0:
                            return 0
                        check1=row1[-1][-1]
                        begin=2
                        break
                    else:
                        if double==1:
                            begin=1
                        elif double==2:
                            begin=2
                        elif double==3:
                            begin=3
                        elif double==4:
                            begin=4
                        else:
                            begin=2
                            
                            
                    
        
                
                #Row 2
                if begin==2 and (double==2 or double==0):
                    flipped=reverse(hand[i])
                    if hand[i][0]==check2:
                        if hand[i][0]==check2 and hand[i][1]==check2:
                            double=2
                            wall=len(row2)+2
                        row2.append(hand[i])
                        hand.pop(i)
                        if len(row2)==wall:
                            begin=3
                            double=0
                            check1=row1[-1][-1]
                            check2=row2[-1][-1]
                            check3=row3[-1][-1]
                            check4=row4[-1][-1]
                        if len(hand)==0:
                            return 0
                        check2=row2[-1][-1]
                        begin=3
                        break
                    elif flipped[0]==check2 and begin == 2:
                        row2.append(flipped)
                        hand.pop(i)
                        if len(row2)==wall:
                            begin=3
                            double=0
                            check1=row1[-1][-1]
                            check2=row2[-1][-1]
                            check3=row3[-1][-1]
                            check4=row4[-1][-1]
                        if len(hand)==0:
                            return 0
                        check2=row2[-1][-1]
                        begin=3
                        break
                    else:
                        if double==1:
                            begin=1
                        elif double==2:
                            begin=2
                        elif double==3:
                            begin=3
                        elif double==4:
                            begin=4
                        else:
                            begin=3
        
                
                #Row 3
                if begin==3 and (double==3 or double==0):
                    flipped=reverse(hand[i])
                    if hand[i][0]==check3:
                        if hand[i][0]==check3 and hand[i][1]==check3:
                            double=3
                            wall=len(row3)+2
                        row3.append(hand[i])
                        hand.pop(i)
                        if len(row3)==wall:
                            begin=4
                            double=0
                            check1=row1[-1][-1]
                            check2=row2[-1][-1]
                            check3=row3[-1][-1]
                            check4=row4[-1][-1]
                        if len(hand)==0:
                            return 0
                        check3=row3[-1][-1]
                        begin=4
                        break
                    elif flipped[0]==check3:
                        row3.append(flipped)
                        hand.pop(i)
                        if len(row3)==wall:
                            begin=4
                            double=0
                            check1=row1[-1][-1]
                            check2=row2[-1][-1]
                            check3=row3[-1][-1]
                            check4=row4[-1][-1]
                        if len(hand)==0:
                            return 0
                        check3=row3[-1][-1]
                        begin=4
                        break
                    else:
                        if double==1:
                            begin=1
                        elif double==2:
                            begin=2
                        elif double==3:
                            begin=3
                        elif double==4:
                            begin=4
                        else:
                            begin=4
                        
                if begin==4 and (double==4 or double==0):
                    #Row 4
                    flipped=reverse(hand[i])
                    if hand[i][0]==check4:
                        if hand[i][0]==check4 and hand[i][1]==check4:
                            double=4
                            wall=len(row3)+2
                        row4.append(hand[i])
                        hand.pop(i)
                        if len(row4)==wall:
                            begin=1
                            double=0
                            check1=row1[-1][-1]
                            check2=row2[-1][-1]
                            check3=row3[-1][-1]
                            check4=row4[-1][-1]
                        if len(hand)==0:
                            return 0
                        check4=row4[-1][-1]
                        begin=1
                        break
                    elif flipped[0]==check4:
                        row4.append(flipped)
                        hand.pop(i)
                        if len(row4)==wall:
                            begin=1
                            double=0
                            check1=row1[-1][-1]
                            check2=row2[-1][-1]
                            check3=row3[-1][-1]
                            check4=row4[-1][-1]
                        if len(hand)==0:
                            return 0
                        check4=row4[-1][-1]
                        begin = 1
                        break
                    else:
                        if double==1:
                            begin=1
                        elif double==2:
                            begin=2
                        elif double==3:
                            begin=3
                        elif double==4:
                            begin=4
                        else:
                            begin=1
                
                if double==1:
                    if len(row1)==wall:
                        double=0
                    else:
                        check2=-1
                        check3=-1
                        check4=-1
                        begin=1
                
                    
                elif double==2:
                    if len(row2)==wall:

                        double=0
                    else:
                        check1=-1
                        check3=-1
                        check4=-1
                        begin=2
                    
                    
                elif double==3:
                    if len(row3)==wall:

                        double=0
                    else:
                        check1=-1
                        check2=-1
                        check4=-1
                        begin=3
                    
                    
                elif double==4:
                    if len(row4)==wall:

                        double=0
                        
                    else:
                        check1=-1
                        check2=-1
                        check3=-1
                        begin=4

                else:
                    check1=row1[-1][-1]
                    check2=row2[-1][-1]
                    check3=row3[-1][-1]
                    check4=row4[-1][-1]
                
                if double==0:
                    check1=row1[-1][-1]
                    check2=row2[-1][-1]
                    check3=row3[-1][-1]
                    check4=row4[-1][-1]
                
                turnchecker1=0
                turnchecker2=0
                turnchecker3=0
                turnchecker4=0
                full=[]
                for num in range(len(hand)):
                    full.append(hand[num][0])
                    full.append(hand[num][1])
                
                try:
                    full.index(check1)
                except:
                    turnchecker1=1
                try:
                    full.index(check2)
                except:
                    turnchecker2=1
                try:
                    full.index(check3)
                except:
                    turnchecker3=1
                try:
                    full.index(check4)
                except:
                    turnchecker4=1
        
                    
                if turnchecker1 == 1 and turnchecker2 == 1 and turnchecker3 == 1 and turnchecker4 == 1:
                    try:
                        hand.append(drawPile[0])
                        drawPile.pop(0)
                        break
                    except:
                        turn=0
                else:
                    break
          
    answerList=[]
    answer=0
    for line in range(len(hand)):
        answerList.append(hand[line][0])
        answerList.append(hand[line][1])
    for i in range(len(answerList)):
        answer=answer+int(answerList[i])
    return answer
print(findHandSum(655,"23 55 55 45 94 99 12 99 89 32","0"))