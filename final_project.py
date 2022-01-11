import pygame
import random
import ctypes

ctypes.windll.user32.SetProcessDPIAware()                                     #Displaying the pixels correctly


#Defining important variables

#Screen dimensions
surfaceWidth = 550
surfaceHeight = 980
groundLevel = surfaceHeight - 55

rectPRD = [160,725,230,75]
rectHD = [160,625,230,75]
    
#Pad positions
padStartPos = []
padNormalPos = []
padMovePos = []
padTrampPos = []
padSpikePos = []
padMoveSpikePos = []
padTrapPos = []
padBreakPos = []

#A method to constantly randomize pad placement
def padPlacement():
    
    global padNormalPos
    global padMovePos
    global padTrampPos
    global padTrapPos
    global padSpikePos
    global padMoveSpikePos
    global padBreakPos
    global padStartPos
        
    padStartPos = []
    padNormalPos = []
    padMovePos = []
    padTrampPos = []
    padSpikePos = []
    padMoveSpikePos = []
    padTrapPos = []
    padBreakPos = []

    #Only 3 such pads should be displayed at a time
    for i in range(3):
        padNormalPos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])
        padMovePos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0), 0.8])
              
    #Only 2 such pads should be displayed at a time
    for i in range(2):
        padTrampPos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])
        padTrapPos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])
        padSpikePos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])
        padMoveSpikePos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0), 0.8])
        padBreakPos.append([random.randrange(surfaceWidth - 55), random.randrange(-980, 0)])

    #A series of these sprites must be displayed
    for i in range(10, 560, 55):
        padStartPos.append([i, 600])



def main():

    pygame.init()
 
    mainSurface = pygame.display.set_mode((surfaceWidth,surfaceHeight))       #Creating the screen
    
    gameState = "start"                                                       #Setting the game state
    clock = pygame.time.Clock()                                               #Controlling the FPS
    
    #Font data
    font = pygame.font.SysFont("Candara", 100)
    font2 = pygame.font.SysFont("Tahoma", 50)
    font3 = pygame.font.SysFont("Impact", 113)
    font4 = pygame.font.SysFont("Verdana", 38)
    font5 = pygame.font.SysFont("Times New Roman", 63)

    #Loading various backgrounds
    startBG = pygame.image.load("wallpapers/white_wallp2.jpg")
    gameBG = pygame.image.load("wallpapers/white_brick_wp.jpg")
    helpBG1 = pygame.image.load("wallpapers/helpBG1.jpg")
    helpBG2 = pygame.image.load("wallpapers/helpBG2.jpg")
    
    #Main sprite data
    spriteImgMain = pygame.image.load("sprites/spriteMain.png")               #Loading the main sprite
    spriteImgMainX = pygame.transform.scale(spriteImgMain, (48, 48))          #Scaling it up to the desirable size
    spriteMainPos = [250,250]
    spriteSpeedY = 0
    moveSpriteRight = False
    moveSpriteLeft = False
    spriteFall = False                                                        #The game's over when this is True
    
#     #Lizard
#     spriteLizard = pygame.image.load("lizard_f_idle_anim_f0.png")
#     spriteLizard2x = pygame.transform.scale2x(spriteLizard)
#     spriteLizardPos = [200,225]
# 
#     #Elf
#     spriteElf = pygame.image.load("elf_m_idle_anim_f0.png")
#     spriteElf2x = pygame.transform.scale2x(spriteElf)
#     spriteElfPos = [200,325]
# 
#     #Knight
#     spriteKnight = pygame.image.load("knight_f_idle_anim_f0.png")
#     spriteKnight2x = pygame.transform.scale2x(spriteKnight)
#     spriteKnightPos = [200,425]

    #Loading the pad sprites
    padStart = pygame.image.load("sprites/pad_start.png")
    padNormal = pygame.image.load("sprites/pad_normal.png")
    padMove = pygame.image.load("sprites/pad_move.png")
    padTramp = pygame.image.load("sprites/pad_tramp.png")
    padSpike = pygame.image.load("sprites/pad_spike.png")
    padTrap = pygame.image.load("sprites/pad_trap.png")
    padMoveSpike = pygame.image.load("sprites/pad_movespike.png")
    padBreak = pygame.image.load("sprites/pad_break.png")    
    padSpeed = 0
    
    padPlacement()                                                            #Randomizing pad placement
    
    #Score data
    score = 0
    initialPos = 0
    finalPos = 0
    

#Methods
    #Method for sprite-pad collision detection
    def spritePadCol(spriteCoords, padCoords, spriteSpeedY):
        if ((padCoords[0] - 50) < spriteCoords[0] < (padCoords[0] + 50))\
           and ((padCoords[1]  - 15) < (spriteCoords[1] + 50) < (padCoords[1] + 10)) and spriteSpeedY > 0:
            return True

