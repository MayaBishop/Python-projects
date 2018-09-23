#---------------------------------------------------------------
# Author: Maya Bishop
# Date: Feb 23, 2017
# Description: The program creates a number of polygons
#   with random coloured side lenghts with a randomly coloured 
#   turtle in the centre of the polygons
# Input: User inputs the number of sides, the length of the
#   sides on the first shape and the number of shapes to draw
#
#---------------------------------------------------------------
import turtle
import random
#create variables for number of sides, the gap size and the number of shapes
#create screen and turtle and give basic properties, allow for RGB colours
numSides = int(input ("How manys sides will the shape have? "))
gapSize = int(input ("What is the gap size do you want? "))
numPolygons = int(input ("How many polygons would you like? "))
wn = turtle.Screen()
wn.colormode(255)
clara = turtle.Turtle()
clara.shape("blank")
sideLength = gapSize
#for loop for each shape created repeated based off the number of shapes wanted
for shapes in range(numPolygons):
    #you increase pensize move the drawing tool far enough that you have centered the shape
    clara.pensize(shapes+1)
    clara.up()
    clara.goto(0-sideLength/2,0)
    clara.down()
    #for loop for each side repeated based of the number of sides wanted
    for sides in range(numSides):
        #pick random numbers to create random colours for the sides
        r = (random.randrange(256))
        g = (random.randrange(256))
        b = (random.randrange(256))
        clara.color(r,g,b)
        #move the turtle to create the shape based of the side length and the number of sides
        clara.forward(sideLength)
        clara.left(360/numSides)
    #Increase the side length each shape
    sideLength += gapSize
#Without drawing, center drawing tool and create stamp of turtle around the centre of the shape
clara.up()
clara.forward(gapSize*numPolygons/2)
clara.left(90)
clara.forward(gapSize/2)
clara.shape("turtle")
clara.stamp()
clara.shape("blank")
