import pygame
#class containing a rext for position num of rows columns and a gap between cells
#as well as the cell Width/Height and whether the grid is visible
class grid():
    def __init__(self,rect,rows,columns,gap, visibility = True):
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2]
        self.h = rect[3]
        self.rows = rows
        self.columns = columns
        self.gap = gap
        self.visibility = visibility
        self.cWidth = (self.w - gap*(columns-1))/columns
        self.cHeight = (self.h - gap*(rows-1))/rows
        self.cellLocations = self.loadCellLocations()
#create a method that creates a list of all the rests for each cell
    def loadCellLocations(self):
        cLocations = []
        gy = self.y
        for i in range(self.rows):
            gx = self.x
            for i in range(self.columns):
                rect = (gx,gy,self.cWidth,self.cHeight)
                cLocations.append(rect)
                gx += self.cWidth+self.gap
            gy += self.cHeight+self.gap
        return cLocations
#draws each cell
    def draw(self,win):
        for i in self.data:
            i.draw(win)
#gets the data for the a specific row and column
    def retrieveData(self,row,column):
        if self.rows<row or self.columns<column:
            return None
        index = column+(row-1)*self.columns-1
        return self.cellData[index]
#checks what cell the mouse is over
    def isOver(self,mp):
        mx,my = mp[0],mp[1]
        for i,cell in enumerate(self.cellLocations):
            cx = cell[0]
            cy = cell[1]
            cw = cell[2]
            ch = cell[3]
            if cx <= mx <= cx + cw and cy <= my <= cy + ch:
                return i
        return -1
#class that takes in rect positions and rows and columns, gaps and the data and colours for the grid as well as font type and size
class EventsShown(grid):
    def __init__(self, rect, gap, events):
        self.events = events
        rows= len(events)
        columns = len(events[0])
        grid.__init__(self,rect,rows,columns,gap, False)
        self.data = self.createEvents()
#creates a event for each row
    def createEvents(self):
        dta = []
        for i in range(self.rows):
            for j in range(self.columns):
                if i<len(self.events):
                    dta.append(textbox(self.cellLocations[j+(i*self.columns)],self.events[i][j]))
        return dta

