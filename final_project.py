import pygame
import random   

def main():

    pygame.init()
 
    #Screen dimensions & stuff
    surfaceWidth = 560
    surfaceHeight = 980
    groundLevel = surfaceHeight - 55
    mainSurface = pygame.display.set_mode((surfaceWidth,surfaceHeight))             #Creating the screen
    
    gameState = "start"             #Setting the game state
    clock = pygame.time.Clock()             #Controlling the FPS
    
    #Font data
    font = pygame.font.SysFont("Candara", 94)
    font2 = pygame.font.SysFont("Tahoma", 50)
    font3 = pygame.font.SysFont("Impact", 113)
    font4 = pygame.font.SysFont("Verdana", 38)
    font5 = pygame.font.SysFont("Times New Roman", 63)

    startBG = pygame.image.load("wallpapers/white_wallp2.jpg")
    gameBG = pygame.image.load("wallpapers/white-brick-wall-planning-iphone-11.jpg")

    #Sprite data
    spriteImgMain = pygame.image.load("sprites/spriteMain.png")             #Loading the main sprite
    spriteImgMainX = pygame.transform.scale(spriteImgMain, (48, 48))                #Scaling it up to the desirable size
    
##    #Lizard
##    spriteLizard = pygame.image.load("lizard_f_idle_anim_f0.png")
##    spriteLizard2x = pygame.transform.scale2x(spriteLizard)
##    spriteLizardPos = [200,225]
##
##    #Elf
##    spriteElf = pygame.image.load("elf_m_idle_anim_f0.png")
##    spriteElf2x = pygame.transform.scale2x(spriteElf)
##    spriteElfPos = [200,325]
##
##    #Knight
##    spriteKnight = pygame.image.load("knight_f_idle_anim_f0.png")
##    spriteKnight2x = pygame.transform.scale2x(spriteKnight)
##    spriteKnightPos = [200,425]

    spriteMainPos = [225,250]
    spriteSpeedY = 0
    spriteFall = False

    #Pad data
    padStart = pygame.image.load("sprites/pad_start.png")
    padNormal = pygame.image.load("sprites/pad_normal.png")
    padMove = pygame.image.load("sprites/pad_move.png")
    padTramp = pygame.image.load("sprites/pad_tramp.png")
    padSpike = pygame.image.load("sprites/pad_spike.png")
    padTrap = pygame.image.load("sprites/pad_trap.png")
    padMoveSpike = pygame.image.load("sprites/pad_movespike.png")
    padBreak = pygame.image.load("sprites/pad_break.png")
    
    padSpeed = 0
    jumping = False

    rectPRD = [125,575,200,55]
    rectCD = [125,500,200,55]
    moveSpriteRight = False
    moveSpriteLeft = False
    
    #Score data
    score = 0
    initialPos = 0
    finalPos = 0


    #Randomising pad placement

    padStartPos = []
    padNormalPos = []
    padMovePos = []
    padTrampPos = []
    padSpikePos = []
    padMoveSpikePos = []
    padTrapPos = []
    padBreakPos = []
    
    for i in range(3):
        padNormalPos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])
        padMovePos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0), 0.8])
        padSpikePos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])
            
    for i in range(2):
        padTrampPos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])
        padTrapPos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])
        padMoveSpikePos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0), 0.8])
        padBreakPos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])

    for i in range(10, 560, 55):
        padStartPos.append([i, 600])
    

