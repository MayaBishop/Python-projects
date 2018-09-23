##############################################################################
## File Name: example-animation.py                                          ##
## Description: This program draws a ball on the screen.                    ##
## Input: The user can move the ball up/down/left/right with the arrows.    ##
##############################################################################
import pygame
pygame.init()
import gridsFilegood
import math

 
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
#Reads in the events from the text file and create an instance of the class event for each event
def createEvents():
    fileref = open('events.txt',"r")
    linelist = fileref.readlines()
    events=[]
    while linelist != []:
        
        comments=[line[:-1] for line in linelist[11:11+int(linelist[10][:-1])]]
        event = gridsFilegood.event(linelist[0][:-1],linelist[1][:-1],linelist[2][:-1],linelist[5][:-1],linelist[6][:-1],linelist[3][:-1],linelist[4][:-1],linelist[7][:-1],linelist[8][:-1],linelist[9][:-1],comments)
        events.append(event)
        linelist = linelist[11+len(comments):]
    fileref.close()
    return events
#creates a list of all possible log ins 
def createloginlist():
    fileref = open('users.txt',"r")
    logins = []
    for aline in fileref:
        login = aline.split()
        logins.append(login)
    fileref.close()
    return logins
#writes over the file by writing in every event it oresviously had or was created 
def outputEvents(events):
    fileref = open('events.txt',"w")
    while events != []:
        #ename,sclub,sname,date,description,stuCoApproval="Unapproved",principalApproval="Unapproved", caf = "No",custodian= "No",techcrew= "No",commentslst=[]
        fileref.write(events[0].ename.text + '\n')
        fileref.write(events[0].sclub + '\n')
        fileref.write(events[0].sname + '\n')
        fileref.write(events[0].stuCoApproval + '\n')
        fileref.write(events[0].principalApproval + '\n')
        fileref.write(events[0].date.text + '\n')
        fileref.write(events[0].description.text + '\n')
        fileref.write(events[0].caf + '\n')
        fileref.write(events[0].custodian + '\n')
        fileref.write(events[0].techcrew + '\n')
        fileref.write(str(len(events[0].commentslst)) + '\n')
        if len(events[0].commentslst)!= 0:
            for i in range(len(events[0].commentslst)):
                fileref.write(str(events[0].commentslst[i]) + '\n')
        print(events)
        events = events[1:]
    fileref.close()
#draws the game screen by calling the draw method of different instances based off what is on screen
def redraw_game_window():
    game_window.fill(WHITE)
    for i in onscreen:
        i.draw(game_window)
    pygame.display.update()
#Takes in the key pressed down and returns the ordinal value for the character based off whether shift is pressed
def keyType(key,shift):
    if shift:
        for i in range(ord("a"),ord("z")+1):
            if key==i:
                return i-32
    else:
        for i in range(ord("a"),ord("z")+1):
            if key==i:
                return i
        for i in range(ord('0'),ord("9")+1):
            if key==i:
                return i
        if key == ord("."):
            return ord(".")
    return None
#checks to see if the peson logging in is in the system
def checkLogin(username,password,loginlst):
    for li in loginlst:
        if username == li[0]:
            if password == li[-1]:
                return li
            else:
                onscreen.append(gridsFilegood.textbox((200,600,600,50),"Incorrect password.Please try again."))
                return True
    onscreen.append(gridsFilegood.textbox((200,600,600,50),"Username is not found. Please try again."))
    return True
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
#### DON'T FORGET TO CREATE EXIT AND BACK AND LOGOUT BUTTONS
#initalize all variables
game_window=pygame.display.set_mode((1000,700))
events = createEvents()#list of all event instances
onscreen = []#contains all instances on screen
#boolean variables for which window it is in
inPlay = True
isLogIn = True
isPeople = False
isEvents = False
loginlist = createloginlist()#possible logins list
usersTypes = {"Principal":gridsFilegood.Principal1,"StudentCoRep":gridsFilegood.StudentCoRep,"President":gridsFilegood.President,"Student":gridsFilegood.Student}#allows the correct type of person's screen based off the password typed
username = gridsFilegood.textbox((200,400,600,50),"Username: ")#login screens
password = gridsFilegood.textbox((200,500,600,50),"Password: ")
login = gridsFilegood.textbox((400,200,200,50),"Log in:")
onscreen.append(login)
onscreen.append(username)
onscreen.append(password)
clickPos = (0,0)
shift = False#whether shift is being pressed
while inPlay:
    redraw_game_window()                # window must be constantly redrawn - animation
    pygame.time.delay(10)               # pause for 10 miliseconds  

    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # if user clicks on the window's 'X' button
            inPlay = False              # exit from the game
        if event.type == pygame.MOUSEBUTTONDOWN:  # checks for mouse clicked down
            clickPos = pygame.mouse.get_pos() #gets the position where the mouse was clicked
            #if there it is in a persons window check where was clicked and if an event row was clicked and which one or whether the add an event button was clicked if any were clicked switch to the screen of that event type
            if isPeople:
                clicked = onscreen[0].isOver(clickPos)
                if type(clicked) == int:
                    if clicked != -1:
                        if clicked !=0:
                            tevent = len(onscreen[0].events.data)//clicked
                            if tevent != len(onscreen[0].lstevents):
                                onscreen = [events[tevent-1]]
                                isEvent = True

                else:
                    if clicked == True:
                        events.append(gridsFilegood.event("Event Name",li[1],li[0],"Date","Description"))#add the new event to the event list)
                        onscreen = [events[-1]]
                        isEvent = True
                isPeople = False
        #if the key is down 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                for i in onscreen:
                    i.delete(clickPos)#delete a character
            elif event.key == pygame.K_ESCAPE:
                inPlay = False                  # exit from the game
            elif event.key == 13:#check the login
                if isLogIn:
                    li = checkLogin(username.text,password.text,loginlist)
                    if li != True:
                        isLogIn = False
                        isPeople = True
                        if li[-1] == "President":
                            onscreen = [usersTypes[li[-1]](li[0],li[1],events)]
                        else:
                            onscreen = [usersTypes[li[-1]](li[0],events)]
            elif event.key == pygame.K_SPACE:#add a space
                for i in onscreen:
                        i.add(clickPos,chr(event.key))
            elif event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:#shift is pressed
                shift = True
            else:
                char = keyType(event.key,shift)#add the character if it is a character allowed
                if char!= None:
                    for i in onscreen:
                        i.add(clickPos,chr(char))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:#if shift is released key is not pressed
                shift = False


outputEvents(events)s
#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!


