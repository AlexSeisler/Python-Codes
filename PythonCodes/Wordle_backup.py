from turtle import*
def box():
    pendown()
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
def darkbox():
    pendown()
    color("darkgrey")
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
def yellowbox():
    pendown()
    color("yellow")
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
def greenbox():
    pendown()
    color("lightgreen")
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
def top():
    pensize(2)
    penup()
    setposition(-123,yy)
    pendown()
    for i in range(5):
        for i in range(4):
            forward(45)
            left(90)
        penup()
        forward(50)
        pendown()


count4=0
def top1():
    tracer(0)
    global count4
    count4=count4+55
    turn=235
    turn=turn-count4
    penup()
    turn
    setposition(-123,turn)
    turn=turn-50
    pendown()
    check4=[]
    
    #for i in range(6):
        #check4.append(answer[i])
    for i in range(5):
        color("black")
        forward(22.5)
        if guess[i]==answer[i]:
            color("lightgreen")
            #check4.pop(i)
            begin_fill()
        elif guess[i] in answer:
            color("yellow")
            begin_fill()
        else:

            color("darkgrey")
            begin_fill()
        
        penup()
        left(90)
        forward(12.5)
        color("black")
        write(guess[i],align="center",font=("Helvetica Neue",10))
        if guess[i]==answer[i]:
            color("lightgreen")
        elif guess[i] in answer:
            color("yellow")
        else:

            color("darkgrey")
        right(180)
        forward(12.5)
        left(90)
        forward(22.5)
        left(90)
        for i in range(3):
            forward(45)
            left(90)
        end_fill()
        penup()
        forward(50)
        pendown()
    tracer(1)
tracer(0)


penup()
tracer(0)
setposition(-220,-150)
pendown()
letters="QWERTYUIOP"
letters=list(letters)
for i in range(10):
    
    pendown()
    box()
    
    penup()
    color("black")
    forward(19)
    left(90)
    forward(15)
    pendown()

    write(letters[i],align="center",font=("Helvetica Neue",10))
    penup()
    right(180)
    forward(15)
    left(90)
    
    forward(26)
    pendown()
    
    
penup()
setposition(-195,-200)
pendown()
letters1="ASDFGHJKL"
letters1=list(letters1)
for i in range(9):
    pendown()
    box()

    penup()
    color("black")
    forward(19)
    left(90)
    forward(15)
    pendown()

    write(letters1[i],align="center",font=("Helvetica Neue",10))
    penup()
    right(180)
    forward(15)
    left(90)
    
    forward(26)
    pendown()
penup()
setposition(-150,-250)
pendown()
letters2="ZXCVBNM"
letters2=list(letters2)
for i in range(7):
    pendown()
    box()
    penup()
    color("black")
    forward(19)
    left(90)
    forward(15)
    pendown()

    write(letters2[i],align="center",font=("Helvetica Neue",10))
    penup()
    right(180)
    forward(15)
    left(90)
    
    forward(26)
    pendown()
tracer(1)
tracer(0)








penup()
setposition(-220,-250)
pendown()
color("lightgrey")
begin_fill()
forward(30)
penup()
left(90)
forward(12.5)
pendown()
color("black")
write("ENTER",align="center",font=("Helvetica Neue",10))
color("lightgrey")
penup()
right(180)
forward(12.5)
left(90)
pendown()
forward(30)
for i in range(90):
    forward(.05)
    left(1)
forward(40)
for i in range(90):
    forward(.05)
    left(1)
forward(60)
for i in range(90):
    forward(.05)
    left(1)
forward(40)
for i in range(90):
    forward(.05)
    left(1)
end_fill()



penup()
setposition(165,-250)
pendown()
color("lightgrey")
begin_fill()
forward(28)
penup()
left(90)
forward(15)
pendown()
color("black")
right(90)
forward(12.5)
left(90)
forward(15)
left(90)
forward(12.5)
left(45)
forward(11)
left(90)
forward(11)
left(135)
pendown()
color("lightgrey")
penup()
right(180)
forward(14)
left(90)
pendown()
forward(32)
for i in range(90):
    forward(.05)
    left(1)
forward(40)
for i in range(90):
    forward(.05)
    left(1)
forward(60)
for i in range(90):
    forward(.05)
    left(1)
forward(40)
for i in range(90):
    forward(.05)
    left(1)
end_fill()

penup()
setposition(198,-228)
pendown()
color("black")
left(45)
for i in range(4):
    forward(4)
    backward(4)
    right(90)
right(45)
tracer(1)
tracer(0)
yy=180
for i in range(6):
    top()
    yy=yy-55

    

tracer(1)


no=[]
maybe=[]
yes=[]


answer=[]


import random
f=open("wordsfive1.txt","r")
words=f.readlines()
f.close()


answer=random.choice(words)
print(answer)
answer=answer.upper()
answer=list(answer)
total=len(answer)
for i in range(7):
    if i==6 and len(yes)!=5:
        print("You Lose")
        answer="".join(answer)
        print(("the word was: ")+str(answer[:5]))
        break
        
    guess=[]
    while True:
        user=""
        user= input("Enter a 5 letter word: ")
        user=user+"\n"
        if user in words:
            break
        else:
            print("invalid word")
            continue
        
    user=user.upper()
    for i in range(5):
        guess.append(user[i])

    for i in range(5):
        if guess[i]==answer[i]:
            yes.append(guess[i])
        elif guess[i] in answer:
            maybe.append(guess[i])
        else:
            no.append(guess[i])



    top1()
    yes = list(set(yes))
    maybe = list(set(maybe))
    no = list(set(no))
    
        


    
    penup()
    setposition(-220,-150)
    pendown()
    letters="QWERTYUIOP"
    letters=list(letters)
    tracer(0)
    for i in range(10):
        
        pendown()
        if letters[i] in yes:
            greenbox()
        elif letters[i] in maybe:
            yellowbox()
        elif letters[i] in no:
            darkbox()
        else:
            box()
        
        penup()
        color("black")
        forward(19)
        left(90)
        forward(15)
        pendown()

        write(letters[i],align="center",font=("Helvetica Neue",10))
        penup()
        right(180)
        forward(15)
        left(90)
        
        forward(26)
        pendown()
        
        
    penup()
    setposition(-195,-200)
    pendown()
    letters1="ASDFGHJKL"
    letters1=list(letters1)
    for i in range(9):
        pendown()
        if letters1[i] in yes:
            greenbox()
        elif letters1[i] in maybe:
            yellowbox()
        elif letters1[i] in no:
            darkbox()
        else:
            box()

        penup()
        color("black")
        forward(19)
        left(90)
        forward(15)
        pendown()

        write(letters1[i],align="center",font=("Helvetica Neue",10))
        penup()
        right(180)
        forward(15)
        left(90)
        
        forward(26)
        pendown()
    penup()
    setposition(-150,-250)
    pendown()
    letters2="ZXCVBNM"
    letters2=list(letters2)
    for i in range(7):
        pendown()
        if letters2[i] in yes:
            greenbox()
        elif letters2[i] in maybe:
            yellowbox()
        elif letters2[i] in no:
            darkbox()
        else:
            box()
        penup()
        color("black")
        forward(19)
        left(90)
        forward(15)
        pendown()

        write(letters2[i],align="center",font=("Helvetica Neue",10))
        penup()
        right(180)
        forward(15)
        left(90)
        
        forward(26)
        pendown()
    tracer(1)
    tracer(1)
    
    if guess[0]==answer[0] and guess[1]==answer[1]and guess[2]==answer[2] and guess[3]==answer[3] and guess[4]==answer[4]:
        print("You Win")
        break