#Methods
    #Method for sprite-pad collision detection
    def spritePadCol(spriteCoords, padCoords, spriteSpeedY):
        if ((padCoords[0] - 25) < spriteCoords[0] < (padCoords[0] + 25))\
           and ((padCoords[1]  - 15) < (spriteCoords[1] + 25) < (padCoords[1] + 10)) and spriteSpeedY > 0:
            return True

    #Method for sprite-mouse collision detection
    def spriteMouseCol(spriteCoords, mouseCoords):
        if ((spriteCoords[0] - 5) < mouseCoords[0] < (spriteCoords[0] + 35))\
           and ((spriteCoords[1] + 5)) < mouseCoords[1] < (spriteCoords[1] + 60):
            return True

    #Method for mouse-rect collision detection
    def mouseRectCol(rectCoords, mouseCoords):
        if rectCoords[0] < mouseCoords[0] < (rectCoords[0] + rectCoords[2])\
           and rectCoords[1] < mouseCoords[1] < (rectCoords[1] + rectCoords[3]):
            return True
    
    #Method for moving the pads downwards
    def moveDownwards(padCoords, spriteSpeedY, padSpeed):
        if spriteSpeedY < 0:
            padCoords[1] += padSpeed
    
    #Method for redrawing the pads at random locations after they go below the screen
    def padRespawn(padCoords, groundLevel):
        if padCoords[1]>= (groundLevel - 10):
            padCoords[0] = random.randrange(surfaceWidth - 55)
            padCoords[1] = -15

    #Method for moving the pads sideways
    def moveSideways(padCoords, surfaceWidth):
        padCoords[0] += padCoords[2]
        if padCoords[0] >= (surfaceWidth - 27) or padCoords[0] <= 3:
            padCoords[2] = -padCoords[2]



    #Main game loop
    while True:
        ev = pygame.event.poll()   
        if ev.type == pygame.QUIT:
            break


       
        #Start screen
        if gameState == "start":
            mainSurface.blit(startBG, [0,0])
            pygame.draw.rect(mainSurface, "black", rectPRD)
##            pygame.draw.rect(mainSurface, "orchid", rectCD)
            text1 = "Whirlybird"
            text2 = "Play"
##            textC = "Customize"
            renderedText1 = font.render(text1, 1, pygame.Color("black"))
            renderedText2 = font2.render(text2, 1, pygame.Color("snow"))
##            renderedTextC = font2.render(textC, 1, pygame.Color("black"))
            mainSurface.blit(renderedText1, (70,115))
            mainSurface.blit(renderedText2, (190,575))
##            mainSurface.blit(renderedTextC, (135, 500))
            if ev.type == pygame.MOUSEBUTTONUP:
##                if mouseRectCol(rectCD, pygame.mouse.get_pos()):
##                    gameState = "customize"
                if mouseRectCol(rectPRD, pygame.mouse.get_pos()):
                    gameState = "game"


