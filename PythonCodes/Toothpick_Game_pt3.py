import random
randomlist=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
count=0
while True:
    try:
        user=int(input("Game setup (1-Manual Setup)(2-Auto Setup): "))
    except ValueError:
            print("Thats not a number, try again")
            continue
    if user == 1 or user == 2:
        break
    else:
        print("Invalid input (1) or (2),try again")
        continue

print("")
if user==1:
    while True:
        try:
            row1=int(input("Amount of toothpicks in row1(1-20): "))
        except ValueError:
            print("Thats not a number, try again")
            continue
        if row1<21 and row1>0:
            break
        elif row1>20:
            print("To high, try again")
            continue
        elif row1<1:
            print("To low, try again")
            continue
        else:
            ("Invalid input")
            continue
    while True:
        try:
            row2=int(input("Amount of toothpicks in row2(1-20): "))
        except ValueError:
            print("Thats not a number, try again")
            continue
        if row2==row1:
            print("Can't have two lengths the same,try again")
            continue
        if row2<21 and row2>0:
            break
        elif row2>20:
            print("To high, try again")
            continue
        elif row2<1:
            print("To low, try again")
            continue
        else:
            ("Invalid input")
            continue
    while True:
        try:
            row3=int(input("Amount of toothpicks in row3(1-20): "))
        except ValueError:
            print("Thats not a number, try again")
            continue
        if row3==row1 or row3==row2:
            print("Can't have two lengths the same,try again")
            continue
        if row3<21 and row3>0:
            break
        elif row3>20:
            print("To high, try again")
            continue
        elif row3<1:
            print("To low, try again")
            continue
        else:
            ("Invalid input")
            continue
#11:37
elif user==2:
    row1=random.choice(randomlist)
    randomlist.pop(row1-1)
    randomlist.insert(row1-1,"fill")
    while True:
        row2=random.choice(randomlist)
        if row2 == "fill":
            continue
        else:
            break
    randomlist.pop(row2-1)
    randomlist.insert(row2-1,"fill")
    while True:
        row3=random.choice(randomlist)
        if row3 =="fill":
            continue
        else:
            break
    randomlist.pop(row3-1)
    randomlist.insert(row3-1,"fill")

    
print("Enter names below")  
print("")

while True:
    try:
        user7=int(input("(1) for 1 player/computer(2) for 2 players: ")) 
    except ValueError:
        print("Thats not a number, try again")
        continue
    if user7 ==1:
        player1="CPU"
        print("player 1: CPU")
        player2=input("Player 2: ")
        break
    elif user7==2:
        player1=input("Player 1: ")
        player2=input("Player 2: ")
        break
    else:
        print("Invalid input (1) or (2),try again")
        continue
print("")
print ("row 1: "+str(row1))
print ("row 2: "+str(row2))
print ("row 3: "+str(row3))
print("")
print("")
print("Enter who will go first below(1)or(2): ")
print("")
while True:
    try:
        first=int(input("First player: "))
    except ValueError:
            print("Thats not a number, try again")
            continue
    if first==1 or first==2:
        break
    else:
        print("invalid input,try again (1) or (2)")
        continue
print("")

if first==1:
    firstplayer=player1
    count=1
    secondplayer=player2
elif first==2:
    firstplayer=player2
    count=1
    secondplayer=player1
    
    