#      #Method for sprite-mouse collision detection
#      def spriteMouseCol(spriteCoords, mouseCoords):
#          if ((spriteCoords[0] - 5) < mouseCoords[0] < (spriteCoords[0] + 35))\
#             and ((spriteCoords[1] + 5)) < mouseCoords[1] < (spriteCoords[1] + 60):
#              return True

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
        if padCoords[0] >= (surfaceWidth - 60) or padCoords[0] <= 3:
            padCoords[2] = -padCoords[2]



    #Main game loop
    while True:
        ev = pygame.event.poll()   
        if ev.type == pygame.QUIT:
            break


       
        #Start screen
        if gameState == "start":
            mainSurface.blit(startBG, [0,0])                                          #Loading the background
            pygame.draw.rect(mainSurface, "black", rectPRD)                           #Drawing the rect button
            pygame.draw.rect(mainSurface, "navy", rectHD)
            text1 = "Whirlybird"
            text2 = "Play"
            textH = "Help"
            renderedText1 = font.render(text1, True, pygame.Color("black"))
            renderedText2 = font2.render(text2, True, pygame.Color("snow"))
            renderedTextH = font2.render(textH, 1, pygame.Color("snow"))
            mainSurface.blit(renderedText1, (70,125))
            mainSurface.blit(renderedText2, (232,725))                                #Displaying the texts
            mainSurface.blit(renderedTextH, (225,625))
            if ev.type == pygame.MOUSEBUTTONUP:
                if mouseRectCol(rectHD, pygame.mouse.get_pos()):
                    gameState = "help1"
                if mouseRectCol(rectPRD, pygame.mouse.get_pos()):                     #Col-detection for the button
                    gameState = "game"



        #Help screen
        if gameState == "help1":
            mainSurface.blit(helpBG1, [0,0])
            pygame.draw.rect(mainSurface, "black", rectPRD)
            textN = "Next"
            renderedTextN = font2.render(textN, True, pygame.Color("snow"))
            mainSurface.blit(renderedTextN, (225,727))
            if ev.type == pygame.MOUSEBUTTONUP:
                if mouseRectCol(rectPRD, pygame.mouse.get_pos()):
                    gameState = "help2"
                    


        #Game screen
        if gameState == "game":           
            mainSurface.blit(gameBG, [0,0])
            
            #Drawing the sprites
            spriteMain = spriteImgMainX
            mainSurface.blit(spriteMain, spriteMainPos)                               #Displaying the main sprite
            pygame.draw.rect(mainSurface, (35, 30, 25), (0, groundLevel, surfaceWidth, surfaceHeight-groundLevel))

        #Displaying the 'pads'
            #The starting pads (looks like a series of small squares)
            for i in range(len(padStartPos)):
                padStartX = pygame.transform.scale(padStart, (50, 50))
                mainSurface.blit(padStartX, padStartPos[i])
            
            #The normal pads
            for i in range(len(padNormalPos)):
                padNormalX = pygame.transform.scale(padNormal, (62,24))
                mainSurface.blit(padNormalX, padNormalPos[i])

            #The sideways moving pads
            for i in range(len(padMovePos)):
                padMoveX = pygame.transform.scale(padMove, (62,24))
                mainSurface.blit(padMoveX, padMovePos[i][:2])

            #The trampoline-like pads
            for i in range(len(padTrampPos)):
                padTrampX = pygame.transform.scale(padTramp, (62,24))
                mainSurface.blit(padTrampX, padTrampPos[i])

            #The pads that kill the sprite
            for i in range(len(padSpikePos)):
                padSpikeX = pygame.transform.scale(padSpike, (62,24))
                mainSurface.blit(padSpikeX, padSpikePos[i])

            #The pads which are actually traps (they don't let the sprite bounce)
            for i in range(len(padTrapPos)):
                padTrapX = pygame.transform.scale(padTrap, (62,24))
                mainSurface.blit(padTrapX, padTrapPos[i])

            #The pads which kill the sprite but they're moving now
            for i in range(len(padMoveSpikePos)):
                padMoveSpikeX = pygame.transform.scale(padMoveSpike,(62,24))
                mainSurface.blit(padMoveSpikeX, padMoveSpikePos[i][:2])

            #The pads that break upon the sprite landing
            for i in range(len(padBreakPos)):
                padBreakX = pygame.transform.scale(padBreak, (62,24))
                mainSurface.blit(padBreakX, padBreakPos[i])

            #Displaying score
            textScore = str(score)
            textDisplayScore = "Score: "
            renderedTextScore = font4.render(textScore, True, pygame.Color("white"))
            renderedTextDisplayScore = font4.render(textDisplayScore, True, pygame.Color("white"))
            mainSurface.blit(renderedTextScore, (285, groundLevel))
            mainSurface.blit(renderedTextDisplayScore, (145, groundLevel))

            
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
             
            if moveSpriteRight:
                spriteMainPos[0] += 4.5
            elif moveSpriteLeft:
                spriteMainPos[0] -= 4.5
          

            #Making the sprite jump and bounce
            if spriteMainPos[1] >= groundLevel:
                spriteMainPos[1] = groundLevel
                spriteSpeedY = 0
                spriteFall = True
            else:
                spriteSpeedY += 0.45
                    
                    
            #Making the sprite appear on the other side of the screen once it goes off of it
            if spriteMainPos[0] > (surfaceWidth - 30):
                spriteMainPos[0] = -20
            elif spriteMainPos[0] < -20:
                spriteMainPos[0] = (surfaceWidth - 30)
            
            #Stopping the sprite from going above a certain height
            if spriteMainPos[1] <= 100:
                spriteMainPos[1] = 100


        #Making the pads work        
            
            #Manipulating the speed by which the pads move downwards
            if spriteSpeedY <= 0 and spriteMainPos[1] > 100:
                padSpeed = - (spriteSpeedY / 4)
            elif spriteMainPos[1] <= 100:
                padSpeed = - (spriteSpeedY / 2)
                
            #The starting series of pads
            for i in range(len(padStartPos)):
                moveDownwards(padStartPos[i], spriteSpeedY, padSpeed)
                if spritePadCol(spriteMainPos, padStartPos[i], spriteSpeedY):
                    spriteSpeedY = -52

            #The normal, stationary pads
            for i in range(len(padNormalPos)):
                moveDownwards(padNormalPos[i], spriteSpeedY, padSpeed)
                padRespawn(padNormalPos[i], groundLevel)
                if spritePadCol(spriteMainPos, padNormalPos[i], spriteSpeedY):
                    spriteSpeedY = -26
            
            #The sideways moving pads
            for i in range(len(padMovePos)):
                moveSideways(padMovePos[i],surfaceWidth)
                moveDownwards(padMovePos[i], spriteSpeedY, padSpeed)
                padRespawn(padMovePos[i], groundLevel)
                if spritePadCol(spriteMainPos, padMovePos[i], spriteSpeedY):
                    spriteSpeedY = -26
             
            #The trampoline-like pads
            for i in range(len(padTrampPos)):
                moveDownwards(padTrampPos[i], spriteSpeedY, padSpeed)                
                padRespawn(padTrampPos[i], groundLevel)
                if spritePadCol(spriteMainPos, padTrampPos[i], spriteSpeedY):
                    spriteSpeedY = -52
            
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
                    spriteSpeedY = -26
                    padBreakPos[i] = [random.randrange(surfaceWidth - 45), -15]
                    break
                
            spriteMainPos[1] += spriteSpeedY


            #Creating the score mechanism by calculating & adding the dist. covered by the sprite everytime it bounces
            if spriteSpeedY > 0:
                finalPos = spriteMainPos[1]
            elif spriteSpeedY < 0:
                initialPos = spriteMainPos[1]
                score += int((finalPos - initialPos)//15)
                
            #Ensuring that the score doesn't become negative
            if score < 0:
                score = 0

            #Updating the high score using a file
            file = open('High Score.txt', 'r')
            highScore = file.readlines()
            file.close()
            if score > int(highScore[0]):
                highScore[0] = str(score)
                file = open('High Score.txt', 'w')
                file.write(highScore[0])
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
            renderedText3 = font3.render(text3, True, pygame.Color("red"))
            renderedText4 = font2.render(text4, True, pygame.Color("black"))
            renderedTextScore = font4.render(textScore, True, pygame.Color("white"))
            renderedTextDisplayScore = font4.render(textDisplayScore, True, pygame.Color("white"))
            renderedTextHighScore = font4.render(textHighScore, True, pygame.Color("yellow"))
            renderedTextDisplayHighScore = font4.render(textDisplayHighScore, True, pygame.Color("yellow"))
            mainSurface.blit(renderedText3, (30,75))
            mainSurface.blit(renderedText4, (220,725))           
            mainSurface.blit(renderedTextScore, (295,350))
            mainSurface.blit(renderedTextDisplayScore, (150,350))
            mainSurface.blit(renderedTextHighScore, (345, 500))
            mainSurface.blit(renderedTextDisplayHighScore, (65,500))
            if ev.type == pygame.MOUSEBUTTONUP:
                if mouseRectCol(rectPRD, pygame.mouse.get_pos()):
                    padPlacement()
                    gameState = "game"
                    spriteFall = False
                    spriteMainPos = [250,250]
                    moveSpriteLeft = False
                    moveSpriteRight = False
                    score = 0



        #Displaying the screen
        pygame.display.flip()

        #Setting the FPS to 60
        clock.tick(60)

    pygame.quit()

main()