"""
This code is a remake of the game Spelling Bee, it is coded using pygame and uses the work of buttons cursor positons and pygame graphics to perform all takes
required in playing the Spelling Bee game.
"""

#Imports the language pygame into Idle
import pygame
#Imports sys used to exit or quit the code
import sys
#imports time used to keep a time background and to make clicks and frames
import time
#imports random, used to get random numbers which are used to chose a random game set
import random

#manditory pygame setup
pygame.init()


#A Button class Setup as a smoothed rectangle taking in needed parameters that creat a Button object which has 2 method is_clicked and draw paired with each.
#This made creating and using buttons a lot easier throughout the code.
class Button:
    #constuctor for button class
    def __init__(self, x, y, width, height, text, font_size=15, bg_color=("lightgrey"), text_color=("black"), outline_thickness=2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.bg_color = bg_color
        self.text_color = text_color
        self.outline_thickness = outline_thickness
    #draw method, uses pygame.draw to create the buttons image
    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.width, self.height), border_radius=10, width=self.outline_thickness)
        font = pygame.font.SysFont("Arial", self.font_size, bold=False)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        surface.blit(text, text_rect)
    #is clicked method done using mouse_pos which gets the x and y coordinates of the mouse
    def is_clicked(self, mouse_pos):
        return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height
    
#This function was used to find the coordinates of each hexagon this was done by utilizing python turtle but was then taken out once the points were found
"""
def hexMaker(point):
    tracer(0)
    list1=[]
    penup()
    setposition(point)
    for i in range(6):
        forward(50)
        list1.append((xcor(),ycor()))
        backward(50)
        right(60)
    tracer(1)
    return list1
"""

#Function to draw text to the screen, takes in text, font, and an coordinate x and y
def draw_text(text, font, text_color, x,y):
    image = font.render(text, True, text_color,)
    screen.blit(image,(x,y))

#Used paired with the enter button to check the word through the scoring system
def score_check(word):
    global score
    word=word.upper()
    if len(word)==4:
        score = score + 1
    elif len(word) > 4:
        score = score + len(word)
        if word.find(letter[0])!=-1 and word.find(letter[1])!=-1 and word.find(letter[2])!=-1 and word.find(letter[3])!=-1 and word.find(letter[4])!=-1 and word.find(letter[5])!=-1 and word.find(letter[6])!=-1:
            score = score + 7
            
#Used with every word in the list to find the total score of the games set
def score_total(word):
    global total
    word=word.upper()
    if len(word)==4:
        total = total + 1
    elif len(word) > 4:
        total = total + len(word)
        if word.find(letter[0])!=-1 and word.find(letter[1])!=-1 and word.find(letter[2])!=-1 and word.find(letter[3])!=-1 and word.find(letter[4])!=-1 and word.find(letter[5])!=-1 and word.find(letter[6])!=-1:
            total = total + 7
