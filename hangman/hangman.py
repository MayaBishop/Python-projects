#########################################################
## File Name: hangman.py                               ##
## By: Maya Bishop                                     ##
## Description: Hangman game with clues,visual and     ##
##      sound effects and and options and play again   ##
##      window                                         ##
## Topics: Superhero Movies,Musical Instruments,Sports ##
#########################################################
#import all modules and initilize pygame
import math
import random
import pygame
pygame.init()

def readPuzzles(): #This function imports the text file Puzzles and the clues and puzzles into a list based off of category
    p = [[],[],[]]
    puzl = open('puzzles.txt','r')
    for aline in puzl:
        newPuzl = aline.strip().split(',')
        pi = int(newPuzl[-1])-1
        newPuzl = newPuzl[:-1] + [True]
        p[pi].append(newPuzl)
    puzl.close()
    return p

def randPuz(p,c):#picks a puzzle index from the puzzle list
    randP = random.randrange(0,len(p[c]))
    x = [pz[2] for pz in puzzles[cat]]
    if x.count(True)>=1: #also checks that the puzzle has not been done before and there are still more puzzles to do in that category
        while p[c][randP][-1] == False:
            randP = random.randrange(0,len(p[c]))
        p[c][randP][-1] = False
        return randP
    else:
        return -1

def createGuess(p): #converts letters into underscores
    guess =""
    for ltr in p:
        if ltr == " ":
            guess += " "
        else:
            guess += "_"
    return guess

def createButtons(): #creates alphabet buttons lists based of of pre-set button attributes
    btns = []
    x,y,rad,gap = BUTTON1SX, BUTTON1SY, 20,10
    for b in range(26):
        nextB=[x,y,rad, chr(65+b),LIGHT_BLUE,LIGHT_BLUE,True]
        btns.append(nextB)
        x += rad*2+gap
        if b == 12:
           x = BUTTON1SX
           y += rad*2+gap
    return btns