#a class that takes in the rect, and text at least and creates a text box 
class textbox():
    font = pygame.font.SysFont("arialround",25)
    def __init__(self,rect,text,borderColour = (0,0,0), textColour = (0,0,0), borderThickness = 5):
        self.rect = rect
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2]
        self.h = rect[3]
        self.ogtext = text
        self.text = text
        self.borderColour = borderColour
        self.textColour = textColour
        self.borderThickness = borderThickness
    #add the string to text if the mouse is over the text box if typing over orignial text create new string 
    def add(self,mp,string):
        if self.isOver(mp):
            if self.text == self.ogtext:
                self.text = string
            else:
                self.text = self.text+string
        return(self.text)
    #delete an amount off the end based off whether the mouse is over the textbox if the text is the original text or you will delete the whole string make the text the orignial text
    def delete(self,mp,amntbkspace=1):
        if self.isOver(mp):
            if amntbkspace == len(self.text) or self.text == self.ogtext:
                self.text = self.ogtext
            else:
                self.text = self.text[:-amntbkspace]
        return(self.text)
    #checks whether the mouse position is over the text box
    def isOver(self,mp):
        mx,my = mp[0],mp[1]
        return self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h
    #draws the text box and calls the method to draw the text onto the screen
    def draw(self,win):
        pygame.draw.rect(win,self.borderColour,self.rect,self.borderThickness)
        pygame.draw.rect(win,(255,255,255),self.rect)
        self.drawtext(win,self.text,self.w,self.y+10)
    #recursivly blits text onto the screen base off whether the length of the string fits the textbox if it is not full then call the function after drawing what it can 
    def drawtext(self,win,text,width,y):
        if len(text)<= width//10:
            stext = self.font.render(text,True,self.textColour)
            win.blit(stext,(self.x+10,y))
        else:
            length = int(width//10)
            while text[length]!=" ":
                length = length-1
            btext = text[:length]
            text = text[length:]
            stext = self.font.render(btext,True,self.textColour)
            win.blit(stext,(self.x+10,y))
            self.drawtext(win,text,self.w,y+20)

#parent class to the different kinds of people which creates what they are allowed to see and the list of events they ahave as attributes
class People():
    def __init__(self,lstofevnts,eventSubmitter,eventCouncil,stuCoApproval,principalApproval):
        self.lstofevnts = lstofevnts
        self.eventSubmitter = eventSubmitter
        self.eventCouncil = eventCouncil
        self.stuCoApproval = stuCoApproval
        self.principalApproval = principalApproval
    #draws the person on screen
    def draw(self,win):
        self.name.draw(win)
        self.addEvent.draw(win)
        self.events.draw(win)
    #checks whether any of the items on screen are clicked
    def isOver(self,mp):
        if self.events.isOver(mp)!=-1:
            return self.events.isOver(mp)
        else:
            return self.addEvent.isOver(mp)
class Principal1(People):
    def __init__(self,username,lstofevnts):
        self.name = textbox((50,50,200,50),username)
        self.lstevents = [["Events","Club","Principal Status"]]+[[e.ename.text,e.sclub,e.principalApproval] for e in lstofevnts if e.stuCoApproval == "Approved"]
        self.events = EventsShown((50,200,900,350), 0, self.lstevents)
        People.__init__(self,self.lstevents,False,True,False,True)
#child class of People where they are only allowed to see the council,student council status and principal approval as well as creates the add event text box
class StudentCoRep(People):
    def __init__(self,username,lstofevnts):
        self.name = textbox((50,50,200,50),username)
        self.addEvent = textbox((50,600,200,50),"Add Event")
        self.lstevents = [["Events","Club","Student Co. Status","Principal Status"]]+[[e.ename.text,e.sclub,e.stuCoApproval,e.principalApproval] for e in lstofevnts]
        self.events = EventsShown((50,200,900,350), 0, self.lstevents)
        People.__init__(self,self.lstevents,False,True,True,True)
#child class of People where they are only allowed to see the name of the submitter, council,student council status and principal approval as well as creates the add event text box
class President(People):
    def __init__(self,username,club,lstofevnts):
        self.name = textbox((50,50,200,50),username)
        self.addEvent = textbox((50,600,200,50),"Add Event")
        self.club = club
        self.lstevents = [["Events","Submitted by","Student Co. Status","Principal Status"]]+[[e.ename.text,e.sname,e.stuCoApproval,e.principalApproval] for e in lstofevnts if e.sclub == club]
        self.events = EventsShown((50,200,900,350), 0, self.lstevents)
        People.__init__(self,self.lstevents,True,True,True,True)
#child class of People where they are only allowed to see student council status and principal approval as well as creates the add event text box
class Student(People):
    def __init__(self,username,lstofevnts):
        self.name = textbox((50,50,200,50),username)
        self.addEvent = textbox((50,600,200,50),"Add Event")
        self.lstevents = [["Events","Student Co. Status","Principal Status"]]+[[e.ename.text,e.stuCoApproval,e.principalApproval] for e in lstofevnts if e.sname == username]
        self.events = EventsShown((50,200,900,350), 0, self.lstevents)
        People.__init__(self,self.lstevents,False,False,True,True)
#creates the event screen by creating all the textboxes needing to appear on screen
class event():
    def __init__(self,ename,sclub,sname,date,description,stuCoApproval="Unapproved",principalApproval="Unapproved", caf = "No",custodian= "No",techcrew= "No",commentslst=[]):#comments list of lists [[name,comment],[name,comment]], name and description will be text boxes
        self.ename = textbox((50,50,900,50),ename)
        self.sname = sname
        self.sclub = sclub
        self.date = textbox((50,125,200,50),date)
        self.stuCoApproval = stuCoApproval
        self.principalApproval = principalApproval
        self.description = textbox((50,200,900,200),description)
        self.caf = caf
        self.custodian = custodian
        self.techcrew = techcrew
        self.commentslst = commentslst
        self.scAprrovalBox = textbox((275,125,350,50),"Student Council Approval: "+stuCoApproval)
        self.pAprovalBox = textbox((650,125,300,50),"Principal Approval: "+principalApproval)
        self.cafBox = textbox((100,425,200,50),"Cafeteria: "+caf)
        self.custodianBox = textbox((400,425,200,50),"Custodian: "+custodian)
        self.tcBox = textbox((700,425,200,50),"Tech Crew: "+techcrew)
        self.commentBoxes = [textbox((50,500+i*50,900,50),commentslst[i]) for i in range(len(commentslst))]
        self.txtboxes = [self.ename,self.date,self.description,self.scAprrovalBox,self.pAprovalBox,self.cafBox,self.custodianBox,self.tcBox,self.commentBoxes]
    #draws the screen by drawing all the textboxes on screen
    def draw(self,win):
        for i in self.txtboxes:
            if type(i) == list:
                for j in i:
                    j.draw(win)
            else:
                i.draw(win)
    #add to a textbox on screen
    def add(self,mp,string):
        for i in self.txtboxes:
            if type(i) == list:
                for j in i:
                    j.add(mp,string)
            else:
                i.add(mp,string)
    #delete to a textbox on screen
    def delete(self,mp,amntbkspace=1):
        for i in self.txtboxes:
            if type(i) == list:
                for j in i:
                    j.delete(mp,amntbkspace)
            else:
                i.delete(mp,amntbkspace)
    #checks if mouse is over a textbox on screen
    def isOver(self,mp):
        for i in self.txtboxes:
            if type(i) == list:
                for j in i:
                    return j.isOver(mp)
            else:
                return i.isOver(mp)
                
                