#A function that is checking the users score and displaying the score bar on the left side of the screen. Updating after every event and changes the displayed
#text according the players score
def score_draw(points):
    percent=(((points*1.0)/(total*1.0))*100.0)
    
    if percent < 2:
        pygame.draw.circle(screen,"yellow", (45,366.66),13)
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        draw_text("Beginner",text_font,("black"),20,380)

        text_font = pygame.font.SysFont("Arial",12)
        #Used to center the score on the drawn area
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,359)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,359)
        else:
            draw_text(str(score),text_font,("black"),38.5,359)
            
       #drawing each word label and color values of the score bar for each different percent area 
    elif percent >=2 and percent<5:

        pygame.draw.rect(screen,("white"), (30,90,50,373))
        
        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,333.33),5)
        pygame.draw.circle(screen,"lightgrey", (45,300),5)
        pygame.draw.circle(screen,"lightgrey", (45,266.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,233.33),5)
        pygame.draw.circle(screen,"lightgrey", (45,200),5)
        pygame.draw.circle(screen,"lightgrey", (45,166.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,133.33),5)
        pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top

        
        pygame.draw.circle(screen,"yellow", (45,333.33),13)
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))
        draw_text("Good Start",text_font,("black"),19,380)

        text_font = pygame.font.SysFont("Arial",12)
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,325.67)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,325.67)
        else:
            draw_text(str(score),text_font,("black"),38.5,325.67)
            
    elif percent >=5 and percent<8:
        pygame.draw.rect(screen,("white"), (30,90,50,373))

        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"yellow", (45,333.33),5)
        pygame.draw.circle(screen,"lightgrey", (45,300),5)
        pygame.draw.circle(screen,"lightgrey", (45,266.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,233.33),5)
        pygame.draw.circle(screen,"lightgrey", (45,200),5)
        pygame.draw.circle(screen,"lightgrey", (45,166.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,133.33),5)
        pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top

        
        pygame.draw.circle(screen,"yellow", (45,300),13)
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))
        draw_text("Moving Up",text_font,("black"),20,380)

        text_font = pygame.font.SysFont("Arial",12)
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,292.34)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,292.34)
        else:
            draw_text(str(score),text_font,("black"),38.5,292.34)
    elif percent >=8 and percent<15:
        pygame.draw.rect(screen,("white"), (30,90,50,373))

        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"yellow", (45,333.33),5)
        pygame.draw.circle(screen,"yellow", (45,300),5)
        pygame.draw.circle(screen,"lightgrey", (45,266.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,233.33),5)
        pygame.draw.circle(screen,"lightgrey", (45,200),5)
        pygame.draw.circle(screen,"lightgrey", (45,166.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,133.33),5)
        pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top

        
        pygame.draw.circle(screen,"yellow", (45,266.66),13)
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))
        draw_text("Good",text_font,("black"),28,380)

        text_font = pygame.font.SysFont("Arial",12)
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,259)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,259)
        else:
            draw_text(str(score),text_font,("black"),38.5,259)
    elif percent >=15 and percent<25:
        pygame.draw.rect(screen,("white"), (30,90,50,373))

        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"yellow", (45,333.33),5)
        pygame.draw.circle(screen,"yellow", (45,300),5)
        pygame.draw.circle(screen,"yellow", (45,266.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,233.33),5)
        pygame.draw.circle(screen,"lightgrey", (45,200),5)
        pygame.draw.circle(screen,"lightgrey", (45,166.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,133.33),5)
        pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top

        
        pygame.draw.circle(screen,"yellow", (45,233.33),13)
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))
        draw_text("Solid",text_font,("black"),21,380)

        text_font = pygame.font.SysFont("Arial",12)
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,225.67)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,225.67)
        else:
            draw_text(str(score),text_font,("black"),38.5,225.67)
    elif percent >=25 and percent<40:
        pygame.draw.rect(screen,("white"), (30,90,50,373))

        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"yellow", (45,333.33),5)
        pygame.draw.circle(screen,"yellow", (45,300),5)
        pygame.draw.circle(screen,"yellow", (45,266.66),5)
        pygame.draw.circle(screen,"yellow", (45,233.33),5)
        pygame.draw.circle(screen,"lightgrey", (45,200),5)
        pygame.draw.circle(screen,"lightgrey", (45,166.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,133.33),5)
        pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top

        
        pygame.draw.circle(screen,"yellow", (45,200),13)
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))
        draw_text("Nice",text_font,("black"),23,380)

        text_font = pygame.font.SysFont("Arial",12)
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,192.34)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,192.34)
        else:
            draw_text(str(score),text_font,("black"),38.5,192.34)
    elif percent >=40 and percent<50:
        pygame.draw.rect(screen,("white"), (30,90,50,373))

        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"yellow", (45,333.33),5)
        pygame.draw.circle(screen,"yellow", (45,300),5)
        pygame.draw.circle(screen,"yellow", (45,266.66),5)
        pygame.draw.circle(screen,"yellow", (45,233.33),5)
        pygame.draw.circle(screen,"yellow", (45,200),5)
        pygame.draw.circle(screen,"lightgrey", (45,166.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,133.33),5)
        pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top

        
        pygame.draw.circle(screen,"yellow", (45,166.66),13)
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))
        draw_text("Great",text_font,("black"),21,380)

        text_font = pygame.font.SysFont("Arial",12)
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,159)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,159)
        else:
            draw_text(str(score),text_font,("black"),38.5,159)
    elif percent >=50 and percent<70:
        pygame.draw.rect(screen,("white"), (30,90,50,373))

        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"yellow", (45,333.33),5)
        pygame.draw.circle(screen,"yellow", (45,300),5)
        pygame.draw.circle(screen,"yellow", (45,266.66),5)
        pygame.draw.circle(screen,"yellow", (45,233.33),5)
        pygame.draw.circle(screen,"yellow", (45,200),5)
        pygame.draw.circle(screen,"yellow", (45,166.66),5)
        pygame.draw.circle(screen,"lightgrey", (45,133.33),5)
        pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top

        
        pygame.draw.circle(screen,"yellow", (45,133.33),13)
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))
        draw_text("Amazing",text_font,("black"),18,380)

        text_font = pygame.font.SysFont("Arial",12)
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,125.67)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,125.67)
        else:
            draw_text(str(score),text_font,("black"),38.5,125.67)
    elif percent >=70 and percent<100:
        pygame.draw.rect(screen,("white"), (30,90,50,373))

        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"yellow", (45,333.33),5)
        pygame.draw.circle(screen,"yellow", (45,300),5)
        pygame.draw.circle(screen,"yellow", (45,266.66),5)
        pygame.draw.circle(screen,"yellow", (45,233.33),5)
        pygame.draw.circle(screen,"yellow", (45,200),5)
        pygame.draw.circle(screen,"yellow", (45,166.66),5)
        pygame.draw.circle(screen,"yellow", (45,133.33),5)
        pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top

        pygame.draw.rect(screen,("yellow"), (35,90,20,20))

        

        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))
        draw_text("Genius",text_font,("black"),20,380)

        text_font = pygame.font.SysFont("Arial",12)
        if score<10:
            draw_text(str(score),text_font,("black"),43.5,92.34)
        elif score>=10 and score<100:
            draw_text(str(score),text_font,("black"),41,92.34)
        else:
            draw_text(str(score),text_font,("black"),38.5,92.34)
    elif keeper==keeper1:
        pygame.draw.rect(screen,("white"), (30,90,50,373))

        pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
        pygame.draw.circle(screen,"yellow", (45,366.66),5)
        pygame.draw.circle(screen,"yellow", (45,333.33),5)
        pygame.draw.circle(screen,"yellow", (45,300),5)
        pygame.draw.circle(screen,"yellow", (45,266.66),5)
        pygame.draw.circle(screen,"yellow", (45,233.33),5)
        pygame.draw.circle(screen,"yellow", (45,200),5)
        pygame.draw.circle(screen,"yellow", (45,166.66),5)
        pygame.draw.circle(screen,"yellow", (45,133.33),5)
        pygame.draw.rect(screen,("yellow"), (40,95,10,10)) #top

        pygame.draw.rect(screen,("yellow"), (35,90,20,20)) #top
        text_font = pygame.font.SysFont("Arial",12,bold=True)
        
        pygame.draw.rect(screen,("white"), (20,380,45,400))

        text_font = pygame.font.SysFont("Arial",150)
        draw_text("Queen Bee",text_font,("black"),25,25)
        if keeper==keeper1:
            screen.fill("white")
            text_font = pygame.font.SysFont("Arial",100)
            draw_text("Queen Bee",text_font,("black"),25,100)
            pygame.display.flip()
            pygame.time.delay(15000)
            pygame.quit()
            sys.exit()
            





