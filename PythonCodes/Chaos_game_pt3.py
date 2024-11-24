tracer(0)
import random
penup()
setposition(-150,0)
pendown()
setposition(-75,-130)
setposition(75,-130)
setposition(150,0)
setposition(75,130)
setposition(-75,130)
setposition(-150,0)
start1=(-150,0)
start2=(-75,-130)
start3=(75,-130)
start4=(150,0)
start5=(75,130)
start6=(-75,130)

x=[1,2,3,4,5,6]
cur=(-150,0)
listend=[]
for i in range(50000):
    while True:
        num=random.choice(x)
        listend.append(num)
        
        if len(listend)<=1:
            break
        if listend[-1]==listend[-2]:
            continue
        else:
            break
    
    if num==1:
        x1=(cur[0]+start1[0])/2
        y1=(cur[1]+start1[1])/2
        cur=(x1,y1)
        penup()
        setposition(x1,y1)
        pendown()
        circle(.25)
    elif num==2:
        x1=(cur[0]+start2[0])/2
        y1=(cur[1]+start2[1])/2
        cur=(x1,y1)
        penup()
        setposition(x1,y1)
        pendown()
        circle(.25)
    elif num==3:
        x1=(cur[0]+start3[0])/2
        y1=(cur[1]+start3[1])/2
        cur=(x1,y1)
        penup()
        setposition(x1,y1)
        pendown()
        circle(.25)
    elif num==4:
        x1=(cur[0]+start4[0])/2
        y1=(cur[1]+start4[1])/2
        cur=(x1,y1)
        penup()
        setposition(x1,y1)
        pendown()
        circle(.25)
    elif num==5:
        x1=(cur[0]+start5[0])/2
        y1=(cur[1]+start5[1])/2
        cur=(x1,y1)
        penup()
        setposition(x1,y1)
        pendown()
        circle(.25)
    elif num==6:
        x1=(cur[0]+start6[0])/2
        y1=(cur[1]+start6[1])/2
        cur=(x1,y1)
        penup()
        setposition(x1,y1)
        pendown()
        circle(.25)
        
tracer(1)