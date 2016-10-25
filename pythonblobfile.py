import Myro
from Myro import *
from Graphics import *
from random import *


width = 500
height = 500
sim = Simulation("Maze World", width, height, Color("gray"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("black"))
sim.addWall((10, 10), (20, 490), Color("black"))
sim.addWall((480, 10), (490, 490), Color("black"))
sim.addWall((10, 480), (490, 490), Color("black"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 150 and getGreen(pixel) < 50 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel) < 50 and getGreen(pixel) > 100 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) < 50 and getGreen(pixel) < 50  and getBlue(pixel) > 150):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 200 and getGreen(pixel) > 150 and getBlue(pixel) < 50):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel


# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

######################Code Starts Here##################################

chooseBlobColor = raw_input("Please choose the color that you would like the robot to find")
if chooseBlobColor == "red" or chooseBlobColor == "Red":
    colorNumber = 1
elif chooseBlobColor == "green" or chooseBlobColor == "Green":
    colorNumber = 2
elif chooseBlobColor == "blue" or chooseBlobColor == "Blue":
    colorNumber = 3
elif chooseBlobColor == "yellow" or chooseBlobColor == "Yellow":
    colorNumber = 4
else:
    print("Pick one of the four colors or check your spelling, please")
    

def blobFind():
    bigTurnNumber = randrange(30,60)
    smallTurnNumber = randrange(1,9)
    takePicture()
    print(colorNumber)
    while findColorSpot(takePicture(),colorNumber) == 0:
        turnBy(bigTurnNumber)
        takePicture()
        print(findColorSpot(takePicture(),colorNumber))
    while findColorSpot(takePicture(),colorNumber) > 0:
        if 0 < findColorSpot(takePicture(),colorNumber) < 108:
            turnBy(smallTurnNumber)
        elif 148 < findColorSpot(takePicture(),colorNumber):
            turnBy(-smallTurnNumber)
        else:
            forward(4.5,1)
    
blobFind()

goAgain = raw_input("Would you like to find another blob?")
if goAgain == "yes" or goAgain == "Yes" or goAgain == "y":
    backward(4.5,1)
    chooseBlobColor = raw_input("Please choose the color that you would like the robot to find")
    if chooseBlobColor == "red" or chooseBlobColor == "Red":
        colorNumber = 1
        blobFind()
    elif chooseBlobColor == "green" or chooseBlobColor == "Green":
        colorNumber = 2
        blobFind()
    elif chooseBlobColor == "blue" or chooseBlobColor == "Blue":
        colorNumber = 3
        blobFind()
    elif chooseBlobColor == "yellow" or chooseBlobColor == "Yellow":
        colorNumber = 4
        blobFind()
    else:
        print("Pick one of the four colors or check your spelling, please")
elif goAgain == "no" or goAgain == "No" or goAgain == "n":
    stop()
else:
    print("Please say either yes or no")

