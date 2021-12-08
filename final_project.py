import pygame
import random   

def main():

    pygame.init()

    i = 0

    #Screen dimensions
    surfaceWidth = 450
    surfaceHeight = 785
    
    gameState = "start"

    #fps
    clock = pygame.time.Clock() 

    mainSurface = pygame.display.set_mode((surfaceWidth,surfaceHeight))

    #Font data
    font = pygame.font.SysFont("Candara", 75)
    font2 = pygame.font.SysFont("Tahoma", 40)
    font3 = pygame.font.SysFont("Impact", 90)

    #Circle and Rectangle data
    circlePos = [250,250]
    circleSize = 27.5
    circleColor = "red"
    circleSpeedY = 0
    circleFall = False
    
    rectPRD = [125,575,200,55]
    rectAgain = 0
    jumping = False
    
    groundLevel = surfaceHeight - 25
    
    moveCircleRight = False 
    moveCircleLeft = False


    #Randomising rectangle placement
    rectNormal = []
    for i in range(6):
        rectNormal.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12])

    rectMove = []
    for i in range(6):
        rectMove.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12,0.8])


    #Creating a method for rectangle collision detection and bouncing
    def bounce(circleCoords,rectCoords,cSize,circleSpeedY):
        if rectCoords[0] < circleCoords[0] < (rectCoords[0] + rectCoords[2])\
           and rectCoords[1] < (circleCoords[1] + cSize) < (rectCoords[1] + rectCoords[3] + 10) and circleSpeedY > 0:
            return -21
        else:
            return circleSpeedY
     
     
    #Main game loop
    while True:
        ev = pygame.event.poll()   
        if ev.type == pygame.QUIT:
            break


       
        #Start screen
        if gameState == "start":
            mainSurface.fill("navy")
            pygame.draw.rect(mainSurface, "white", rectPRD)
            text1 = "Whirlybird"
            text2 = "Play"
            renderedText1 = font.render(text1, 1, pygame.Color("white"))
            renderedText2 = font2.render(text2, 1, pygame.Color("navy"))
            mainSurface.blit(renderedText1, (70,115))
            mainSurface.blit(renderedText2, (190,575))
            if ev.type == pygame.MOUSEBUTTONUP:
                if rectPRD[0] < pygame.mouse.get_pos()[0] < (rectPRD[0] + rectPRD[2])\
                   and rectPRD[1] < pygame.mouse.get_pos()[1] < (rectPRD[1] + rectPRD[3]):
                    gameState = "game"



        #Game screen
        if gameState == "game":
            
            mainSurface.fill("dodgerblue")

            #Drawing the circles and rectangles
            pygame.draw.rect(mainSurface, (35, 25, 25), (0,groundLevel,surfaceWidth,surfaceHeight-groundLevel))
            pygame.draw.circle(mainSurface, circleColor, circlePos, circleSize)
        
            for i in range(len(rectNormal)):
                pygame.draw.rect(mainSurface, "navy", (rectNormal[i][:4]))
            for i in range(len(rectMove)):
                pygame.draw.rect(mainSurface, "darkred", (rectMove[i][:4]))


            #Moving the ball sideways with keys
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
                circleFall = True
                circleSpeedY = 0
                jumping = False
            else:
                circleSpeedY += 0.3      
        
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if jumping == False:
                    circleSpeedY = -21
                    circleSpeedY2 = -21
                    jumping = True


            #Making the rectangles work  
            for i in range(len(rectNormal)):    
                circleSpeedY = bounce(circlePos,rectNormal[i],circleSize,circleSpeedY)

                if circleSpeedY < 0:
                    rectNormal[i][1] += 1

                if (rectNormal[i][1] + rectNormal[i][3]) >= groundLevel:
                    rectNormal[i][0] = random.randrange(surfaceWidth - 35)
                    rectNormal[i][1] = random.randrange(groundLevel - 25)
            
            for i in range(len(rectMove)):
                circleSpeedY = bounce(circlePos,rectMove[i],circleSize,circleSpeedY)

                if circleSpeedY < 0:
                    rectMove[i][1] += 1

                rectMove[i][0] += rectMove[i][4]
                if (rectMove[i][0] + rectMove[i][2]) >= surfaceWidth or rectMove[i][0] < 0:
                    rectMove[i][4] = -rectMove[i][4]

                if (rectMove[i][1] + rectMove[i][3]) >= groundLevel:
                    rectMove[i][0] = random.randrange(surfaceWidth - 35)
                    rectMove[i][1] = random.randrange(groundLevel - 25)
            
            circlePos[1] += circleSpeedY

            if circlePos[0] > surfaceWidth:
                circlePos[0] = 0
            elif circlePos[0] < 0:
                circlePos[0] = surfaceWidth
 
            #Bringing up the GAME OVER screen
            if circleFall:
                gameState = "game_over"
                

        
        #GAME OVER screen
        if gameState == "game_over":
            mainSurface.fill("black")
            pygame.draw.rect(mainSurface, "red", rectPRD)
            text3 = "GAME OVER"
            text4 = "Retry"
            renderedText3 = font3.render(text3, 1, pygame.Color("red"))
            renderedText4 = font2.render(text4, 1, pygame.Color("black"))
            mainSurface.blit(renderedText3, (30,120))
            mainSurface.blit(renderedText4, (180,575))
            if ev.type == pygame.MOUSEBUTTONUP:
                if rectPRD[0] < pygame.mouse.get_pos()[0] < (rectPRD[0] + rectPRD[2])\
                   and rectPRD[1] < pygame.mouse.get_pos()[1] < (rectPRD[1] + rectPRD[3]):
                    gameState = "game"
                    circleFall = False
                    circlePos[1] = 250

       

        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()

main()
