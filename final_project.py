import pygame
import random   

def main():

    pygame.init()

    #Screen dimensions
    surfaceWidth = 450
    surfaceHeight = 780
    
    gameState = "start"

    #fps
    clock = pygame.time.Clock() 

    mainSurface = pygame.display.set_mode((surfaceWidth,surfaceHeight))

    #Font data
    font = pygame.font.SysFont("Candara", 75)
    font2 = pygame.font.SysFont("Tahoma", 40)
    
    i = 0

    #Circle and Rectangle data
    circlePos = [250,750]
    circleSize = 30
    circleColor = "red"
    circleSpeedY = 0
    rectPlayD = [125,550,200,55]
    #rect1D = [210,40,35,12]
    rectColor = "black"
    #rectSpeed = 0.8
    jumping = False
    aboveScreen = False
    
    groundLevel = 755
    
    moveCircleRight = False 
    moveCircleLeft = False


    #Randomising rectangle placement
    rectNormal = []
    for i in range(7):
        rectNormal.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12])

    rectMove = []
    #if aboveScreen:
    for i in range(3):
        rectMove.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12,0.8])


    #Creating a method for rectangle collision detection and bouncing
    def bounce(circleCoords,rectCoords,cSize,circleSpeedY):
        if rectNormal[i][0] < circleCoords[0] < (rectNormal[i][0] + rectNormal[i][2])\
           and rectNormal[i][1] < (circleCoords[1] + cSize) < (rectNormal[i][1] + rectNormal[i][3] + 10) and circleSpeedY > 0:
            print("Hit")
            return -21
        else:
            return circleSpeedY
            
    while True:
        ev = pygame.event.poll()   
        if ev.type == pygame.QUIT:  
            break

       
        #Start screen
        if gameState == "start":
            mainSurface.fill("navy")
            pygame.draw.rect(mainSurface, "white", rectPlayD)
            text1 = "Whirlybird"
            text2 = "Play"
            renderedText1 = font.render(text1, 1, pygame.Color("white"))
            renderedText2 = font2.render(text2, 1, pygame.Color("navy"))
            mainSurface.blit(renderedText1, (70,120))
            mainSurface.blit(renderedText2, (190,550))
            if ev.type == pygame.MOUSEBUTTONUP:
                if rectPlayD[0] < pygame.mouse.get_pos()[0] < (rectPlayD[0] + rectPlayD[2])\
                   and rectPlayD[1] < pygame.mouse.get_pos()[1] < (rectPlayD[1] + rectPlayD[3]):
                    gameState = "game"


        #Game screen
        if gameState == "game":

            mainSurface.fill("dodgerblue")

            #Drawing the circles and rectangles
            pygame.draw.rect(mainSurface, "black", (0,groundLevel,surfaceWidth,surfaceHeight-groundLevel))
            pygame.draw.circle(mainSurface, circleColor, (circlePos[0],circlePos[1]),circleSize)
        
            for i in range(len(rectNormal)):
                pygame.draw.rect(mainSurface, rectColor, (rectNormal[i][0], rectNormal[i][1], rectNormal[i][2], rectNormal[i][3]))
            for i in range(len(rectMove)):
                pygame.draw.rect(mainSurface, rectColor, (rectMove[i][0], rectMove[i][1], rectMove[i][2], rectMove[i][3]))
            
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    moveCircleRight = True
                elif ev.key == pygame.K_LEFT:
                    moveCircleLeft = True

            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_RIGHT:
                    moveCircleRight = False
                elif ev.key == pygame.K_LEFT:
                    moveCircleLeft = False            
             
            if ((circlePos[1] + circleSize) < groundLevel) and moveCircleRight:
                circlePos[0] += 4
            elif ((circlePos[1] + circleSize) < groundLevel) and moveCircleLeft:
                circlePos[0] -= 4
          

        #Making the circle jump and bounce
            if ((circlePos[1] + circleSize) > groundLevel):
                circlePos[1] = groundLevel - circleSize
                circleSpeedY = 0
                jumping = False
            else:
                circleSpeedY += 0.3      
        
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if jumping == False:
                    circleSpeedY = -21
                    jumping = True
                
            for i in range(len(rectNormal)):    
                circleSpeedY = bounce(circlePos,rectNormal[i],circleSize,circleSpeedY)
            circlePos[1] += circleSpeedY

            if circlePos[0] > surfaceWidth:
                circlePos[0] = 0
            elif circlePos[0] < 0:
                circlePos[0] = surfaceWidth

        #Moving the rectangles
            if circleSpeedY < 0:
                for i in range(len(rectNormal)):
                    rectNormal[i][1] += 0.7
                for i in range(len(rectMove)):
                    rectMove[i][1] += 0.7

            for i in range(len(rectMove)):
                rectMove[i][0] += rectMove[i][4]
                if (rectMove[i][0] + rectMove[i][2]) >= surfaceWidth or rectMove[i][0] < 0:
                    rectMove[i][4] = -rectMove[i][4]

            #if circlePos[1] <= 0:
                #aboveScreen = True
            #elif circlePos[1] > 0:
                #aboveScreen = False

        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()

main()