def drawButtons(btns): #use button lists to draw circles
    btn_font = pygame.font.SysFont("arial", 20)
    x,y,r,label,c = 0,1,2,3,4
    for b in btns:
        pygame.draw.circle(win,BLACK,(b[x],b[y]), b[r], 0)
        pygame.draw.circle(win,b[c],(b[x],b[y]), b[r]-2, 0)
        label_surface = btn_font.render(b[label],True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
        win.blit(label_surface,(b[x]-(b[r]/3),b[y]-(b[r]/2)))

def clickButtons(btns,cPos): #uses pythagorium theorum to check if the buttons have been clicked and return the index number
    x,y,r,label,cl, = 0,1,2,3,4
    for i,bu in enumerate(btns):
        a = math.fabs(bu[x]-cPos[x])
        b = math.fabs(bu[y]-cPos[y])
        c = math.sqrt(a**2+b**2)
        if c <= bu[r]:
            bu[cl]= RED
            return i
    return -1

def mouseOverButtons(btns,mPos): #uses pythagorium theorum to check if the mouse is over the button and changes the colour if it is over the button
    x,y,r,label,cl,sc = 0,1,2,3,4,5
    for i,bu in enumerate(btns):
        a = math.fabs(bu[x]-mPos[x])
        b = math.fabs(bu[y]-mPos[y])
        c = math.sqrt(a**2+b**2)
        if c <= bu[r]and bu[cl] == bu[sc]:
            bu[cl]= BLUE
        elif c > bu[r]and bu[cl] == BLUE:
            bu[cl]= bu[sc]
            
def updateGuess(p,bc,g,btns): #if a button is pressed update the guess to include that letter instead of an underscore
    label = 3
    uGuess = ''
    for i, ltr in enumerate(p):
        ltr = ltr.upper()
        if ltr == btns[bc][label]:
            uGuess += ltr
        else:
            uGuess += g[i:i+1]
    return uGuess

def drawSpaceGuess(g): #added spaces in between each part of the string and create the surface of the guess and blit it on to the screen
    spacedGuess = ''
    for ltr in g:
        spacedGuess += ltr+' '
    guess_font = pygame.font.SysFont("monospace", 24)
    guess_surface = guess_font.render(spacedGuess,True,BLACK)
    win.blit(guess_surface,(350-(15*len(spacedGuess)/2),400))

def createRectButtons(): #manually create rectangular buttons and put into a list
    superMovies = [(38,200,175,50),"Superhero Movies",GREEN,GREEN,True]
    musicInstruments = [(263,200,175,50),"Musical Instruments",GREEN,GREEN,True]
    sports = [(488,200,175,50),"Sports",GREEN,GREEN,True]
    playAgain = [(300,200,100,50),"Play Again",RED,RED,True]
    quitBtn = [(590,400,60,30),"Quit",RED,RED,True]
    clue = [(50,400,60,30),"Clue",RED,RED,True]
    btns=[superMovies,musicInstruments,sports,playAgain,quitBtn,clue]
    return btns

def drawRectButtons(btns,ind): #use button lists to draw rectangles
    btn_font = pygame.font.SysFont("arial", 20)
    m,x,y,l,w,label,c = 0,0,1,2,3,1,2
    for b in ind:
        pygame.draw.rect(win,BLACK,(btns[b][m]))
        pygame.draw.rect(win,btns[b][c],(btns[b][m][x]+5,btns[b][m][y]+5,btns[b][m][l]-10,btns[b][m][w]-10))
        label_surface = btn_font.render(btns[b][label],True,BLACK) #Creates surfaces containing the labels to blit on to the screen ontop of the buttons
        lsize = label_surface.get_size()
        win.blit(label_surface,(btns[b][m][x]+btns[b][m][l]/2-lsize[0]/2,btns[b][m][y]+btns[b][m][w]/2-lsize[1]/2))

def clickRectButtons(btns,cPos,ind): #if the mouse clicked between the sides of a button and if so return the index number
    m,x,y,l,w,label,c = 0,0,1,2,3,1,2
    for i,bu in enumerate(btns):
        for num in ind:
            if num == i:
                if bu[m][x]<cPos[x]<bu[m][x]+bu[m][l] and bu[m][y]<cPos[y]<bu[m][y]+bu[m][w]:
                    bu[c]= LIGHT_BLUE
                    return i
    return -1
def mouseOverRectButtons(btns,mPos): #if the mouse is in between the sides of a button and if so change the colour
    m,x,y,l,w,label,c,sc = 0,0,1,2,3,1,2,3
    for i,bu in enumerate(btns):
        if bu[m][x]<mPos[x]<bu[m][x]+bu[m][l] and bu[m][y]<mPos[y]<bu[m][y]+bu[m][w] and bu[c] == bu[sc]:
            bu[c]= BLUE
        if not(bu[m][x]<mPos[x]<bu[m][x]+bu[m][l] and bu[m][y]<mPos[y]<bu[m][y]+bu[m][w]) and bu[c] == BLUE:
            bu[c] = bu[sc]

def drawClue(c): #create surface and blit the clue into the center of the screen
    guess_font = pygame.font.SysFont("monospace", 20)
    clue_surface = guess_font.render(c,True,BLACK)
    cwid = clue_surface.get_width()
    win.blit(clue_surface,(350-cwid/2,450))
    
def hangman(wg):#import and blit hangman image onto the screen
    fileName = "hangman"+str(wg)+".png"
    hangman_surface = pygame.image.load(fileName)
    win.blit(hangman_surface,(250,125))               
def clapping():#import and blit clapping image onto the screen
    fileName = "ClappingHands.png"
    clapping_surface = pygame.image.load(fileName)
    win.blit(clapping_surface,(75,175))
    win.blit(clapping_surface,(525,175))
def youveWin():#create surface and blit the 'You Win' into the center of the screen
    guess_font = pygame.font.SysFont("monospace", 48)
    yw_surface = guess_font.render("You Win",True,BLACK)
    ywWid = yw_surface.get_width()
    win.blit(yw_surface,(350-ywWid/2,75))
def youveLose():#create surface and blit the 'You Lose" into the center of the screen
    guess_font = pygame.font.SysFont("monospace", 48)
    yl_surface = guess_font.render("You Lose",True,BLACK)
    ylWid = yl_surface.get_width()
    win.blit(yl_surface,(350-ylWid/2,75))
def optionSaying():#create surface and blit the title and instructions into the center of the screen
    guess_font = pygame.font.SysFont("monospace", 48)
    h_surface = guess_font.render("Hangman",True,BLACK)
    guess_font = pygame.font.SysFont("monospace", 32)
    s_surface = guess_font.render("Please pick a category.",True,BLACK)
    hWid = h_surface.get_width()
    sWid = s_surface.get_width()
    win.blit(h_surface,(350-hWid/2,50))
    win.blit(s_surface,(350-sWid/2,125))
#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():#updates game window
    win.fill(GREEN)
    if clap:
        clapping()
    drawButtons(buttons)
    drawSpaceGuess(guess)
    hangman(wrongGuess)
    drawRectButtons(optBtns,(q,c))
    if clue:
        drawClue(puzzles[cat][pi][1])
    pygame.display.update()
def redraw_options_window():#updates options window based off what menu is needed
    win.fill(LIGHT_BLUE)
    if youLose or youWin:
        if youWin:
           youveWin()
        elif youLose:
           youveLose()
        drawRectButtons(optBtns,(pa,q))
    else:
        optionSaying()
        drawRectButtons(optBtns,(sm,mi,s,q))
    pygame.display.update()
#---------------------------------------#
# initialize global variables/constants #
#---------------------------------------#
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED   = (255,0, 0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
LIGHT_BLUE = (102,255,255)
BUTTON1SX = 50
BUTTON1SY = 50
wrongGuess = 0
RECTBUTTONX = 50
RECTBUTTONY = 100
win = pygame.display.set_mode((700,480))
buttons=createButtons()
optBtns=createRectButtons()
sm,mi,s,pa,q,c = 0,1,2,3,4,5
co,sc = 2,3
count = 0
dying = 0
puzzles = readPuzzles()
youLose = False
youWin = False
options = True
playing = False
inPlay = True
clue = False
clap = False
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
while inPlay:
    while options:
        redraw_options_window()# window must be constantly redrawn - animation
        pygame.time.delay(10)# pause for 10 miliseconds
        mousePos = pygame.mouse.get_pos()#Get and check mouse position with buttons
        mouseOverButtons(buttons,mousePos)
        mouseOverRectButtons(optBtns,mousePos)
        for event in pygame.event.get(): # check for any events              
            if event.type == pygame.QUIT:# if user clicks on the window's 'X' button
                inPlay = False           # exit from the game
                options = False                         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:# if user presses the ESC key
                    inPlay = False              # exit from the game
                    options = False                     
            if event.type == pygame.MOUSEBUTTONDOWN: # if user clicks anywhere on win  
                clickPos = pygame.mouse.get_pos()    #Get the position
                if youWin or youLose:                #Check it if the mouse has clicked the buttons that are on the screen
                    rbClick = clickRectButtons(optBtns,clickPos,(pa,q))
                else:
                    rbClick = clickRectButtons(optBtns,clickPos,(sm,mi,s,q))
                if rbClick != -1:#if options button clicked
                    if rbClick <=2:#if categorys button is pressed reset game and set category variable
                        cat = rbClick
                        options = False
                        playing = True
                        clue = False
                        for b in buttons:
                            b[4] = LIGHT_BLUE
                            b[6] = True
                        pi = randPuz(puzzles,cat)
                        guess = createGuess(puzzles[cat][pi][0])
                        wrongGuess = 0
                    elif rbClick == 3: #if play again button is pressed go to main menu
                        for i in range(3):
                            optBtns[i][co]=optBtns[i][sc]
                        optBtns[pa][co]=optBtns[pa][sc]
                        youLose = False
                        youWin = False
                    elif rbClick == 4: #if quit is pressed exit from game
                        inPlay = False
                        options = False
    if inPlay == False:
        break
    while playing:
        redraw_game_window()# window must be constantly redrawn - animation
        pygame.time.delay(10)# pause for 10 miliseconds
        count+=1
        dying+=1
        if count == 85: #turns claping symbol off
            clap = False
        if guess == puzzles[cat][pi][0].upper():#if the guess is the same as the puzzle
            pygame.time.delay(1000)#resets game with next puzzle
            clue = False
            clap = False
            optBtns[5][co] = optBtns[5][sc]
            for b in buttons:
                b[4] = LIGHT_BLUE
                b[6] = True
            pi = randPuz(puzzles,cat)
            if pi == -1:#if there is no more puzzles go to YOU WIN screen
                youWin = True
                options = True
                playing = False
                break
            guess = createGuess(puzzles[cat][pi][0])
            wrongGuess = 0
        mousePos = pygame.mouse.get_pos()#Get and check mouse position with buttons
        mouseOverButtons(buttons,mousePos)
        mouseOverRectButtons(optBtns,mousePos)
        for event in pygame.event.get():               # check for any events
            if event.type == pygame.QUIT:              # if user clicks on the window's 'X' button
                inPlay = False                         # exit from the game
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # if user presses the ESC key
                    inPlay = False               # exit from the game
                    playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:   # if user clicks anywhere on win
                clickPos = pygame.mouse.get_pos()      #Get the position
                bClick = clickButtons(buttons,clickPos)#Check it if the mouse has clicked the buttons that are on the screen
                rbClick = clickRectButtons(optBtns,clickPos,(q,c))
                if wrongGuess != 6: #if a button has been clicked, wrong guess is under 6 and the button hasn't been clicked yet
                    if bClick != -1:
                        if buttons[bClick][6]:
                            if guess.count(buttons[bClick][3]) != puzzles[cat][pi][0].upper().count(buttons[bClick][3]):#if letter is in the puzzle
                                clap = True                                                                             #update guess and do sound and visual effects
                                pygame.mixer.music.load("clapping sound.mp3")
                                pygame.mixer.music.play()
                                count = 0
                                guess = updateGuess(puzzles[cat][pi][0],bClick,guess,buttons)
                            elif puzzles[cat][pi][0].upper().count(buttons[bClick][3]) == 0:    #otherwise add one to wrong guess
                                clap = False
                                wrongGuess += 1
                            buttons[bClick][6] = False
                if rbClick != -1:#if options button clicked
                    if rbClick == 4:#if quit is clicked go to main menu
                        for i in range(3):
                            optBtns[i][co]=optBtns[i][sc]
                        optBtns[q][co]=optBtns[q][sc]
                        options = True
                        playing = False
                    elif rbClick == 5: #if clue is clicked print out clue
                        clue = True
                if wrongGuess == 6: #if you have 6 wrong guess start sound effects
                    pygame.mixer.music.load("hangman death sound.mp3")
                    pygame.mixer.music.play()
                    dying = 0
        if dying == 50 and wrongGuess == 6:#if you have 6 wrong guess and sound effect done go to YOU LOSE screen 
            youLose = True
            options = True
            playing = False
            
     

#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!