############
while True:
    if firstplayer!="CPU":
        if count%2==1:
            print(str(firstplayer)+"s turn,enter a row and how many toothpicks to take.")
    if secondplayer!="CPU":
        if count%2==0:
            print(str(secondplayer)+"s turn,enter a row and how many toothpicks to take.")
    print("")
    
    
    if firstplayer!="CPU":
        if count%2==1:
            print("row1=(1), row2=(2), row3=(3)")
            while True:
                try:
                    turnrow=int(input("What row: "))
                except ValueError:
                    print("Thats not a number, try again")
                    continue
                if turnrow==1 and row1==0:
                    print("There are no more toothpicks left there, try again")
                    continue
                elif turnrow==2 and row2==0:
                    print("There are no more toothpicks left there, try again")
                    continue
                elif turnrow==3 and row3==0:
                    print("There are no more toothpicks left there, try again")
                    continue
                if turnrow == 1 or turnrow == 2 or turnrow ==3:
                    break
                else:
                    print("invalid input (1), (2), or (3), try again")
            print("")
            while True:
                try:
                    picks=int(input("How many to take: "))
                except ValueError:
                    print("Thats not a number, try again")
                    continue
                if turnrow==1:
                    if picks>row1:
                        print("Not that many toothpicks,try again")
                        continue
                    elif picks<1:
                        print("Has to be greater than 0,try again")
                        continue
                    else:
                        break
                elif turnrow==2:
                    if picks>row2:
                        print("Not that many toothpicks,try again")
                        continue
                    elif picks<1:
                        print("Has to be greater than 0,try again")
                        continue
                    else:
                        break
                elif turnrow==3:
                    if picks>row3:
                        print("Not that many toothpicks,try again")
                        continue
                    elif picks<1:
                        print("Has to be greater than 0,try again")
                        continue
                    else:
                        break
        if turnrow==1:
            row1=row1-picks
        elif turnrow==2:
            row2=row2-picks
        elif turnrow==3:
            row3=row3-picks
        print("")
        print("New rows below")
        print("")
        print ("row 1: "+str(row1))
        print ("row 2: "+str(row2))
        print ("row 3: "+str(row3))
        print("")
        if row1==0 and row2==0 and row3==0 and count%2==1:
            print(str(firstplayer)+" IS THE WINNER")
            break
        elif row1==0 and row2==0 and row3==0 and count%2==0:
            print(str(secondplayer)+" IS THE WINNER")
            break
        count=count+1
    else:
        #Start top
        #Ai
        #
        #
        count5=0
        count6=0
        count7=0
        crow1=int(row1)
        crow2=int(row2)
        crow3=int(row3)
        filler=1
        while crow1>count5:
            count5=count5+1
            fill=row1
            fill=fill-count5
            crow1=str(bin(fill))[2:]
            crow2=str(bin(row2))[2:]
            crow3=str(bin(row3))[2:]
            while True:
                if len(crow1)!=5:
                    crow1="0"+crow1
                else:
                    break
            while True:
                if len(crow2)!=5:
                    crow2="0"+crow2
                else:
                    break
            while True:
                if len(crow3)!=5:
                    crow3="0"+crow3
                else:
                    break
            nim = ((int(crow1, 2)^int(crow2,2))^int(crow3,2))
    
            nimsum=(bin(nim)[2:].zfill(len(crow1)))
            crow1=int(row1)
            crow2=int(row2)
            crow3=int(row3)
            if nimsum=="00000":
                turnrow=1
                picks=count5
                filler=0
                break
        if filler!=0:
            
            while crow2>count6:
                count6=count6+1
                fill=row2
                fill=fill-count6
                crow1=str(bin(row1))[2:]
                crow2=str(bin(fill))[2:]
                crow3=str(bin(row3))[2:]
                while True:
                    if len(crow1)!=5:
                        crow1="0"+crow1
                    else:
                        break
                while True:
                    if len(crow2)!=5:
                        crow2="0"+crow2
                    else:
                        break
                while True:
                    if len(crow3)!=5:
                        crow3="0"+crow3
                    else:
                        break
                nim = ((int(crow1, 2)^int(crow2,2))^int(crow3,2))
        
                nimsum=(bin(nim)[2:].zfill(len(crow1)))
                crow1=int(row1)
                crow2=int(row2)
                crow3=int(row3)
                if nimsum=="00000":
                    turnrow=2
                    picks=count6
                    filler=0
                    break
        if filler!=0:
            
            while crow3>count7:
                count7=count7+1
                fill=row3
                fill=fill-count7
                crow1=str(bin(row1))[2:]
                crow2=str(bin(row2))[2:]
                crow3=str(bin(fill))[2:]
                while True:
                    if len(crow1)!=5:
                        crow1="0"+crow1
                    else:
                        break
                while True:
                    if len(crow2)!=5:
                        crow2="0"+crow2
                    else:
                        break
                while True:
                    if len(crow3)!=5:
                        crow3="0"+crow3
                    else:
                        break
                nim = ((int(crow1, 2)^int(crow2,2))^int(crow3,2))
        
                nimsum=(bin(nim)[2:].zfill(len(crow1)))
                crow1=int(row1)
                crow2=int(row2)
                crow3=int(row3)
                if nimsum=="00000":
                    turnrow=3
                    picks=count7
                    filler=0
                    break
            
        if filler==1:
            if row1>=row2 and row1>=row3:
                turnrow=1
            elif row2>=row1 and row2>=row3:
                turnrow=2
            elif row3>=row1 and row3>=row2:
                turnrow=3
            picks=1
            

        #end Ai
        #
        #
        #
        
                
                
                
        #printing Ai 
        if turnrow==1:
            row1=row1-picks
        elif turnrow==2:
            row2=row2-picks
        elif turnrow==3:
            row3=row3-picks
        print("")
        print("New rows below")
        print("")
        print ("row 1: "+str(row1))
        print ("row 2: "+str(row2))
        print ("row 3: "+str(row3))
        print("")
        if row1==0 and row2==0 and row3==0 and count%2==1:
            print(str(firstplayer)+" IS THE WINNER")
            break
        elif row1==0 and row2==0 and row3==0 and count%2==0:
            print(str(secondplayer)+" IS THE WINNER")
            break
        count=count+1
                    
                    
                    
                    
    if secondplayer!="CPU":
        if count%2==0:
            print("row1=(1), row2=(2), row3=(3)")
            while True:
                try:
                    turnrow=int(input("What row: "))
                except ValueError:
                    print("Thats not a number, try again")
                    continue
                if turnrow==1 and row1==0:
                    print("There are no more toothpicks left there, try again")
                    continue
                elif turnrow==2 and row2==0:
                    print("There are no more toothpicks left there, try again")
                    continue
                elif turnrow==3 and row3==0:
                    print("There are no more toothpicks left there, try again")
                    continue
                if turnrow == 1 or turnrow == 2 or turnrow ==3:
                    break
                else:
                    print("invalid input (1), (2), or (3), try again")
            print("")
            while True:
                try:
                    picks=int(input("How many to take: "))
                except ValueError:
                    print("Thats not a number, try again")
                    continue
                if turnrow==1:
                    if picks>row1:
                        print("Not that many toothpicks,try again")
                        continue
                    elif picks<1:
                        print("Has to be greater than 0,try again")
                        continue
                    else:
                        break
                elif turnrow==2:
                    if picks>row2:
                        print("Not that many toothpicks,try again")
                        continue
                    elif picks<1:
                        print("Has to be greater than 0,try again")
                        continue
                    else:
                        break
                elif turnrow==3:
                    if picks>row3:
                        print("Not that many toothpicks,try again")
                        continue
                    elif picks<1:
                        print("Has to be greater than 0,try again")
                        continue
                    else:
                        break
        if turnrow==1:
            row1=row1-picks
        elif turnrow==2:
            row2=row2-picks
        elif turnrow==3:
            row3=row3-picks
        print("")
        print("New rows below")
        print("")
        print ("row 1: "+str(row1))
        print ("row 2: "+str(row2))
        print ("row 3: "+str(row3))
        print("")
        if row1==0 and row2==0 and row3==0 and count%2==1:
            print(str(firstplayer)+" IS THE WINNER")
            break
        elif row1==0 and row2==0 and row3==0 and count%2==0:
            print(str(secondplayer)+" IS THE WINNER")
            break
        count=count+1
    else:
        #Start top
        #Ai
        #
        #
        #
        count5=0
        count6=0
        count7=0
        crow1=int(row1)
        crow2=int(row2)
        crow3=int(row3)
        filler=1
        while crow1>count5:
            count5=count5+1
            fill=row1
            fill=fill-count5
            crow1=str(bin(fill))[2:]
            crow2=str(bin(row2))[2:]
            crow3=str(bin(row3))[2:]
            while True:
                if len(crow1)!=5:
                    crow1="0"+crow1
                else:
                    break
            while True:
                if len(crow2)!=5:
                    crow2="0"+crow2
                else:
                    break
            while True:
                if len(crow3)!=5:
                    crow3="0"+crow3
                else:
                    break
            nim = ((int(crow1, 2)^int(crow2,2))^int(crow3,2))
    
            nimsum=(bin(nim)[2:].zfill(len(crow1)))
            crow1=int(row1)
            crow2=int(row2)
            crow3=int(row3)
            if nimsum=="00000":
                turnrow=1
                picks=count5
                filler=0
                break
        if filler!=0:
            
            while crow2>count6:
                count6=count6+1
                fill=row2
                fill=fill-count6
                crow1=str(bin(row1))[2:]
                crow2=str(bin(fill))[2:]
                crow3=str(bin(row3))[2:]
                while True:
                    if len(crow1)!=5:
                        crow1="0"+crow1
                    else:
                        break
                while True:
                    if len(crow2)!=5:
                        crow2="0"+crow2
                    else:
                        break
                while True:
                    if len(crow3)!=5:
                        crow3="0"+crow3
                    else:
                        break
                nim = ((int(crow1, 2)^int(crow2,2))^int(crow3,2))
        
                nimsum=(bin(nim)[2:].zfill(len(crow1)))
                crow1=int(row1)
                crow2=int(row2)
                crow3=int(row3)
                if nimsum=="00000":
                    turnrow=2
                    picks=count6
                    filler=0
                    break
        if filler!=0:
            
            while crow3>count7:
                count7=count7+1
                fill=row3
                fill=fill-count7
                crow1=str(bin(row1))[2:]
                crow2=str(bin(row2))[2:]
                crow3=str(bin(fill))[2:]
                while True:
                    if len(crow1)!=5:
                        crow1="0"+crow1
                    else:
                        break
                while True:
                    if len(crow2)!=5:
                        crow2="0"+crow2
                    else:
                        break
                while True:
                    if len(crow3)!=5:
                        crow3="0"+crow3
                    else:
                        break
                nim = ((int(crow1, 2)^int(crow2,2))^int(crow3,2))
        
                nimsum=(bin(nim)[2:].zfill(len(crow1)))
                crow1=int(row1)
                crow2=int(row2)
                crow3=int(row3)
                if nimsum=="00000":
                    turnrow=3
                    picks=count7
                    filler=0
                    break
            
        if filler==1:
            if row1>=row2 and row1>=row3:
                turnrow=1
            elif row2>=row1 and row2>=row3:
                turnrow=2
            elif row3>=row1 and row3>=row2:
                turnrow=3
            picks=1




        #end Ai
        #
        #
        #
        
                
                
        #printing Ai 
        if turnrow==1:
            row1=row1-picks
        elif turnrow==2:
            row2=row2-picks
        elif turnrow==3:
            row3=row3-picks
        print("")
        print("New rows below")
        print("")
        print ("row 1: "+str(row1))
        print ("row 2: "+str(row2))
        print ("row 3: "+str(row3))
        print("")
        if row1==0 and row2==0 and row3==0 and count%2==1:
            print(str(firstplayer)+" IS THE WINNER")
            break
        elif row1==0 and row2==0 and row3==0 and count%2==0:
            print(str(secondplayer)+" IS THE WINNER")
            break
        count=count+1
    
##################            
    
    
    
    
    
#Set Ai here using turnrow and picks    
if row1 >2 and row2 >2 and row3 >2:
    smallest=row1
    if row2<smallest:
        smallest=row2
    elif row3<smallest:
        smallest=row3
    if smallest==row1:
        turnrow=1
        picks=smallest
    elif smallest==row2:
        turnrow=2
        picks=smallest
    elif smallest==row3:
        picks=smallest
        turnrow=3
    

    
    
    
    
##################