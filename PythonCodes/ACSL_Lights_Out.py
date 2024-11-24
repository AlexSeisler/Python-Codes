#creates empty board indexes starting at 1
board=[["fill"],["fill",0,0,0,0,0,0,0,0],["fill",0,0,0,0,0,0,0,0],["fill",0,0,0,0,0,0,0,0],["fill",0,0,0,0,0,0,0,0],["fill",0,0,0,0,0,0,0,0],["fill",0,0,0,0,0,0,0,0],["fill",0,0,0,0,0,0,0,0],["fill",0,0,0,0,0,0,0,0]]

#gets all user input and sets them to variables
user=input("Input: ")
user=user.split(" ")
list1=[]
list2=[]
rowsOn=int(user[0])
amount=int(user[rowsOn+1])
for i in range(1,rowsOn+1):
    list1.append(user[i])
for i in range(1,amount+1):
    list2.append(user[rowsOn+1+i])
    

for i in range(len(list1)):
    row=int(list1[i][0])
    for j in range(1,len(list1[i])):
        column=int(list1[i][j])
        board[row][column]=1
    
for i in range(len(list2)):
    row=int(list2[i][0])
    column=int(list2[i][1])
    try:
        if row > 8 or column > 8 or row < 1 or column < 1:
            pass
        else:
            if board[row][column]==0:
                board[row][column]=1
            else:
                board[row][column]=0
    except:
        pass
    try:
        if row > 8 or column+1 > 8 or row < 1 or column+1 < 1:
            pass
        else:
            if board[row][column+1]==0:
                board[row][column+1]=1
            else:
                board[row][column+1]=0
    except:
        pass
    try:
        if row > 8 or column+2 > 8 or row < 1 or column+2 < 1:
            pass
        else:
            if board[row][column+2]==0:
                board[row][column+2]=1
            else:
                board[row][column+2]=0
    except:
        pass
    try:
        if row > 8 or column-1 > 8 or row < 1 or column-1 < 1:
            pass
        else:
            if board[row][column-1]==0:
                board[row][column-1]=1
            else:
                board[row][column-1]=0
    except:
        pass
    try:
        if row > 8 or column-2 > 8 or row < 1 or column-2 < 1:
            pass
        else:
            if board[row][column-2]==0:
                board[row][column-2]=1
            else:
                board[row][column-2]=0
    except:
        pass
    try:
        if row+1 > 8 or column > 8 or row+1 < 1 or column < 1:
            pass
        else:
            if board[row+1][column]==0:
                board[row+1][column]=1
            else:
                board[row+1][column]=0
    except:
        pass
    try:
        if row+1 > 8 or column-1 > 8 or row+1 < 1 or column-1 < 1:
            pass
        else:
            if board[row+1][column-1]==0:
                board[row+1][column-1]=1
            else:
                board[row+1][column-1]=0
    except:
        pass
    try:
        if row+1 > 8 or column+1 > 8 or row+1 < 1 or column+1 < 1:
            pass
        else:
            if board[row+1][column+1]==0:
                board[row+1][column+1]=1
            else:
                board[row+1][column+1]=0
    except:
        pass
    try:
        if row+2 > 8 or column > 8 or row+2 < 1 or column < 1:
            pass
        else:
            if board[row+2][column]==0:
                board[row+2][column]=1
            else:
                board[row+2][column]=0
    except:
        pass
    try:
        if row-1 > 8 or column > 8 or row-1 < 1 or column < 1:
            pass
        else:
            if board[row-1][column]==0:
                board[row-1][column]=1
            else:
                board[row-1][column]=0
    except:
        pass
    try:
        if row-1 > 8 or column+1 > 8 or row-1 < 1 or column+1 < 1:
            pass
        else:
            if board[row-1][column+1]==0:
                board[row-1][column+1]=1
            else:
                board[row-1][column+1]=0
    except:
        pass
    try:
        if row-1 > 8 or column-1 > 8 or row-1 < 1 or column-1 < 1:
            pass
        else:
            if board[row-1][column-1]==0:
                board[row-1][column-1]=1
            else:
                board[row-1][column-1]=0
    except:
        pass
    try:
        if row-2 > 8 or column > 8 or row-2 < 1 or column < 1:
            pass
        else:
            if board[row-2][column]==0:
                board[row-2][column]=1
            else:
                board[row-2][column]=0
    except:
        pass
count=0
for i in range(1,9):
    for j in range(1,9):
        if board[i][j]==1:
            count=count+1
print(count)

    
    
    
#2 434 523 1 43
#1 58 1 58
#1 58 1 57
#3 32 44 56 2 54 18
#4 345 456 567 678 2 36 55