#setup
size = width, height = 500,500
screen = pygame.display.set_mode(size)
#sets font style
text_font = pygame.font.SysFont("Arial",30,bold=True)



#found list of all the hexagon points 
listhex = [[(300.0, 250.0), (275.0, 206.698729811), (225.0, 206.698729811), (200.0, 250.0), (225.0, 293.301270189), (275.0, 293.301270189)],
           [(382.0, 202.0), (357.0, 158.698729811), (307.0, 158.698729811), (282.0, 202.0), (307.0, 245.301270189), (357.0, 245.301270189)],
           [(382.0, 296.0), (357.0, 252.698729811), (307.0, 252.698729811), (282.0, 296.0), (307.0, 339.301270189), (357.0, 339.301270189)],
           [(300.0, 344.0), (275.0, 300.698729811), (225.0, 300.698729811), (200.0, 344.0), (225.0, 387.301270189), (275.0, 387.301270189)],
           [(218.0, 296.0), (193.0, 252.698729811), (143.0, 252.698729811), (118.0, 296.0), (143.0, 339.301270189), (193.0, 339.301270189)],
           [(218.0, 202.0), (193.0, 158.698729811), (143.0, 158.698729811), (118.0, 202.0), (143.0, 245.301270189), (193.0, 245.301270189)],
           [(300.0, 156.0), (275.0, 112.698729811), (225.0, 112.698729811), (200.0, 156.0), (225.0, 199.301270189), (275.0, 199.301270189)]]  
    
