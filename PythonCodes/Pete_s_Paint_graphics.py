graph=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def paint(format):
    color=format[0]
    start=int(format[1])
    startx=int(format[2],16)
    starty=int(format[3],16)
    length=int(format[4],16)
    height=int(format[5],16)
    
    
    graph[15-starty][startx]=color
    starty=15-starty
    
    
    x=startx
    
    for i in range(length):
        for j in range(height):
            
            if start==1:
                try:
                    graph[starty+j][x+i]=color
                except:
                    starty=starty-16
                    try:
                        graph[starty+j][x+i]=color
                    except:
                        x=x-16
                        graph[starty+j][x+i]=color
            elif start==2:
                try:
                    graph[starty+j][x-i]=color
                except:
                    starty=starty-16
                    try:
                        graph[starty+j][x-i]=color
                    except:
                        x=x-16
                        graph[starty+j][x-i]=color
                            
            elif start==3:
                try:
                    graph[starty-j][x-i]=color
                except:
                    starty=starty-16
                    try:
                        graph[starty-j][x-i]=color
                    except:
                        x=x-16
                        graph[starty-j][x-i]=color
            elif start==4:
                try:
                    graph[starty-j][x+i]=color
                except:
                    starty=starty-16
                    try:
                        graph[starty-j][x+i]=color
                    except:
                        x=x-16
                        graph[starty-j][x+i]=color
    
    tracer(0)
    fixGrid()
    penup()
    setposition(-160,160)
    pendown()
    for i in range(16):
        for j in range(16):
            if graph[i][j]=="R":
                box("red")
            elif graph[i][j]=="O":
                box("orange")
            elif graph[i][j]=="Y":
                box("yellow")
            elif graph[i][j]=="G":
                box("green")
            elif graph[i][j]=="B":
                box("blue")
            elif graph[i][j]=="I":
                box("indigo")
            elif graph[i][j]=="V":
                box("violet")
            else:
                box("black")
            penup()
            forward(20)
            pendown()
        penup()
        right(180)
        forward(320)
        left(90)
        forward(20)
        left(90)
        pendown()
        
        
    penup()
    setposition(-160,160)
    pendown()
    pensize(2)
    
    for i in range(16):
        for j in range(16):
            
            box1()
            penup()
            forward(20)
            pendown()
        penup()
        right(180)
        forward(320)
        left(90)
        forward(20)
        left(90)
        pendown()
    
    tracer(1)
    user=input("Continue?")

def observe(choice):
    count=0
    for i in range(16):
        for j in range(16):
            if graph[i][j]==choice:
                count=count+1
    if choice=="R":
        co="Red"
    elif choice=="O":
        co="Orange"
    elif choice=="Y":
        co="Yellow"
    elif choice=="G":
        co="Green"
    elif choice=="B":
        co="Blue"
    elif choice=="I":
        co="Indigo"
    elif choice=="V":
        co="Violet"
    return (str(co)+": "+str(count))
    
    
  
def pete(directions):
    for i in range(len(directions)):
        if directions[i][0]=="PAINT":
            paint(directions[i][1])
        else:
            print(observe(directions[i][1]))
def fixGrid():
    for i in range(16):
        for j in range(16):
            color=("black")
            box1()
def box1():
    for i in range(4):
        forward(20)
        right(90)
def box(col):
    color(col)
    if col=="black":
        pass
    else:
        begin_fill()
    for i in range(4):
        forward(20)
        right(90)
    end_fill()
    
        
tracer(0)
penup()
setposition(-160,160)
pendown()


for i in range(16):
    for j in range(16):
        box1()
        penup()
        forward(20)
        pendown()
    penup()
    right(180)
    forward(320)
    left(90)
    forward(20)
    left(90)
    pendown()
tracer(1)

#pete([["PAINT","G13A45"],["PAINT","B16B22"],["OBSERVE","G"]])
#pete([["PAINT","Y3CE33"],["OBSERVE","Y"],["PAINT","B1AAAA"]])

#pete([["PAINT","R2FF83"],["PAINT","B377AA"],["OBSERVE","R"],["PAINT","Y12345"]])
pete([["PAINT","B24A27"],["PAINT","Y12345"],["PAINT","V324E6"],["PAINT","R23389"],["PAINT","O18811"],["OBSERVE","O"],["OBSERVE","V"],["OBSERVE","G"]])