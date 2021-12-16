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
    font4 = pygame.font.SysFont("Verdana", 30)

    groundLevel = surfaceHeight - 25

    #Circle and Rectangle data
    circleSize = 27.5
    circlePos = [225,250]
    circleColor = "red"
    splCirclePos = [random.randrange(surfaceWidth - 35), random.randrange(groundLevel - 55)]
    #splCircleColor = "magenta"
    #splCircleSize = 15
    circleSpeedY = 0
    circleFall = False
    
    rectPRD = [125,575,200,55]
    rectSpeed = 2.5
    jumping = False
    
    moveCircleRight = False 
    moveCircleLeft = False
    
    #Score data
    score = 0
    initialPos = 0
    finalPos = 0
    scoreX = 200

    #Randomising rectangle placement
    rectNormal = []
    for i in range(2):
        rectNormal.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12])

    rectMove = []
    for i in range(2):
        rectMove.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12,0.8])
        
    rectTramp = []
    for i in range(2):
        rectTramp.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12])
        
    rectSpike = []
    for i in range(2):
        rectSpike.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12])
        
    rectMoveSpike = []
    for i in range(2):
        rectMoveSpike.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12,0.8])
        
    rectTrap = []
    for i in range(1):
        rectTrap.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12,0.8])
        
    rectBreak = []
    for i in range(2):
        rectBreak.append([random.randrange(surfaceWidth - 35),random.randrange(groundLevel - 55),35,12,0.8])


    #Creating a method for rectangle collision detection and bouncing
    def bounce(circleCoords,rectCoords,cSize,circleSpeedY):
        if rectCoords[0] < circleCoords[0] < (rectCoords[0] + rectCoords[2])\
           and rectCoords[1] < (circleCoords[1] + cSize) < (rectCoords[1] + rectCoords[3] + 10)\
           and circleSpeedY > 0:
            return -21
        else:
            return circleSpeedY
        
    def bounceTwiceAsHigh(circleCoords,rectCoords,cSize,circleSpeedY):
        if rectCoords[0] < circleCoords[0] < (rectCoords[0] + rectCoords[2])\
           and rectCoords[1] < (circleCoords[1] + cSize) < (rectCoords[1] + rectCoords[3] + 10)\
           and circleSpeedY > 0:
            return -42
        else:
            return circleSpeedY
     
    def bounceAndVanish(circleCoords,rectCoords,cSize,circleSpeedY):
        if rectCoords[0] < circleCoords[0] < (rectCoords[0] + rectCoords[2])\
           and rectCoords[1] < (circleCoords[1] + cSize) < (rectCoords[1] + rectCoords[3] + 10)\
           and circleSpeedY > 0:
            return (-21, True)
        else:
            return (circleSpeedY, False)
        
    def moveDownwards(rectCoords, circleSpeedY, rectSpeed):
        if circleSpeedY < 0:
                    rectCoords[i][1] += rectSpeed
    
    def rectRespawn(rectCoords,groundLevel):
        if (rectCoords[i][1] + rectCoords[i][3]) >= groundLevel:
            rectCoords[i][0] = random.randrange(surfaceWidth - 35)
            rectCoords[i][1] = random.randrange(350)

    def flyHigh(circle1Coords,circle2Coords,cSize,circleSpeedY):
        if circle2Coords[0] < circle1Coords[0] < (circle2Coords[0] + circle2Coords[2])\
           and circle2Coords[1] < (circle1Coords[1] + cSize) < (circle2Coords[1] + circle2Coords[3] + 10)\
           and circleSpeedY > 0:
            return -42
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
            pygame.draw.rect(mainSurface, (35, 30, 25), (0,groundLevel,surfaceWidth,surfaceHeight-groundLevel))
            pygame.draw.circle(mainSurface, circleColor, circlePos, circleSize)
            #pygame.draw.circle(mainSurface, splCircleColor, splCirclePos, splCircleSize)
        
            for i in range(len(rectNormal)):
                pygame.draw.rect(mainSurface, "navy", (rectNormal[i][:4]))
            for i in range(len(rectMove)):
                pygame.draw.rect(mainSurface, "yellow", (rectMove[i][:4]))
            for i in range(len(rectTramp)):
                pygame.draw.rect(mainSurface, "green", (rectTramp[i][:4]))
            for i in range(len(rectSpike)):
                pygame.draw.rect(mainSurface, "black", (rectSpike[i][:4]))
            for i in range(len(rectMoveSpike)):
                pygame.draw.rect(mainSurface, "darkred", (rectMoveSpike[i][:4]))
            for i in range(len(rectTrap)):
                pygame.draw.rect(mainSurface, "white", (rectTrap[i][:4]))
            for i in range(len(rectBreak)):
                pygame.draw.rect(mainSurface, "darkgreen", (rectBreak[i][:4]))

            #Displaying score
            textScore = str(score)
            renderedTextScore = font4.render(textScore, 1, pygame.Color("white"))
            mainSurface.blit(renderedTextScore, (scoreX,groundLevel-7))
            if score >= 10000:
                scoreX = 185
            

           #Changing the ball's colors 
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_b:
                    circleColor = "black"
                elif ev.key == pygame.K_y:
                    circleColor = "yellow"
                elif ev.key == pygame.K_o:
                    circleColor = "orange"
                elif ev.key == pygame.K_g:
                    circleColor = "green"
                elif ev.key == pygame.K_r:
                    circleColor = "red"
            
            
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
                    jumping = True


        #Making the rectangles work     
            if circleSpeedY < 0:
                rectSpeed = -1*(circleSpeedY/5)
                
            #The normal, stationary rectangle
            for i in range(len(rectNormal)):
                
                circleSpeedY = bounce(circlePos,rectNormal[i],circleSize,circleSpeedY)
                moveDownwards(rectNormal, circleSpeedY, rectSpeed)
                rectRespawn(rectNormal, groundLevel)
            
            #The sideways moving rectangle
            for i in range(len(rectMove)):
                
                circleSpeedY = bounce(circlePos,rectMove[i],circleSize,circleSpeedY)
                moveDownwards(rectMove, circleSpeedY, rectSpeed)
                rectRespawn(rectMove, groundLevel)

                rectMove[i][0] += rectMove[i][4]
                if (rectMove[i][0] + rectMove[i][2]) >= surfaceWidth or rectMove[i][0] < 0:
                    rectMove[i][4] = -rectMove[i][4]
             
            #The trampoline-like rectangle
            for i in range(len(rectTramp)):

                circleSpeedY = bounceTwiceAsHigh(circlePos,rectTramp[i],circleSize,circleSpeedY)
                moveDownwards(rectTramp, circleSpeedY, rectSpeed)                
                rectRespawn(rectTramp, groundLevel)
            
            #The rectangle which kills the circle
            for i in range(len(rectSpike)):
                if rectSpike[i][0] < circlePos[0] < (rectSpike[i][0] + rectSpike[i][2])\
                   and rectSpike[i][1] < (circlePos[1] + circleSize) < (rectSpike[i][1] + rectSpike[i][3] + 10)\
                   and circleSpeedY > 0:
                    circleFall = True

                moveDownwards(rectSpike, circleSpeedY, rectSpeed)
                rectRespawn(rectSpike, groundLevel)
             
            #The rectangle which kills the circle but it's moving now
            for i in range(len(rectMoveSpike)):
                if rectMoveSpike[i][0] < circlePos[0] < (rectMoveSpike[i][0] + rectMoveSpike[i][2])\
                   and rectMoveSpike[i][1] < (circlePos[1] + circleSize) < (rectMoveSpike[i][1] + rectMoveSpike[i][3] + 10)\
                   and circleSpeedY > 0:
                    circleFall = True

                rectMoveSpike[i][0] += rectMoveSpike[i][4]
                if (rectMoveSpike[i][0] + rectMoveSpike[i][2]) >= surfaceWidth or rectMoveSpike[i][0] < 0:
                    rectMoveSpike[i][4] = -rectMoveSpike[i][4]
                
                moveDownwards(rectMoveSpike, circleSpeedY, rectSpeed)
                rectRespawn(rectMoveSpike, groundLevel)
             
            #The rectangle which is actually a trap (doesn't let the ball bounce)
            for i in range(len(rectTrap)):

                moveDownwards(rectTrap, circleSpeedY, rectSpeed)
                rectRespawn(rectTrap, groundLevel)
             
            #The rectangle which breaks once the ball bounces on it
            for i in range(len(rectBreak)):
                circleSpeedY, breakBlock = bounceAndVanish(circlePos,rectBreak[i],circleSize,circleSpeedY)

                if breakBlock:
                    rectBreak.pop(i)
                    break
                
                moveDownwards(rectBreak, circleSpeedY, rectSpeed)
                rectRespawn(rectBreak, groundLevel)
            
            circlePos[1] += circleSpeedY

            if circlePos[0] > surfaceWidth:
                circlePos[0] = 0
            elif circlePos[0] < 0:
                circlePos[0] = surfaceWidth

            if circlePos[1] <= 27.5:
                circlePos[1] = 27.5


            #Creating the score mechanism
            if circleSpeedY > 0:
                finalPos = circlePos[1]
            elif circleSpeedY < 0:
                initialPos = circlePos[1]
                score += int((finalPos - initialPos)//15)
            
            if score < 0:
                score = 0

            #Updating the high score using a file
            file = open('High Score.txt', 'r')
            highScore = file.readlines()
            file.close()
            if score > int(highScore[0]):
                highScore = str(score)
                file = open('High Score.txt', 'w')
                file.write(highScore)
                file.close()
            
            
            #Bringing up the GAME OVER screen
            if circleFall:
                gameState = "game_over"
           
            
         
         #GAME OVER screen
        if gameState == "game_over":
            mainSurface.fill("black")
            pygame.draw.rect(mainSurface, "red", rectPRD)
            text3 = "GAME OVER"
            text4 = "Retry"
            textDisplayScore = "Score: "
            textHighScore = str(int(highScore[0]))
            textDisplayHighScore = "HIGH SCORE: "
            renderedText3 = font3.render(text3, 1, pygame.Color("red"))
            renderedText4 = font2.render(text4, 1, pygame.Color("black"))
            renderedTextScore = font4.render(textScore, 1, pygame.Color("white"))
            renderedTextDisplayScore = font4.render(textDisplayScore, 1, pygame.Color("white"))
            renderedTextHighScore = font4.render(textHighScore, 1, pygame.Color("yellow"))
            renderedTextDisplayHighScore = font4.render(textDisplayHighScore, 1, pygame.Color("yellow"))
            mainSurface.blit(renderedText3, (30,75))
            mainSurface.blit(renderedText4, (180,575))           
            mainSurface.blit(renderedTextScore, (235,275))
            mainSurface.blit(renderedTextDisplayScore, (125,275))
            mainSurface.blit(renderedTextHighScore, (290, 390))
            mainSurface.blit(renderedTextDisplayHighScore, (70,390))
            if ev.type == pygame.MOUSEBUTTONUP:
                if rectPRD[0] < pygame.mouse.get_pos()[0] < (rectPRD[0] + rectPRD[2])\
                   and rectPRD[1] < pygame.mouse.get_pos()[1] < (rectPRD[1] + rectPRD[3]):
                    gameState = "game"
                    circleFall = False
                    circlePos = [225,250]
                    moveCircleLeft = False
                    moveCircleRight = False
                    score = 0


        #Displaying the screen
        pygame.display.flip()

        #Setting the fps to 60
        clock.tick(60)

    pygame.quit()

main()
