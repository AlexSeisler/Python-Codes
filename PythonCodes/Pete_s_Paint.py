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
                    x=x-16
                    graph[starty+j][x+i]=color
            elif start==2:
                try:
                    graph[starty+j][x-i]=color
                except:
                    x=x+16
                    graph[starty+j][x-i]=color
            elif start==3:
                try:
                    graph[starty-j][x-i]=color
                except:
                    x=x+16
                    graph[starty-j][x-i]=color
            elif start==4:
                try:
                    graph[starty-j][x+i]=color
                except:
                    x=x-16
                    graph[starty-j][x+i]=color

    

def observe(choice):
    count=0
    for i in range(16):
        for j in range(16):
            if graph[i][j]==choice:
                count=count+1
    return count
    
    
  
def pete(directions):
    for i in range(len(directions)):
        if directions[i][0]=="PAINT":
            paint(directions[i][1])
        else:
            print(observe(directions[i][1]))

pete([["PAINT","G13A45"],["PAINT","B16B22"],["OBSERVE","G"]])
pete([["PAINT","Y3CE33"],["PAINT","R1FF99"],["OBSERVE","Y"]])