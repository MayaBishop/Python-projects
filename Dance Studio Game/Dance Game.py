import pygame
import random
pygame.init()
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED   = (255,0, 0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
LIGHT_BLUE = (102,255,255)
###### All functions for main screen
#puts backgroung for main menu onto screen
def add_main_screen():
    fileName = "background for hall.png"
    background_surface = pygame.image.load(fileName)
    win.blit(background_surface,(0,0))

#creates polygons for all three doors
def create_doors():
    door1 = [(179,209),(248,175),(262,385),(197,446),BLACK,1,1]#
    door2 = [(624,207),(607,447),(542,384),(554,174),BLACK,1,2]#
    door3 = [(354,142),(455,141),(444,315),(359,315),BLACK,1,3]#
    doors = [door1,door2,door3]
    return doors

#draw polygons for doors
def draw_doors(ds):
    c,l = 4,5
    for d in ds:
        pygame.draw.polygon(win, d[c],[d[0],d[1],d[2],d[3]], d[l])

#if the door has a mouse over it change the colour of the door
def mouse_over(ds,pos):
    x,y,c,l = 0,1,4,5
    for d in ds:
        if d[3][x]<=pos[x]<=d[1][x] and d[0][y]<=pos[y]<=d[2][y]:
            d[c] = LIGHT_BLUE
            d[l] = 0
        else:
            d[c] = BLACK
            d[l] = 1

#if the door is clicked on return the door number
def click_on(ds,pos):
    x,y,c,l,num = 0,1,4,5,6
    for d in ds:
        if d[3][x]<=pos[x]<=d[1][x] and d[0][y]<=pos[y]<=d[2][y]:
            return d[num]
    return -1

#Draw the titles on to the main menu screen
def titles():
    titles_font = pygame.font.SysFont("monospace", 24)
    titles_surface = titles_font.render("Learn a Dance",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    title_rotate = pygame.transform.rotate(titles_surface,20)
    win.blit(title_rotate,(110,110))
    titles_surface = titles_font.render("Leaping Game",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    title_rotate = pygame.transform.rotate(titles_surface,-21)
    win.blit(title_rotate,(525,110))
    titles_surface = titles_font.render("Exit",True,BLACK)
    win.blit(titles_surface,(375,100))
    titles_font = pygame.font.SysFont("monospace", 18)
    titles_surface = titles_font.render("To leave any game, press ESC.",True,BLACK)
    title_wid = titles_surface.get_width()
    win.blit(titles_surface,(400-title_wid/2,500))
    titles_surface = titles_font.render("Welcome to Dance Class",True,BLACK)
    title_wid = titles_surface.get_width()
    win.blit(titles_surface,(400-title_wid/2,400))
    titles_surface = titles_font.render("Pick a room and have some fun",True,BLACK)
    title_wid = titles_surface.get_width()
    win.blit(titles_surface,(400-title_wid/2,425))

#updates main screen
def redraw_game_window():
    win.fill(WHITE)
    draw_doors(door)
    add_main_screen()
    titles()
    pygame.display.update()

#####Functions for both games
#puts background on the screen
def background():
    bgFile = 'dance room.png'
    imgbg = pygame.image.load(bgFile)
    win.blit(imgbg, (0, 0))

#draws play button in instructions window
def drawRectButtons(btn): 
    btn_font = pygame.font.SysFont("arial", 20)
    m,x,y,l,w,label,c = 0,0,1,2,3,1,2
    pygame.draw.rect(win,BLACK,(btn[m]))
    pygame.draw.rect(win,btn[c],(btn[m][x]+5,btn[m][y]+5,btn[m][l]-10,btn[m][w]-10))
    label_surface = btn_font.render(btn[label],True,BLACK) 
    lsize = label_surface.get_size()
    win.blit(label_surface,(btn[m][x]+btn[m][l]/2-lsize[0]/2,btn[m][y]+btn[m][w]/2-lsize[1]/2))

#checks if the play button is clicked, if so returns True
def clickRectButtons(btn,cPos): 
    m,x,y,l,w,label,c = 0,0,1,2,3,1,2
    if btn[m][x]<cPos[x]<btn[m][x]+btn[m][l] and btn[m][y]<cPos[y]<btn[m][y]+btn[m][w]:
        btn[c]= LIGHT_BLUE
        return True
    return False

#checks if the mose is over the button, if so change the colour
def mouseOverRectButtons(btn,mPos): 
    m,x,y,l,w,label,c,sc = 0,0,1,2,3,1,2,3
    if btn[m][x]<mPos[x]<btn[m][x]+btn[m][l] and btn[m][y]<mPos[y]<btn[m][y]+btn[m][w] and btn[c] == btn[sc]:
        btn[c]= BLUE
    if not(btn[m][x]<mPos[x]<btn[m][x]+btn[m][l] and btn[m][y]<mPos[y]<btn[m][y]+btn[m][w]) and btn[c] == BLUE:
        btn[c] = btn[sc]

    
##### All functions for Learn a Dance game
#creates a list with all the different moves
def load_moves():
    imgmoves = []
    for i in range(7):
        moveFile = 'move' + str(i) + '.png'
        imgmoves.append(pygame.image.load(moveFile))
    return imgmoves

#chooses a random index number from the list of options and addes that move to the list that contains the order of the dance moves
def add_order(opt,o):
    randM = random.randrange(0,len(opt)-1)
    o.append(opt[randM])

#allows exiting from all the while loops in the L.A.D. Game
def exit_game(ss,ing,erTurn):
    ss = False
    ing = False
    erTurn = False
    return ss,ing,erTurn

###Functions for the instructions window
def instructionsss():
    pygame.draw.rect(win,BLACK,(25,25,750,500), 3)
    iFile = 'instructionsss.png'
    imgi = pygame.image.load(iFile)
    win.blit(imgi, (500, 50))

#puts the rules onto the screen
def rulesss():
    rules_font = pygame.font.SysFont("monospace", 48)
    rules_surface = rules_font.render("Learn a Dance",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(50,100))
    rules_font = pygame.font.SysFont("monospace", 20)
    rules_surface = rules_font.render("Goal: Create the proper relfection by mimicing the",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(50,275))
    rules_surface = rules_font.render("stickman on the right.",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(75,300))
    rules_surface = rules_font.render("Directions: Press the buttons related the moves you",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(50,350))
    rules_surface = rules_font.render("see to move up a level.",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(75,375))

#puts the keys and what move they are on to the scree
def keys(x,y):
    for i in range(6):
        keyFile = 'keymove'+str(i)+'.png'
        imgkey = pygame.image.load(keyFile)
        win.blit(imgkey, (x, y))
        x += 125

#updates the instructions window
def redraw_instruction_window_ss():
    win.fill(WHITE)
    instructionsss()
    rulesss()
    drawRectButtons(playss)
    keys(50,450)
    pygame.display.update()

#updates the game window   
def redraw_game_window_ss():
    win.fill(WHITE)
    background()
    keys(50,475)
    win.blit(guessss[gmss], (225, 220))
    win.blit(orderss[omss], (450, 320))
    pygame.display.update()

#Main game function
def simon_says():
    global playss
    global optionsss
    global orderss
    global movess
    global gmss
    global omss
    global timess
    global guessss
    playss = [(575,387,175,50),"Play",WHITE,WHITE]
    optionsss = load_moves()
    orderss = [optionsss[6]]
    movess = 0
    score = 0
    gmss = 0
    omss = 0
    timess = 500
    guessss = [optionsss[6]]
    playing_gamess = False
    playerTurnss = False
    guessingss = False
    playingss = True
    instructionsss = True
    highscore = True
    while playingss:
        #while loop for instructions only exited it if the exit button is pressed or if the play button is pressed
        while instructionsss:
            redraw_instruction_window_ss()
            mousePos = pygame.mouse.get_pos()
            mouseOverRectButtons(playss,mousePos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playingss,playing_gamess,playerTurnss = exit_game(playingss,playing_gamess,playerTurnss)
                    instructionsss = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN: # if user clicks anywhere on win  
                    clickPos = pygame.mouse.get_pos()
                    rbClick = clickRectButtons(playss,clickPos)
                    if rbClick:
                        instructionsss = False
                        playing_gamess = True
        while playing_gamess:#in the game
            redraw_game_window_ss()
            pygame.time.delay(1000)
            for event in pygame.event.get():#check if they want to quit the game
                if event.type == pygame.QUIT:
                    playingss,playing_gamess,playerTurnss = exit_game(playingss,playing_gamess,playerTurnss)
                    continue
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:# if user presses the ESC key
                        playss,playing_gamess,playerTurnss = exit_game(playss,playing_gamess,playerTurnss)
                        continue
            add_order(optionsss,orderss)#add a move to the order
            movess +=1
            for i in range(movess):#iterate through each move
                omss = i+1
                redraw_game_window_ss()
                pygame.time.delay(timess)
                omss = 0
                redraw_game_window_ss()
                pygame.time.delay(timess)
            omss = 0#make the person standing again
            redraw_game_window_ss()
            pygame.time.delay(timess)
            playerTurnss = True
            guessingss = True
            m = 0
            while playerTurnss:# have player guess
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playingss,playing_gamess,playerTurnss = exit_game(playingss,playing_gamess,playerTurnss)
                        continue
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:# if user presses the ESC key
                            playingss,playing_gamess,playerTurnss = exit_game(playingss,playing_gamess,playerTurnss)
                            continue
                        #if the they press a key that corresponds with a move play the move then go back to standing
                        if event.key == pygame.K_UP:
                            m+=1
                            guessss.append(optionsss[0])
                            gmss = m
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                            gmss = 0
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                        if event.key == pygame.K_DOWN:
                            m+=1
                            guessss.append(optionsss[1])
                            gmss = m
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                            gmss = 0
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                        if event.key == pygame.K_LEFT:
                            m+=1
                            guessss.append(optionsss[2])
                            gmss = m
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                            gmss = 0
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                        if event.key == pygame.K_RIGHT:
                            m+=1
                            guessss.append(optionsss[3])
                            gmss = m
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                            gmss = 0
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                        if event.key == pygame.K_SPACE:
                            m+=1
                            guessss.append(optionsss[4])
                            gmss = m
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                            gmss = 0
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                        if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                            m+=1
                            guessss.append(optionsss[5])
                            gmss = m
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                            gmss = 0
                            redraw_game_window_ss()
                            pygame.time.delay(timess)
                    if guessss != orderss[:m+1]:#if the guessess they have made don't match the order so farexit the game
                        playingss,playing_gamess,playerTurnss = exit_game(playingss,playing_gamess,playerTurnss)
                        break
                if guessss == orderss:#if all the guesses are the same as the order play the next set of orders 
                    gmss = 0
                    guessss = [optionsss[6]]
                    score +=1
                    redraw_game_window_ss()
                    pygame.time.delay(timess)
                    playerTurnss = False
    while highscore:#go to highscore screen until escape or the exit button is pressed
        score_window(str(score))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                highscore = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    highscore = False

#####All functions for Leaping Game
#Creates rotations of the objects moving across the screen
def rotations(file):
    rots = []
    image = pygame.image.load(file)
    for a in range(0, 361,20):
        rotate = pygame.transform.rotate(image,a)
        rots.append(rotate)
    return rots

#checks for colision between the hangman and the items on the screen and returns True or False    
def iscollision():
    collision = False
    for i in itemslg[:objectslg]:
        iwidth = i[0][i[6]].get_width()
        iheight = i[0][i[6]].get_height()
        hwidth = movelg[mlg].get_width()
        hheight = movelg[mlg].get_height()
        if i[2] <= mylg <= i[2] + iheight or i[2] <= mylg + hheight <= i[2] + iheight:
            if i[1] <= mxlg <= i[1] + iwidth or i[1] <= mxlg + hwidth <= i[1] + iwidth:
                collision = True
    return collision

#Prints score on screen so player can keep track
def print_scorelg(s):
    scorelg_font = pygame.font.SysFont("monospace", 48)
    scorelg_surface = scorelg_font.render("Score:"+str(s),True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    scorelg_wid = scorelg_surface.get_width()
    win.blit(scorelg_surface,(400-scorelg_wid/2,25))
    
###Deals with instruction windows
#Deals with drawing the instructions onto the screen
def redraw_instruction_window_lg():
    win.fill(WHITE)
    instructionslg()
    ruleslg()
    drawRectButtons(playlg)
    pygame.display.update()

#puts framing rectangle and image of game screen on the instruction screen
def instructionslg():
    pygame.draw.rect(win,BLACK,(25,25,750,500), 3)
    iFile = 'instructionslg.png'
    imgi = pygame.image.load(iFile)
    win.blit(imgi, (500, 50))

#Puts Rules on to the screen    
def ruleslg():
    rules_font = pygame.font.SysFont("monospace", 48)
    rules_surface = rules_font.render("Leaping Game",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(50,100))
    rules_font = pygame.font.SysFont("monospace", 20)
    rules_surface = rules_font.render("Goal: To go back and forth across the screen",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(50,225))
    rules_surface = rules_font.render("while leaping over objects across the floor",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(75,250))
    rules_surface = rules_font.render("Directions: Use the RIGHT, LEFT,UP and DOWN keys to",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(50,300))
    rules_surface = rules_font.render("make your character move right, left,jump and stand.",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(75,325))
    rules_surface = rules_font.render("You can stay in the air longer by pressing the UP",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(75,350))
    rules_surface = rules_font.render("key midair.",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(75,375))
    rules_surface = rules_font.render("Reminder: You only have 3 lives, so be careful.",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    win.blit(rules_surface,(50,425))


###Main game
#Deals with drawing the game onto the screen
def redraw_game_window_lg():
    win.fill(WHITE)
    background()
    print_scorelg(scorelg)
    win.blit(movelg[mlg], (mxlg, mylg))
    for i in itemslg:
        for num in range(objectslg):
            #if the item being blited is in the range of objects we want on screen
            if itemslg[num] == i:
                #if the x position is not reaching its end point and it has a count of 0
                if i[4] != i[1] and i[5] == 0:
                    #then put the image on the screen
                    win.blit(i[0][i[6]], (i[1], i[2]))#change placement of item
                    #add speed and move on to the next image
                    i[1] += i[3]
                    i[6] +=1
                    if i[6] == 19:#if the image equals the last image go back to the beginning
                        i[6] = 0
                else:
                    #if the count is greater than 5 and the side to aim for is the left
                    if i[5] >= 5 and i[4] >= 0 and sidelg == 'left':
                        #set x to the left side, set the speed increasing to the right, the end point to the right side and the count and image to 0 
                        i[1] = 110
                        i[3] = 10
                        i[4] = 590
                        i[5] = 0
                        i[6] = 0
                    #if the count is greater than 5 and the side to aim for is the right
                    elif i[5] >= 5 and i[4] >= 0 and sidelg == 'right':
                        #set x to the right side, set the speed increasing to the left, the end point to the left side and the count and image to 0 
                        i[1] = 580
                        i[3] = -10
                        i[4] = 100
                        i[5] = 0
                        i[6] = 0
                    #if the end point = the x and the count is 0 but the end position is not 0
                    elif i[4] == i[1] and i[5] == 0 and i[4]!=0:
                        #make the count dependant on what the object # is to space out objects
                        i[5] = -25*(objectslg-1)+5
                    else:
                        #other wise add to the count and make x and end pont 0
                        i[1] = 0
                        i[4] = 0
                        i[5] += 1
    pygame.display.update()
    
#Main loop for leaping game
def leap_game():
    global playlg
    global movelg
    global mlg
    global mxlg
    global mylg
    global velXlg
    global velYlg
    global xSpeedlg
    global ySpeedlg
    global gravitylg
    global sidelg
    global scorelg
    global objectslg
    
    playlg = [(575,460,175,50),"Play",WHITE,WHITE]
    movelg = standlg
    mlg = 0      
    mxlg = 100   
    mylg = 325 
    velXlg = 0
    velYlg = 0
    xSpeedlg = 15 
    ySpeedlg = 200
    gravitylg = 50
    sidelg = 'right'
    scorelg = 0
    objectslg = 1
    wrongguess = 0
    highscore = True
    checklg = False
    playinglg = True
    instrustionlg = True
    #while loop for instructions only exited it if the exit button is pressed or if the play button is pressed
    while instrustionlg:
        redraw_instruction_window_lg()
        mousePos = pygame.mouse.get_pos()
        mouseOverRectButtons(playlg,mousePos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instrustionlg = False
                playinglg = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN: # if user clicks anywhere on win  
                clickPos = pygame.mouse.get_pos()
                rbClick = clickRectButtons(playlg,clickPos)
                if rbClick:
                    instrustionlg = False
    #while playing the game
    while playinglg:
        redraw_game_window_lg()#update the game window          
        pygame.time.delay(200)
        mlg += 1 #change to the next image
        if scorelg == 2*objectslg:#Each time the score is a multiple of 2 an object is added to the game until all the objects are added
            if objectslg <=5:
                objectslg += 1
                checklg = True
        if objectslg%2 == 0 and checklg:#everytime an object is added make sure all the objects are on the same side
            for i in range(objectslg):
                itemslg[i][1] = 100
                itemslg[i][3] = 10
                itemslg[i][4] = 100
        checklg = False
        if mylg >= 325: #if the person is on the ground subtract gravity
            mylg -= gravitylg
        mylg += gravitylg #add gravity to the person
        if mlg == len(movelg): #if the person is on the last graphic
            mlg = 0 # go back to the first image
            if movelg == leap_rightlg or movelg == leap_leftlg: #if they are jumping make them walk in the direction they were moving and make them walk at a normal speed
                velYlg = 0
                if velXlg == xSpeedlg*3:
                    velXlg -= xSpeedlg
                    movelg = walk_rightlg
                elif velXlg == -xSpeedlg*3:
                    movelg = walk_leftlg
                    velXlg += xSpeedlg
        elif mlg >= 1 and (movelg == leap_rightlg or movelg == leap_leftlg):#they are mid way through the jump
            velYlg = 0 #make the Y velocity = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#if ecit button is pressed exit game
                playinglg = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:# if user presses the ESC key
                    playinglg = False              # exit from the game
                if event.key == pygame.K_LEFT: #If the left key is pressed move to the left, reset the image to the start graphic and make the graphics walking to the left
                    velXlg = -xSpeedlg
                    mlg = 0
                    movelg = walk_leftlg
                if event.key == pygame.K_RIGHT:#If the right key is pressed move to the right, reset the image to the start graphic and make the graphics walking to the right
                    velXlg = xSpeedlg
                    mlg = 0
                    movelg = walk_rightlg
                if event.key == pygame.K_DOWN:#If the down key is pressed stop, reset the image to the start graphic and make the graphics standing
                    velXlg = 0
                    velYlg = 0
                    mlg = 0
                    movelg = standlg
                if event.key == pygame.K_UP:#If the up key is pressed move to in the previous direction at a greater speed, reset the image to the start graphic and make the graphics jumping in the direction they were walking in
                    if velXlg == xSpeedlg:
                        velYlg = -ySpeedlg
                        velXlg = xSpeedlg*3
                        mlg = 0
                        movelg = leap_rightlg
                    elif velXlg == -xSpeedlg:
                        velYlg = -ySpeedlg
                        velXlg = -xSpeedlg*3
                        mlg = 0
                        movelg = leap_leftlg
                    else:
                        if sidelg == 'right':#if  standing make them jump in the direction they need to go in
                            velYlg = -ySpeedlg
                            velXlg = xSpeedlg*3
                            mlg = 0
                            movelg = leap_rightlg
                        elif sidelg == 'left':
                            velYlg = -ySpeedlg
                            velXlg = -xSpeedlg*3
                            mlg = 0
                            movelg = leap_leftlg
        if velXlg >= xSpeedlg and mxlg >= 595: #if they reach the right side make them stand and reset the image to thto the first image of the motion
            velXlg = 0
            velYlg = 0
            mylg = 325
            mlg = 0
            movelg = standlg
        if velXlg <= -xSpeedlg and mxlg <= 100:#if they reach the left side make them stand and reset the image to thto the first image of the motion
            velXlg = 0
            velYlg = 0
            mylg = 325
            mlg = 0
            movelg = standlg
        if sidelg == 'right' and mxlg >= 595:#if they are meant to reach the right side and have reached that side increase the score and change the side to the left
            scorelg += 1
            sidelg = 'left'
        elif sidelg == 'left' and mxlg <= 100:#if they are meant to reach the left side and have reached that side increase the score and change the side to the right
            scorelg += 1
            sidelg = 'right'
        mxlg += velXlg#add to the X and Y coordinate using the X and Y velocities
        mylg += velYlg
        if mylg<=25: #if the height of the person is above 25 then make their x coordinate 26 and their Y velocity 0
            mylg=26
            velYlg=0
        if not(sidelg == 'left' and mxlg >= 595) and not(sidelg == 'right' and mxlg <= 100):#if it is not at one of the sides check for collision
            if iscollision():#if there is colision
                wrongguess += 1#increase wrong guess and set them back to the start positionfor this round
                if sidelg == 'right':
                    mxlg = 100
                    mylg = 325
                    velXlg = 0
                    velYlg = 0
                    movelg = standlg
                    mlg = 0
                elif sidelg == 'left':
                    mxlg = 590
                    mylg = 325
                    velXlg = 0
                    velYlg = 0
                    movelg = standlg
                    mlg = 0
        if wrongguess == 3:#if the user has 3 colisions stop the game
            break
    while highscore: #go to highscore screen until escape or the exit button is pressed
        score_window(str(scorelg))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                highscore = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    highscore = False
    
#####All functions for High Score Window
#Gets previous Highscores and replace it if it is less than the score of this round
def readHighscore(s,g):
    infile = open('Highscores.txt','r')
    line = 0
    data = []
    for aline in infile:
        game = aline.strip()
        if line == g:
            if s>game:
                dataline = s
            else:
                dataline = game
        else:
            dataline = game
        data.append(dataline)
        line+=1
    infile.close()
    return data

#Put new Highscores in to file
def writeHighscore(data):
    outfile = open("Highscores.txt", "w")
    for dataline in data:
        outfile.write(dataline +'\n')
    outfile.close()

#prints HIgh scroes on to the screen    
def highscore(g,s):
    hscore = readHighscore(s,g)
    highscore_font = pygame.font.SysFont("monospace", 48)
    highscore_surface = highscore_font.render("High Score: "+hscore[g],True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    highscore_wid = highscore_surface.get_width()
    win.blit(highscore_surface,(400-highscore_wid/2,200))
    score_surface = highscore_font.render("Score: "+s,True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    score_wid = score_surface.get_width()
    win.blit(score_surface,(400-score_wid/2,300))
    writeHighscore(hscore)
    if hscore[g] == s:
        new_HS_surface = highscore_font.render("NEW HIGH SCORE!",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
        new_HS_wid = new_HS_surface.get_width()
        win.blit(new_HS_surface,(400-new_HS_wid/2,100))
    highscore_font = pygame.font.SysFont("monospace", 24)
    exit_surface = highscore_font.render("To go to main menu press ESC",True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
    exit_wid = exit_surface.get_width()
    win.blit(exit_surface,(400-exit_wid/2,400))

#Redraws the highscore screen    
def score_window(s):
    win.fill(WHITE)
    pygame.draw.rect(win,BLACK,(25,25,750,500), 3)
    highscore(game-1,s)
    pygame.display.update()
    




#initilize moves for leaping game
#standlg
standlg = []
standFile = 'stand.png'
standlg.append(pygame.image.load(standFile))
#leap left
leap_leftlg = []
for i in range(3):
    leapFile = 'lleft' + str(i) + '.png'
    leap_leftlg.append(pygame.image.load(leapFile))
#leap right
leap_rightlg = []
for i in range(3):
    leapFile = 'lright' + str(i) + '.png'
    leap_rightlg.append(pygame.image.load(leapFile))
#walk right
walk_rightlg = []
for i in range(3):
    walkFile = 'wright' + str(i) + '.png'
    walk_rightlg.append(pygame.image.load(walkFile))
#walk left
walk_leftlg = []
for i in range(3):
    walkFile = 'wleft' + str(i) + '.png'
    walk_leftlg.append(pygame.image.load(walkFile))
#itemslg
itemslg = []
c = 0
for i in range(6):
    itemFile = 'ditem' + str(i) + '.png'
    rotates = rotations(itemFile)
    item = [rotates, 590, 425, -10, 100,c,0]
    itemslg.append(item)
    c-=45

#initilize variables for main menu
win=pygame.display.set_mode((800,550))
door = create_doors()
playing = True

while playing:
    redraw_game_window()
    mousePos = pygame.mouse.get_pos()
    mouse_over(door,mousePos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                playing = False             
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            game = click_on(door,clickPos)
            #if a door is picked go to the game for that door.
            if game == 1:
                simon_says()
            if game == 2:
                leap_game()
            if game == 3:
                playing = False

pygame.quit() 
