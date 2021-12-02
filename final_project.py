import pygame
import random


#Creating a method for rectangle collision detection and bouncing
def bounce(circleCoords,rectCoords,cSize,circleSpeedY):
        if rectCoords[0] < circleCoords[0] < (rectCoords[0] + rectCoords[2])\
           and rectCoords[1] < (circleCoords[1] + cSize) < (rectCoords[1] + rectCoords[3] + 0):
            print("Hit")
            return -21
        else:
            return circleSpeedY
      
            
def main():

    pygame.init()

    #Screen dimensions
    surfaceWidth = 450
    surfaceHeight = 780
    
    gameState = "start"
    
    clock = pygame.time.Clock()  #fps

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
    rect1D = [210,450,35,12]
    jumping = False
    
    groundLevel = 755
    
    moveCircleRight = False 
    moveCircleLeft = False

    #Randomising rectangle placement
    rects = []
    for i in range(7):
            rects.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12])
            
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
                
                
            circleSpeedY = bounce(circlePos,rect1D,circleSize,circleSpeedY)
            circlePos[1] += circleSpeedY
            
            
            if circlePos[0] > surfaceWidth:
                circlePos[0] = 0
            elif circlePos[0] < 0:
                circlePos[0] = surfaceWidth

            mainSurface.fill("dodgerblue")

            #Drawing the circles and rectangles
            pygame.draw.rect(mainSurface, "lightgray", (0,groundLevel,surfaceWidth,surfaceHeight-groundLevel))
            pygame.draw.rect(mainSurface, "darkgreen", rect1D)
            pygame.draw.circle(mainSurface, circleColor, (circlePos[0],circlePos[1]),circleSize)
        
            for i in range(len(rects)):
                    pygame.draw.rect(mainSurface, "black", (rects[i][0], rects[i][1], rects[i][2], rects[i][3]))

        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()

main()