##        #Customization screen
##        if gameState == "customize":
##            mainSurface.fill("purple")
##            pygame.draw.rect(mainSurface, "snow", rectPRD)
##            
##            textChoose = "Choose your Avatar"
##            renderedTextChoose = font5.render(textChoose, 1, pygame.Color("black"))
##            mainSurface.blit(renderedTextChoose, (30,115))
##            mainSurface.blit(renderedText2, (190,575))
##            
##            mainSurface.blit(spriteLizard2x, spriteLizardPos)
##            mainSurface.blit(spriteElf2x, spriteElfPos)
##            mainSurface.blit(spriteKnight2x, spriteKnightPos)
##            if ev.type == pygame.MOUSEBUTTONUP:
##                if spriteMouseCol(spriteLizardPos, pygame.mouse.get_pos()):
##                    spriteMain = spriteLizard2x
##                    print("You have selected - Lizard")
##                elif spriteMouseCol(spriteElfPos, pygame.mouse.get_pos()):
##                    spriteMain = spriteElf2x
##                    print("You have selected - Elf")
##                elif spriteMouseCol(spriteKnightPos, pygame.mouse.get_pos()):
##                    spriteMain = spriteKnight2x
##                    print("You have selected - Knight")
##
##                if mouseRectCol(rectPRD, pygame.mouse.get_pos()):
##                    gameState = "game"
                    


        #Game screen
        if gameState == "game":
            
            mainSurface.blit(gameBG, [0,0])
            
            #Drawing the sprites
            spriteMain = spriteImgMainX
            mainSurface.blit(spriteMain, spriteMainPos)
            pygame.draw.rect(mainSurface, (35, 30, 25), (0, groundLevel, surfaceWidth, surfaceHeight-groundLevel))

        #Displaying the 'pads'
            #The starting pad
            for i in range(len(padStartPos)):
                padStartX = pygame.transform.scale(padStart, (50, 50))
                mainSurface.blit(padStartX, padStartPos[i])
            
            #The normal pads
            for i in range(len(padNormalPos)):
                padNormalX = pygame.transform.scale(padNormal, (66,27))
                mainSurface.blit(padNormalX, padNormalPos[i])

            #The sideways moving pads
            for i in range(len(padMovePos)):
                padMoveX = pygame.transform.scale(padMove, (66,27))
                mainSurface.blit(padMoveX, padMovePos[i][:2])

            #The trampoline-like pads
            for i in range(len(padTrampPos)):
                padTrampX = pygame.transform.scale(padTramp, (66,27))
                mainSurface.blit(padTrampX, padTrampPos[i])

            #The pads that kill the sprite
            for i in range(len(padSpikePos)):
                padSpikeX = pygame.transform.scale(padSpike, (66,27))
                mainSurface.blit(padSpikeX, padSpikePos[i])

            #The pad which is actually a trap (doesn't let the sprite bounce)
            for i in range(len(padTrapPos)):
                padTrapX = pygame.transform.scale(padTrap, (66,27))
                mainSurface.blit(padTrapX, padTrapPos[i])

            #The pad which kills the sprite but it's moving now
            for i in range(len(padMoveSpikePos)):
                padMoveSpikeX = pygame.transform.scale(padMoveSpike, (66,27))
                mainSurface.blit(padMoveSpikeX, padMoveSpikePos[i][:2])

            #The pads that break upon the sprite landing
            for i in range(len(padBreakPos)):
                padBreakX = pygame.transform.scale(padBreak, (66,27))
                mainSurface.blit(padBreakX, padBreakPos[i])


            #Displaying score
            textScore = str(score)
            renderedTextScore = font4.render(textScore, 1, pygame.Color("white"))
            mainSurface.blit(renderedTextScore, (225, groundLevel-7))


            
            #Moving the sprite sideways with keys
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RIGHT:
                    moveSpriteRight = True
                elif ev.key == pygame.K_LEFT:
                    moveSpriteLeft = True
            elif ev.type == pygame.KEYUP:
                if ev.key == pygame.K_RIGHT:
                    moveSpriteRight = False
                elif ev.key == pygame.K_LEFT:
                    moveSpriteLeft = False            
             
            if (spriteMainPos[1] < groundLevel) and moveSpriteRight:
                spriteMainPos[0] += 4.5
            elif (spriteMainPos[1] < groundLevel) and moveSpriteLeft:
                spriteMainPos[0] -= 4.5
          

            #Making the sprite jump and bounce
            if spriteMainPos[1] > groundLevel:
                spriteMainPos[1] = groundLevel
                spriteSpeedY = 0
                jumping = False
                spriteFall = True
            else:
                spriteSpeedY += 0.3

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if jumping == False:
                    spriteSpeedY = -23
                    jumping = True
                    spriteSpeedY += 0.3


        #Making the pads work        
            if spriteSpeedY <= 0 and spriteMainPos[1] > 30:
                padSpeed = - spriteSpeedY / 4
            elif spriteMainPos[1] <= 30:
                padSpeed = - spriteSpeedY / 2
                
            #The starting pad
            for i in range(len(padStartPos)):
                moveDownwards(padStartPos[i], spriteSpeedY, padSpeed)
                if spritePadCol(spriteMainPos, padStartPos[i], spriteSpeedY):
                    spriteSpeedY = -46

            #The normal, stationary pads
            for i in range(len(padNormalPos)):
                moveDownwards(padNormalPos[i], spriteSpeedY, padSpeed)
                padRespawn(padNormalPos[i], groundLevel)
                if spritePadCol(spriteMainPos, padNormalPos[i], spriteSpeedY):
                    spriteSpeedY = -23
            
            #The sideways moving pads
            for i in range(len(padMovePos)):
                moveSideways(padMovePos[i],surfaceWidth)
                moveDownwards(padMovePos[i], spriteSpeedY, padSpeed)
                padRespawn(padMovePos[i], groundLevel)
                if spritePadCol(spriteMainPos, padMovePos[i], spriteSpeedY):
                    spriteSpeedY = -23
             
            #The trampoline-like pads
            for i in range(len(padTrampPos)):
                moveDownwards(padTrampPos[i], spriteSpeedY, padSpeed)                
                padRespawn(padTrampPos[i], groundLevel)
                if spritePadCol(spriteMainPos, padTrampPos[i], spriteSpeedY):
                    spriteSpeedY = -46
            
            #The pads which kill the sprite
            for i in range(len(padSpikePos)):
                moveDownwards(padSpikePos[i], spriteSpeedY, padSpeed)
                padRespawn(padSpikePos[i], groundLevel)
                if spritePadCol(spriteMainPos, padSpikePos[i], spriteSpeedY):
                    spriteFall = True

            #The pads which kill the sprite but they're moving now
            for i in range(len(padMoveSpikePos)):
                moveSideways(padMoveSpikePos[i],surfaceWidth)
                moveDownwards(padMoveSpikePos[i], spriteSpeedY, padSpeed)
                padRespawn(padMoveSpikePos[i], groundLevel)
                if spritePadCol(spriteMainPos, padMoveSpikePos[i], spriteSpeedY):
                    spriteFall = True
             
            #The pads which are actually traps (doesn't let the ball bounce)
            for i in range(len(padTrapPos)):
                moveDownwards(padTrapPos[i], spriteSpeedY, padSpeed)
                padRespawn(padTrapPos[i], groundLevel)
                if spritePadCol(spriteMainPos, padTrapPos[i], spriteSpeedY):
                    padTrapPos[i] = [random.randrange(surfaceWidth - 45), -15]
                    break
             
            #The pads which break once the sprite bounces on it
            for i in range(len(padBreakPos)):
                moveDownwards(padBreakPos[i], spriteSpeedY, padSpeed)
                padRespawn(padBreakPos[i], groundLevel)
                if spritePadCol(spriteMainPos, padBreakPos[i], spriteSpeedY):
                    spriteSpeedY = -23
                    padBreakPos[i] = [random.randrange(surfaceWidth - 45), -15]
                    break
                
            spriteMainPos[1] += spriteSpeedY


            if spriteMainPos[0] > surfaceWidth:
                spriteMainPos[0] = 0
            elif spriteMainPos[0] < 0:
                spriteMainPos[0] = surfaceWidth

            if spriteMainPos[1] <= 30:
                spriteMainPos[1] = 30


            #Creating the score mechanism
            if spriteSpeedY > 0:
                finalPos = spriteMainPos[1]
            elif spriteSpeedY < 0:
                initialPos = spriteMainPos[1]
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
            if spriteFall:
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
            mainSurface.blit(renderedTextScore, (235,285))
            mainSurface.blit(renderedTextDisplayScore, (127,285))
            mainSurface.blit(renderedTextHighScore, (285, 400))
            mainSurface.blit(renderedTextDisplayHighScore, (65,400))
            if ev.type == pygame.MOUSEBUTTONUP:
                if mouseRectCol(rectPRD, pygame.mouse.get_pos()):
                    gameState = "game"
                    spriteFall = False
                    spriteMainPos = [225,250]
                    moveSpriteLeft = False
                    moveSpriteRight = False
                    score = 0



        #Displaying the screen
        pygame.display.flip()

        #Setting the FPS to 60
        clock.tick(60)

    pygame.quit()

main()
