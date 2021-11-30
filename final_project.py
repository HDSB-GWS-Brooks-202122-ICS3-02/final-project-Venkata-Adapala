import pygame


def  bounce(circleCoords,rectCoords,cSize):
        if rectCoords[0] < circleCoords[0] < (rectCoords[0] + rectCoords[2])\
           and rectCoords[1] < (circleCoords[1] + cSize) < (rectCoords[1] + rectCoords[3]):
            circleCoords[1] += -325
            

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      
    surfaceWidth = 450
    surfaceHeight = 780 
    
    clock = pygame.time.Clock()  


    mainSurface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
    
    
    circlePos = [250,275]
    circleSize = 30
    circleColor = "red"
    circleSpeedY = 0
    rect1D = [210,450,35,15]
    jumping = False
    direction = "up"
    
    groundLevel = 755
    
    moveCircleRight = False 
    moveCircleLeft = False
            
    while True:
        ev = pygame.event.poll()   
        if ev.type == pygame.QUIT:  
            break
        
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
                
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if (not jumping):
                circleSpeedY = -21
                
                jumping = True

        bounce(circlePos,rect1D,circleSize)   
        circlePos[1] += circleSpeedY

        
        if ((circlePos[1] + circleSize) > groundLevel):
            circlePos[1] = groundLevel - circleSize
            
            circleSpeedY = 0
            
            jumping = False
        
        else:
            circleSpeedY += 0.325
            

        if circlePos[0] > surfaceWidth:
            circlePos[0] = 0
        elif circlePos[0] < 0:
            circlePos[0] = surfaceWidth
            

        mainSurface.fill("dodgerblue")
      
        pygame.draw.rect(mainSurface,"lightgray", (0,groundLevel,surfaceWidth,surfaceHeight-groundLevel))
        pygame.draw.rect(mainSurface,"darkgreen", rect1D)
        pygame.draw.circle(mainSurface, circleColor, (circlePos[0],circlePos[1]), circleSize)

        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()

main()