#Used to create the list above but, easier to see just copy and pasted
"""
listhex.append(hexMaker((250,250)))#m
listhex.append(hexMaker((332,202)))#tr
listhex.append(hexMaker((332,296)))#br
listhex.append(hexMaker((250,344)))#bm
listhex.append(hexMaker((168,296)))#bl
listhex.append(hexMaker((168,202)))#tl
listhex.append(hexMaker((250,156)))#tm
"""

#Sets empty variable to use 
words=[]
keeper=0
score=0
found=[]
letter=[]
end_words=[]

#All middle cords for the hexagons
middle_cords=[(250,250),(332,202),(332,296),(250,344),(168,296),(168,202),(250,156)]

#setting button objects
Enter = Button(300, 420, 75, 45, "Enter",outline_thickness=1)
Delete = Button(125, 420, 75, 45, "Delete",outline_thickness=1)
guessed_words = Button(400, 30, 90, 25, "Gussed Words",outline_thickness=1)
end_game = Button(25,25,45,30,"Quit")
quit_game = Button(150,300,200,100,"Close")

#Importting images same concept as creating the button objects but for the image of a cycle
cycle_image = pygame.image.load("TheCycle.png")
cycle_image = pygame.transform.scale(cycle_image, (25, 25))

#More set variables
button_radius = 23
button_x = 250
button_y = 445
answer = ""
entered = False
timer = pygame.time.get_ticks()
total=0
hexagon_size = 50
hexagon_color = (255,0,0)
clicked_hexagons = []

#Used to pick a random set by chosing the number at the index and going to that assorted Game file
randomlist=[1,2,3,4,5]
random_number=random.choice(randomlist)
if random_number==1:
    
    with open('Game1.txt', 'r')as file:
        keep=0
        keeper1=0
        for line in file:
            line = line.strip()
            if keep == 0:
                letter=list(line)
                keep = 1
            else:
                keeper1=keeper1+1
                score_total(line)
                words.append(str(line.upper()))
elif random_number==2:
    with open('Game2.txt', 'r')as file:
        keep=0
        keeper1=0
        for line in file:
            line = line.strip()
            if keep == 0:
                letter=list(line)
                keep = 1
            else:
                keeper1=keeper1+1
                score_total(line)
                words.append(str(line.upper()))
elif random_number==3:
    with open('Game3.txt', 'r')as file:
        keep=0
        keeper1=0
        for line in file:
            line = line.strip()
            if keep == 0:
                letter=list(line)
                keep = 1
            else:
                keeper1=keeper1+1
                score_total(line)
                words.append(str(line.upper()))
elif random_number==4:
    with open('Game4.txt', 'r')as file:
        keep=0
        keeper1=0
        for line in file:
            line = line.strip()
            if keep == 0:
                letter=list(line)
                keep = 1
            else:
                keeper1=keeper1+1
                score_total(line)
                words.append(str(line.upper()))
elif random_number==5:
    with open('Game5.txt', 'r')as file:
        keep=0
        keeper1=0
        for line in file:
            line = line.strip()
            if keep == 0:
                letter=list(line)
                keep = 1
            else:
                keeper1=keeper1+1
                score_total(line)
                words.append(str(line.upper()))




