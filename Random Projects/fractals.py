import math
import pygame
pygame.init()
#ellipse(Surface, color, Rect, width=0) -> Rect
# sand colour r 255 g 180+ b 30+
def coral(sp,length,win,angle=math.pi/2):
    epx = sp[0]+(length*math.cos(angle))
    epy = sp[1]-(length*math.sin(angle))
    ep=(epx,epy)
    pygame.draw.line(win,(244, 107, 66),sp,ep)
    pygame.display.update()
    if length > 2*3:
        coral(ep,length-2*3,win,angle/2)
        coral(ep,length-2*3,win,angle*3/2)

def shell(x1,y1,t,angle,length,n):
    x2 = x1 + (length * math.cos(angle))
    y2 = y1 + (length * math.sin(angle))
    wx = (x2-x1)*t
    hy = (y2-y1)*t
    tamp = wx*hy+wx*hy
    print(tamp)
    if wx!=0:
        if wx/abs(wx) == 1:
            k = tamp*-1/15
        else:
            k = tamp*1/15
    else:
        k = 0
    print("k",k)
    pygame.draw.line(window,(0,0,0),(x1,y1),(x2,y2),5)
    #pygame.draw.polygon(window,(224, 62, 33),[(x1,y1),(x2,y2),(x2+k,y2),(x2+k,y1)])
    #print((x1,y1),(x2,y2),wx+hy)
    pygame.display.update()
    if n>1:
        shell(x2,y2,t-.1,angle+0.4,length*.9,n-1)
    print((x1,y1))
    
def waves(x,y,r,n):
    pygame.draw.circle(window,(0, 0, 0),(x,y),r)
    pygame.draw.circle(window,(0, 14, 219),(x,y),r-5)
    pygame.display.update()
    pygame.time.delay(50)
    if n>1 and r-10>0 and x<640:
        waves(x+int(r/2),y,r-10,n-1)
        
def sand(clr,x,y,w,h,high):
    pygame.draw.ellipse(window,clr,(x,y,w,h))
    pygame.display.update()
    x += 10
    if (x+w)*3/4>640:
        y += h-2
        w += 10
        x = 0-w/2
        h += 10
        clr = (clr[0],clr[1]+20,clr[2]+20)
        if clr[1]>255 or clr[2]>255:
            clr=(clr[0],clr[1]-20,clr[2]-20)
    if y<high:
        sand(clr,x,y,w,h,high)
        
def sun(x,y,r,maxnum):
    pygame.draw.circle(window,(255, 236, 94),(x,y),r)
    pygame.display.update()
    angle = 2*math.pi/maxnum
    sunbeams(x,y,r,angle,1,maxnum)
def sunbeams(x,y,r,a,n,mn):
    angle = a*n
    if n%2 == 0:
        nx = x+(r*1.5)*math.cos(angle)
        ny = y+(r*1.5)*math.sin(angle)
    else:
        nx = x+(r*2)*math.cos(angle)
        ny = y+(r*2)*math.sin(angle)
    pygame.draw.line(window,(255, 236, 94),(x,y),(nx,ny))
    pygame.display.update()
    if n<=mn:
        sunbeams(x,y,r,a,n+1,mn)
window = pygame.display.set_mode((640,420))
window.fill((32, 191, 183))
waves(100,300,100,20)
waves(300,300,100,20)
waves(500,300,100,20)
sand((255,180,30),-15,300,30,20,420)
coral((320,400),20*3,window)
sun(540,100,40,20)
##shell(302,290,1,math.pi*3/2,50,40)
##shell(202,290,1,math.pi*3/2,50,40)
##shell(102,290,1,math.pi*3/2,50,40)
##pygame.draw.circle(window,(224, 62, 33),(100,),50)
##shell(2,290,1,math.pi*3/2,50,40)
pygame.display.update()
pygame.time.delay(30000)
pygame.quit()
