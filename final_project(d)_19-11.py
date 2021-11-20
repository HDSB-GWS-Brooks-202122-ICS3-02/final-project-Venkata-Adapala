import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      
    surfaceWidth = 530
    surfaceHeight = 945 
    
    clock = pygame.time.Clock()  


    mainSurface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
    
    
    circlePos = [250,500]
    circleSize = 30
    circleColor = "red"
    circleSpeedY = 0;
    jumping = False
    
    groundLevel = 900
    
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
 
       
        circlePos[1] += circleSpeedY
        
        if ((circlePos[1] + circleSize) > groundLevel):
            circlePos[1] = groundLevel - circleSize
            
            circleSpeedY = 0
            
            jumping = False
        
        else:
            circleSpeedY += 0.3
            
        if circlePos[0] > surfaceWidth:
            circlePos[0] = 0
        elif circlePos[0] < 0:
            circlePos[0] = surfaceWidth
            

        mainSurface.fill("dodgerblue")
      
        pygame.draw.rect(mainSurface,"lightgray", (0,groundLevel,surfaceWidth,surfaceHeight-groundLevel))
        pygame.draw.circle(mainSurface, circleColor, (circlePos[0],circlePos[1]), circleSize)

        pygame.display.flip()
        
        clock.tick(60)

    pygame.quit()

main()