#Start of the game loop
while 1:
    #manditory pygame setup
    clock = pygame.time.Clock()
    # Limit to 60 frames per second
    clock.tick(60)
    #manditory pygame setup
    for event in pygame.event.get():
        #manditory pygame setup
        if event.type == pygame.QUIT: sys.exit()

        #Runs everytime a mouse click is activated
        if event.type == pygame.MOUSEBUTTONDOWN:
            #gets the cursors mouse coordinates (x,y)
            mouse_pos = pygame.mouse.get_pos()

            #Loops through the given hexagon coordinates in the format of a list in a list as tuples
            for i, hexagon_points in enumerate(listhex):
                #draws the hexagon border then checks the border (polygon) with the mouse position if the mouse position is in the area adds the letter clicked
                is_within_hexagon = pygame.draw.polygon(screen, (0, 255, 0), hexagon_points).collidepoint(*mouse_pos)

                if is_within_hexagon:
                    
                    answer=answer+letter[i]
                    
            #if statments checking for each button condition, if matches performs the actions
                    
            #Enter button, eneters the users inutted letters
            if Enter.is_clicked(pygame.mouse.get_pos()):
                entered = True
            #Delete button,removes a character from the users inputs
            if Delete.is_clicked(pygame.mouse.get_pos()):
                answer = answer[:(len(answer)-1)]
            #Recycle button,cycles the letters to the user
            if pygame.Rect(button_x - button_radius, button_y - button_radius, button_radius * 2, button_radius * 2).collidepoint(pygame.mouse.get_pos()):
                text_font = pygame.font.SysFont("Arial",30,bold=True)
                recycle=[]
                getter=[0,1,2,3,4,5]
                for i in range(1,7):
                    recycle.append(letter[i])
                for i in range(6):
                    letter.pop(1)
                
                for i in range(6):
                    index = random.choice(getter)
                    popping=getter.index(index)
                    getter.pop(popping)
                    letter.append(recycle[index])
                    
                for i in range(7):
                    draw_text(letter[i], text_font,("black"), middle_cords[i][0]-8,middle_cords[i][1]-18)
            #Guessed words button, shows the user all the words they have guessed
            if guessed_words.is_clicked(pygame.mouse.get_pos()):
                screen.fill("white")


                text_font = pygame.font.SysFont("Arial",50)
                draw_text("Guessed Words",text_font,("black"),100,5)
                pygame.draw.line(screen,"black", (40,55),(470,55),3)
                x_axis = 40
                y_axis = 60
                text_font = pygame.font.SysFont("Arial",15)
                for i in range(len(found)):
                    draw_text(found[i],text_font,("black"),x_axis,y_axis)
                    x_axis = x_axis + ((len(found[i])*8)+10)
                    if x_axis+10+(len(found[i]*8))>=475:
                        x_axis = 40
                        y_axis = y_axis + 20
                    
                    
                pygame.display.flip()
                pygame.time.delay(3000)
            #Quit button, Shows the user the rest of the words and ends the game
            if end_game.is_clicked(pygame.mouse.get_pos()):
                for i in range(len(words)):
                    if words[i] in found:
                        continue
                    else:
                        end_words.append(words[i])

                screen.fill("white")
                text_font = pygame.font.SysFont("Arial",50)
                draw_text("Words Not Guessed",text_font,("black"),70,5)
                pygame.draw.line(screen,"black", (40,55),(470,55),3)
                x_axis = 40
                y_axis = 60
                text_font = pygame.font.SysFont("Arial",15)
                for i in range(len(end_words)):
                    draw_text(end_words[i],text_font,("black"),x_axis,y_axis)
                    x_axis = x_axis + ((len(end_words[i])*8)+10)
                    if x_axis+10+(len(end_words[i]*8))>=475:
                        x_axis = 40
                        y_axis = y_axis + 20
                quit_game.draw(screen)
                pygame.display.flip()
                pygame.time.delay(10000)
                if quit_game.is_clicked(pygame.mouse.get_pos()):
                    sys.exit()
                    pygame.quit()
                
            
        


            

    #Event

                    
    #Starts the screens imaging
    screen.fill("white")

    
    #Draws the buttons to the user using the button class methods
    Enter.draw(screen)
    Delete.draw(screen)
    guessed_words.draw(screen)
    end_game.draw(screen)
    screen.blit(cycle_image, (237,433))
    pygame.draw.circle(screen,"lightgrey",(250,445),25,width=1)
    #user display
    shift=0
    #score bar
    pygame.draw.line(screen,"lightgrey", (45,100),(45,366.66),3)#bottom
    pygame.draw.circle(screen,"lightgrey", (45,366.66),5)
    pygame.draw.circle(screen,"lightgrey", (45,333.33),5)
    pygame.draw.circle(screen,"lightgrey", (45,300),5)
    pygame.draw.circle(screen,"lightgrey", (45,266.66),5)
    pygame.draw.circle(screen,"lightgrey", (45,233.33),5)
    pygame.draw.circle(screen,"lightgrey", (45,200),5)
    pygame.draw.circle(screen,"lightgrey", (45,166.66),5)
    pygame.draw.circle(screen,"lightgrey", (45,133.33),5)
    pygame.draw.rect(screen,("lightgrey"), (40,95,10,10)) #top
    score_draw(score)
    #centers the numbers according to their lengths
    for i in range(len(answer)):
        shift=shift+7.5
    draw_text(answer,text_font,("black"),250-shift,50)

    text_font = pygame.font.SysFont("Arial",30,bold=True)
    for i in range(7):
        if i==0:
            pygame.draw.polygon(screen,"yellow",listhex[i])
        else:
            pygame.draw.polygon(screen,"gainsboro",listhex[i])
    for i in range(7):
        draw_text(letter[i], text_font,("black"), middle_cords[i][0]-8,middle_cords[i][1]-18)

    #If user clickes the enter button
    if entered == True:
        #Checks for bad user answers, too short, no middle letter, not a word
        if len(answer)<= 3:
            pygame.draw.rect(screen,("black"), (225,15,50,35),border_radius = 10)
            text_font = pygame.font.SysFont("Arial",12,bold=True)
            draw_text("Too short",text_font,("white"),229,25)
            pygame.display.flip()
            pygame.time.delay(800)
            pygame.draw.rect(screen,("white"), (225,15,50,2))
            entered = False
            answer = ""
        elif answer.find(letter[0]) == -1:
            pygame.draw.rect(screen,("black"), (202,15,105,35),border_radius = 10)
            text_font = pygame.font.SysFont("Arial",12,bold=True)
            draw_text("Missing center letter",text_font,("white"),209,25)
            pygame.display.flip()
            pygame.time.delay(800)
            pygame.draw.rect(screen,("white"), (225,15,75,2))
            entered = False
            answer = ""
        elif answer not in words:
            pygame.draw.rect(screen,("black"), (202,15,100,35),border_radius = 10)
            text_font = pygame.font.SysFont("Arial",12,bold=True)
            draw_text("Not in word list",text_font,("white"),214,25)
            pygame.display.flip()
            pygame.time.delay(800)
            pygame.draw.rect(screen,("white"), (225,15,75,2))
            entered = False
            answer = ""
        elif answer in found:
            pygame.draw.rect(screen,("black"), (220,15,75,35),border_radius = 10)
            text_font = pygame.font.SysFont("Arial",12,bold=True)
            draw_text("Already found",text_font,("white"),224,25)
            pygame.display.flip()
            pygame.time.delay(800)
            pygame.draw.rect(screen,("white"), (225,15,50,2))
            entered = False
            answer = ""
        #if it passes runs the else stament which adds the list to found and updates the score accordinly while telling the user
        else:
            keeper=keeper+1
            found.append(answer)
            score_check(answer)
            score_draw(score)
            pygame.draw.rect(screen,("black"), (231,15,30,35),border_radius = 10)
            text_font = pygame.font.SysFont("Arial",12,bold=True)
            draw_text("Nice!",text_font,("white"),235,25)
            pygame.display.flip()
            pygame.time.delay(800)
            pygame.draw.rect(screen,("white"), (225,15,50,2))
            entered = False
            answer = ""

            
            
    
        
    
    
    
    
    
    pygame.display.flip()