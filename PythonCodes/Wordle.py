#from turtle import*
tracer(0)
def box():
    color("lightgrey")
    begin_fill()
    forward(35)
    for i in range(90):
        forward(.05)
        left(1)
    forward(40)
    for i in range(90):
        forward(.05)
        left(1)
    forward(35)
    for i in range(90):
        forward(.05)
        left(1)
    forward(40)
    for i in range(90):
        forward(.05)
        left(1)
    end_fill()
    
penup()
setposition(-220,-150)
pendown()
letters="qwertyuiop"
letters=list(letters)
for i in range(10):
    pendown()
    box()
    penup()
    color("black")
    forward(19)
    left(90)
    forward(17)
    pendown()

    write(letters[i],align="center",font=("ariel",12))
    penup()
    right(180)
    forward(17)
    left(90)
    
    forward(26)
    pendown()
    
penup()
setposition(-195,-200)
pendown()
letters1="asdfghjkl"
letters1=list(letters1)
for i in range(9):
    pendown()
    box()
    penup()
    color("black")
    forward(19)
    left(90)
    forward(17)
    pendown()

    write(letters1[i],align="center",font=("ariel",12))
    penup()
    right(180)
    forward(17)
    left(90)
    
    forward(26)
    pendown()
    

tracer(1)