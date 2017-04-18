'''
Developer: Cristian Moncada

contributors:
      Cristian Moncada

Description: 2-demensional game where the user can develop and test out his/her map

Files: map.txt
'''

import pygame
from pygame.locals import *
import sys
import math

BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
      

class Ball(object):
      #sets the initial fram up on the screen
      def __init__(self, x, y, r, speedx, speedy):
            self.x = x
            self.y = y
            self.r = r
            self.speedx = speedx
            self.speedy = speedy
            
            self.color = (255, 0, 0)
            self.position = (self.x, self.y)

      #changes the color of the ball
      def changeColor(self, r, g, b):
            self.color = (r, g, b)

      #draws the ball on the screen
      def drawBall(self):
            pygame.draw.circle(screen, self.color, self.position, self.r)

      def moveUp(self):
            self.y = self.y - 50

      def moveDown(self):
            self.y = self.y + 50

      def moveRight(self):
            self.x = self.x + 50

      def moveLeft(self):
            self.x = self.x - 50

      #bounces the ball around the screen
      def moveBall(self):

            if (self.x + self.r + 1 > 1600):
                  self.x = 1600 - self.r

            if (self.x - self.r - 1 < 0):
                  self.x = self.r

            if (self.y + self.r + 1 > 900):
                  self.y = 900 - self.r
                
            if (self.y - self.r - 1 < 0):
                  self.y = self.r
                  
            self.position = (self.x, self.y)

      def stationaryBall(self):
            self.position = (self.x, self.y)

      def default(self):
            self.x = 775
            self.y = 425


class Controls():
      def __init__(self, w, h):
            self.w = w
            self.h = h

      #text button
      def ButtonText(self, x, y, text):
            color = (255, 255, 255)
            size = (x, y, self.w, self.h )
            pygame.draw.rect(screen, color, size)
            
            font = pygame.font.SysFont("monosace", 55)
            word = font.render(text, 1, (0, 0, 0))
            screen.blit(word, (x + 5, y))

      def Button(self, x, y, w, h, r, b, g):
            color = (r, b, g)
            size = (x, y, w, h)
            pygame.draw.rect(screen, color, size)

      def Touch(self, x, y, mouseX, mouseY):
            if (mouseX > x and mouseY > y and mouseX < (x + self.w) and mouseY < (y + self.h)):
                  return True
            else:
                  return False

      #creats the options from what th user can use
      def mapMaker(self, x, y):
            row = 0
            cullum = 0
            size = (x, y, 30, 30)
            color = (0, 0, 0)

            preview = [[1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
                       [1, 1, 0, 1, 2, 0, 2, 1, 0, 2, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
                       [1, 1, 0, 1, 2, 0, 2, 1, 0, 2, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1],
                       [1, 1, 0, 1, 2, 0, 2, 1, 0, 2, 2],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2],
                       [1, 1, 0, 1, 2, 0, 2, 1, 0, 2, 2]]
            
            while row < 11:
                  while cullum < 11:
                        size = ((x + row * 30), (y + cullum * 30), 30, 30)
                        
                        if preview[cullum][row] == 0:
                              color = (125, 125, 125)
                        elif preview[cullum][row] == 1:
                              color = (255, 255, 255)
                        elif preview[cullum][row] == 2:
                              color = (0, 0, 0)
                        pygame.draw.rect(screen, color, size)
                        cullum = cullum + 1
                  cullum = 0
                  row = row + 1
            row = 0

      def mapMakerTouch(self, change, tileNumber, mouse_x, mouse_y):
            if self.Touch(1150, 275, mouse_x, mouse_y):
                  tileNumber[0] = 1
                  change[0] = True
            elif self.Touch(1240, 275, mouse_x, mouse_y):
                  tileNumber[0] = 2
                  change[0] = True
            elif self.Touch(1330, 275, mouse_x, mouse_y):
                  tileNumber[0] = 3
                  change[0] = True
            elif self.Touch(1420, 275, mouse_x, mouse_y):
                  tileNumber[0] = 4
                  change[0] = True
            elif self.Touch(1150, 365, mouse_x, mouse_y):
                  tileNumber[0] = 5
                  change[0] = True
            elif self.Touch(1240, 365, mouse_x, mouse_y):
                  tileNumber[0] = 6
                  change[0] = True
            elif self.Touch(1330, 365, mouse_x, mouse_y):
                  tileNumber[0] = 7
                  change[0] = True
            elif self.Touch(1420, 365, mouse_x, mouse_y):
                  tileNumber[0] = 8
                  change[0] = True
            elif self.Touch(1150, 455, mouse_x, mouse_y):
                  tileNumber[0] = 9
                  change[0] = True
            elif self.Touch(1240, 455, mouse_x, mouse_y):
                  tileNumber[0] = 10
                  change[0] = True
            elif self.Touch(1330, 455, mouse_x, mouse_y):
                  tileNumber[0] = 11
                  change[0] = True
            elif self.Touch(1420, 455, mouse_x, mouse_y):
                  tileNumber[0] = 12
                  change[0] = True
            elif self.Touch(1150, 545, mouse_x, mouse_y):
                  tileNumber[0] = 13
                  change[0] = True
            elif self.Touch(1240, 545, mouse_x, mouse_y):
                  tileNumber[0] = 14
                  change[0] = True
            elif self.Touch(1330, 545, mouse_x, mouse_y):
                  tileNumber[0] = 15
                  change[0] = True
            elif self.Touch(1420, 545, mouse_x, mouse_y):
                  tileNumber[0] = 16
                  change[0] = True

#creates the feature on the land on the map
class Map():
      #adds land's optoions to the map
      def addLand(self, road, way):
            index = 0

            #add the vertical
            #while len(road[index]) + 1 > len(road):
            if way == 'y':
                  road.append([-1] * (len(road[0]) + 1))
                  road.append([-1] * (len(road[0]) + 1))

            #add the horizontal
            elif way == 'x':
                  while index < len(road):
                        road[index].append(-1)
                        index = index + 1
                  index = 0
                  while index < len(road):
                        road[index].append(-1)
                        index = index + 1

      def myWorld(self, road, dx, dy):
            x = 0
            y = 0
            size = (y , x, 50, 50)
            color = (0, 0, 0)
            index = 0
            outline = False

      
            while x < len(road[0]):
                  while y < len(road):
                        if road[y][x] == -1:
                              color = (255, 255, 255)
                        elif road[y][x] == 0:
                              color = (0, 0, 255)
                        elif road[y][x] == 1:
                              color = (0, 255, 0)
                        elif road[y][x] == 2:
                              color = (184, 134, 11)
                        elif road[y][x] == 3:
                              color = (255, 0, 0)
                              outline = True

                        #position of the map
                        size = (x * 50 + dx * 50, y * 50 + dy * 50, 50, 50)
                        if (outline):
                              pygame.draw.rect(screen, color, size)
                              outline = False
                        else: 
                              pygame.draw.rect(screen, color, size)
                        
                        y = y + 1
                  y = 0
                  x = x + 1

      def structure(self, world, indexX, indexY, posx, posy, tr, tl, br, bl):
            world[int(indexY - posy)][int(indexX - posx)] = tr
            world[int(indexY - posy) + 1][int(indexX - posx)] = br
            world[int(indexY - posy)][int(indexX - posx) + 1] = tl
            world[int(indexY - posy) + 1][int(indexX - posx) + 1] = bl

      def elementStructure(self, world, indexX, indexY, value):
            world[int(indexY)][int(indexX)] = value

      #restricts the top and left bounds of the wall
      def changable(self, world, indexX, indexY, posx, posy, tileNumber):
            nx = len(world)/2
            ny = len(world[0])/2
            
            #corner
            if (indexX == 0 or indexX == 1) and (indexY == 0 or indexY == 1):
                  if tileNumber in [2]:
                        self.structure(world, indexX, indexY, posx, posy, 1, 1, 1, 2)

            #must have the top wall
            elif indexX != 0 and (indexY == 0 or indexY == 1):
                  if tileNumber in [1, 2, 3, 4]:
                        if tileNumber == 1:
                              self.structure(world, indexX, indexY, posx, posy, 1, 1, 1, 1)
                        if tileNumber == 2:
                              self.structure(world, indexX, indexY, posx, posy, 1, 1, 1, 2)
                        if tileNumber == 3:
                              self.structure(world, indexX, indexY, posx, posy, 1, 1, 2, 1)
                        if tileNumber == 4:
                              self.structure(world, indexX, indexY, posx, posy, 1, 1, 2, 2)

            #must have the left wall
            elif (indexX == 0 or indexX == 1) and indexY != 0:
                  if tileNumber in [1, 2, 5, 6]:
                        if tileNumber == 1:
                              self.structure(world, indexX, indexY, posx, posy, 1, 1, 1, 1)
                        if tileNumber == 2:
                              self.structure(world, indexX, indexY, posx, posy, 1, 1, 1, 2)
                        if tileNumber == 5:
                              self.structure(world, indexX, indexY, posx, posy, 1, 2, 1, 1)
                        if tileNumber == 6:
                              self.structure(world, indexX, indexY, posx, posy, 1, 2, 1, 2)

            else: 
                  if tileNumber == 1:
                        self.structure(world, indexX, indexY, posx, posy, 1, 1, 1, 1)
                  if tileNumber == 2:
                        self.structure(world, indexX, indexY, posx, posy, 1, 1, 1, 2)
                  if tileNumber == 3:
                        self.structure(world, indexX, indexY, posx, posy, 1, 1, 2, 1)
                  if tileNumber == 4:
                        self.structure(world, indexX, indexY, posx, posy, 1, 1, 2, 2)
                  if tileNumber == 5:
                        self.structure(world, indexX, indexY, posx, posy, 1, 2, 1, 1)
                  if tileNumber == 6:
                        self.structure(world, indexX, indexY, posx, posy, 1, 2, 1, 2)
                  if tileNumber == 7:
                        self.structure(world, indexX, indexY, posx, posy, 1, 2, 2, 1)
                  if tileNumber == 8:
                        self.structure(world, indexX, indexY, posx, posy, 1, 2, 2, 2)
                  if tileNumber == 9:
                        self.structure(world, indexX, indexY, posx, posy, 2, 1, 1, 1)
                  if tileNumber == 10:
                        self.structure(world, indexX, indexY, posx, posy, 2, 1, 1, 2)
                  if tileNumber == 11:
                        self.structure(world, indexX, indexY, posx, posy, 2, 1, 2, 1)
                  if tileNumber == 12:
                        self.structure(world, indexX, indexY, posx, posy, 2, 1, 2, 2)
                  if tileNumber == 13:
                        self.structure(world, indexX, indexY, posx, posy, 2, 2, 1, 1)
                  if tileNumber == 14:
                        self.structure(world, indexX, indexY, posx, posy, 2, 2, 1, 2)
                  if tileNumber == 15:
                        self.structure(world, indexX, indexY, posx, posy, 2, 2, 2, 1)
                  if tileNumber == 16:
                        self.structure(world, indexX, indexY, posx, posy, 2, 2, 2, 2)

      #rstricts the movement of the ball when it is horizontal or vertically centered
      def wall(self, world, posX, posY):
            if (world[posY][posX] == 3):
                  return 2
            if (world[posY][posX] == 2):
                  return 1
            else:
                  return 0

class AccessMemory(object):
      def __init__(self):
            self.var = 0
            self.hor = 0
            self.ballPosX = 0
            self.ballPosY = 0
            self.test = ""
            
      def OpenGame(self, testWorld):
            getPlayer = open('player.txt', 'r')
            self.ver = int(getPlayer.readline())
            self.hor = int(getPlayer.readline())
            self.ballPosX = int(getPlayer.readline())
            self.ballPosY = int(getPlayer.readline())
            getPlayer.close()

            getMap = open('World/map.txt', 'r')
            for getLand in getMap.read():
                  if getLand != "," and getLand != "\n":
                        self.test = self.test + getLand
                  elif getLand != "\n":
                        testWorld[len(testWorld) - 1].append(int(self.test))
                        self.test = ""
                  if getLand == "\n":
                        testWorld.append([])

            testWorld.remove(testWorld[len(testWorld) - 1])
            
            getMap.close()

      def SaveGame(self, world, mapY, mapX, ballPosX, ballPosY):
            savePlayer = open('player.txt', 'w')
            savePlayer.write(str(mapY) + "\n")
            savePlayer.write(str(mapX) + "\n")
            savePlayer.write(str(ballPosX) + "\n")
            savePlayer.write(str(ballPosY) + "\n")
            savePlayer.close()
            
            saveMap = open('World/map.txt', 'w')
            save1 = 0
            save2 = 0
            while save1 < len(world):
                  while save2 < len(world[0]):
                        saveMap.write(str(world[save1][save2]) + ",")
                        save2 = save2 + 1
                  save2 = 0
                  saveMap.write("\n")
                  save1 = save1 + 1
            saveMap.close()


      def getVar(self):
            return self.ver

      def getHor(self):
            return self.hor

      def getballPosX(self):
            return self.ballPosX

      def getballPosY(self):
            return self.ballPosY

      def getTest(self):
            return self.test
            
def Main_Loop():
      #calls the initial functions
      ball = Ball(75, 75, 25, 0, 0) #cordx, cordy, radius, speedx, speedy
      control = Controls(110, 40)
      controlRoad = Controls(60, 60)

      option = Controls(300, 40)
      landChoice = 0;
      accessMemory = AccessMemory()
      
      #items that is used to create the map
      mapCreater = Controls(60,60)

      options = [0, 0]
      landOptions = [False, False, False]
      choice = len(options)
      
      world = [[1, 1, -1, -1],
               [1, 2, -1, -1],
               [-1, -1, -1, -1],
               [-1, -1, -1, -1]]

      #reopens the saved file
      testWorld = [[]]
      accessMemory.OpenGame(testWorld)
      ver = accessMemory.getVar()
      hor = accessMemory.getHor()
      ballPosX = accessMemory.getballPosX()
      ballPosY = accessMemory.getballPosY()
      test = accessMemory.getTest();
      
      defaultX = hor
      defaultY = ver
      
      world = testWorld
      
      gameMap = Map()
      text = pygame.font.SysFont("monospace", 75)
      
      labelClose = text.render("<-", 1, (255, 255, 255))
      labelOpen = text.render("->", 1, (255, 255, 255))

      change = False
      visible = False
      red = True
      green = False
      blue = False
      elementNumber = 0
      
      holdUp = False
      holdDown = False
      holdRight = False
      holdLeft = False

      locationX = 50 * (len(world[0]) - 1)
      locationY = 50 * (len(world) - 1)
      tileNumber = -1

      delay = 0

      i = 0
      while i < defaultY:
            ball.moveDown()
            i = i + 1
      i = 0
      while i < defaultX:
            ball.moveRight()
            i = i + 1
      i = 0

      mapX = hor
      mapY = ver
      #starts the loop of the game
      while True:
            screen.fill(BLACK)
            
            land = Controls(100, 50 * len(world))
            land2 = Controls(50 * len(world[0]), 100)
            
            
            for event in pygame.event.get():
                 

                  if event.type == KEYDOWN:
                        if event.key == K_0:
                              accessMemory.SaveGame(world, mapY, mapX, ballPosX, ballPosY)                              
                              pygame.quit()
                              sys.exit()

                        #moves the map up down left and right
                        if visible == False:
                              if event.key == K_UP:
                                    if (gameMap.wall(world, ballPosX, ballPosY - 1) == 2):
                                          if (gameMap.wall(world, ballPosX, ballPosY - 2) == 1):
                                                world[ballPosY - 1][ballPosX] = 2
                                                world[ballPosY - 2][ballPosX] = 3
                                                ballPosY = ballPosY - 1
                                                ver = ver + 1
                                                mapY = ver
                                                holdUp = True
                                                
                                    elif (gameMap.wall(world, ballPosX, ballPosY - 1) == 1):
                                          ballPosY = ballPosY - 1
                                          ver = ver + 1
                                          mapY = ver
                                          holdUp = True

                              elif event.key == K_DOWN:
                                    if (gameMap.wall(world, ballPosX, ballPosY + 1) == 2):
                                          if (gameMap.wall(world, ballPosX, ballPosY + 2) == 1):
                                                world[ballPosY + 1][ballPosX] = 2
                                                world[ballPosY + 2][ballPosX] = 3
                                                ballPosY = ballPosY + 1
                                                ver = ver - 1
                                                mapY = ver
                                                holdDown = True
                                                
                                    elif (gameMap.wall(world, ballPosX, ballPosY + 1) == 1):
                                          ballPosY = ballPosY + 1
                                          ver = ver - 1
                                          mapY = ver
                                          holdDown = True

                              elif event.key == K_RIGHT:
                                    if (gameMap.wall(world, ballPosX + 1, ballPosY) == 2):
                                          if (gameMap.wall(world, ballPosX + 2, ballPosY) == 1):
                                                world[ballPosY][ballPosX + 1] = 2
                                                world[ballPosY][ballPosX + 2] = 3
                                                ballPosX = ballPosX + 1
                                                hor = hor - 1
                                                mapX = hor
                                                holdRight = True
                                                
                                    elif (gameMap.wall(world, ballPosX + 1, ballPosY) == 1):
                                          ballPosX = ballPosX + 1
                                          hor = hor - 1
                                          mapX = hor
                                          holdRight = True

                              elif event.key ==K_LEFT:
                                    if (gameMap.wall(world, ballPosX - 1, ballPosY) == 2):
                                          if (gameMap.wall(world, ballPosX - 2, ballPosY) == 1):
                                                world[ballPosY][ballPosX - 1] = 2
                                                world[ballPosY][ballPosX - 2] = 3
                                                ballPosX = ballPosX - 1
                                                hor = hor + 1
                                                mapX = hor
                                                holdLeft = True
                                                
                                    elif (gameMap.wall(world, ballPosX - 1, ballPosY)  == 1):
                                          ballPosX = ballPosX - 1
                                          hor = hor + 1
                                          mapX = hor
                                          holdLeft = True

                  if event.type == KEYUP and visible == False:
                        if event.key == K_UP:
                              delay = 0
                              holdUp = False

                        if event.key == K_DOWN:
                              delay = 0
                              holdDown = False

                        if event.key == K_RIGHT:
                              delay = 0
                              holdRight = False

                        if event.key == K_LEFT:
                              delay = 0
                              holdLeft = False

                  elif event.type == KEYUP and visible == True:
                        if event.key == K_UP:
                              delay = 0
                              holdUp = False
                              ball.moveUp()
                              ver = ver - 1

                        if event.key == K_DOWN:
                              delay = 0
                              holdDown = False
                              ball.moveDown()
                              ver = ver + 1

                        if event.key == K_RIGHT:
                              delay = 0
                              holdRight = False
                              ball.moveRight()
                              hor = hor + 1

                        if event.key == K_LEFT:
                              delay = 0
                              holdLeft = False
                              ball.moveLeft()
                              hor = hor - 1
                        

                  #open or closes the control panel
                  if event.type == MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = event.pos


                        #closes the panel
                        if visible == True and mouse_x > 990 and mouse_x < 1100 and mouse_y < 75:
                              hor = mapX
                              ver = mapY
                              visible = False

                        #opens the panel
                        elif visible == False and mouse_x > 1490 and mouse_y < 75:
                              visible = True

                        #changes the color of the ball to red
                        if visible == True:
                              red = False
                              blue = False
                              green = False
                              #change the color of the ball to red
                              if control.Touch(1150, 100, mouse_x, mouse_y):
                                    red = True

                              #chage the color of the ball to blue
                              if control.Touch(1290, 100, mouse_x, mouse_y):
                                    blue = True

                              #change the color of the ball to green
                              if control.Touch(1430, 100, mouse_x, mouse_y):
                                    green = True

                              #adds land based on the location where the map is and where the user touch the screen
                              x_axis = land.Touch((len(world[0])) * 50 - 100 + (50 * hor), len(world) + 50 * ver, mouse_x, mouse_y)
                              y_axis = land2.Touch((len(world[0])) + 50 * hor, (len(world)) * 50 - 100 + 50 * ver, mouse_x, mouse_y)
                              
                              if x_axis and mouse_x < 1100 and change and options[0] == 1:
                                    gameMap.addLand(world, 'x')
                                    locationX += 100
                              if y_axis and mouse_x < 1100 and change and options[0] == 1:
                                    gameMap.addLand(world, 'y')
                                    locationY += 100

                              #option list for the user to chose from
                              base = option.Touch(1150, 200, mouse_x, mouse_y)
                              if (base):
                                    if (1 not in options):
                                          options[0] = 1
                                          choice = 0
                                    else:
                                          options[choice] = 0

                              if (option.Touch(1150, 275, mouse_x, mouse_y)):
                                    if (1 not in options):
                                          options[1] = 1
                                          choice = 1       
                                        
                                          
                              #change the tile on the grid
                              if mouse_x < (locationX + 50 * hor) and mouse_y < (locationY + 50 * ver):
                                    posx = math.floor((mouse_x - (50 * hor)) / 50) % 2
                                    posy = math.floor((mouse_y - (50 * ver)) / 50) % 2
                                    sectionX = math.ceil((mouse_x - (50 * hor))/ 50)
                                    sectionY = math.ceil((mouse_y - (50 * ver))/ 50)
                                    
                                    #changes the tiles based on the category that he user has chosen
                                    if change and sectionX >= 0 and sectionY >= 0 and mouse_x < 1100:
                                          if options[1] == 1 and landOptions[elementNumber] and world[int(sectionY)][int(sectionX)] != -1:
                                                if (landOptions[0]):
                                                      gameMap.elementStructure(world, sectionX, sectionY, 3)
                                                      landOptions[0] = False
                                                      change = False
                                                elif (landOptions[1]):
                                                      gameMap.elementStructure(world, sectionX, sectionY, 1)
                                                      landOptions[1] = False
                                                      change = False
                                                elif (landOptions[2]):
                                                      gameMap.elementStructure(world, sectionX, sectionY, 2)
                                                      landOptions[2] = False
                                                      change = False
                                          elif options[0] == 1:
                                                gameMap.changable(world, sectionX, sectionY, posx, posy, tileNumber)
                                                change = False
                                    
                              else:
                                    sectionX = 0
                                    sectionY = 0
                            
            
            #the menu is open and it frezzes the game
            if visible == True:
                  #the game is frozen
                  gameMap.myWorld(world, hor, ver)
                  ball.drawBall()
                  ball.stationaryBall()

                  #the menu
                  color = (125, 125, 125)
                  size = (1100, 0, 500, 900)
                  pygame.draw.rect(screen, color, size)

                  if (red == True):
                        ball.changeColor(255, 0, 0)
                  elif (green == True):
                        ball.changeColor(0, 255, 0)
                  elif (blue == True):
                        ball.changeColor(0, 0, 255)

                  control.ButtonText(1150, 100, "red")
                  control.ButtonText(1290, 100, "blue")
                  control.ButtonText(1430, 100, "green")
                  

                  if (options[0] == 1):
                        option.ButtonText(1150, 200, "add land")
                        control.mapMaker(1150, 275)
                        test = [change]
                        num = [tileNumber]
                        mapCreater.mapMakerTouch(test, num, mouse_x, mouse_y)
                        change = test[0]
                        tileNumber = num[0]
                  elif (options[1] == 1):
                        option.ButtonText(1150, 200, "items")

                        if (controlRoad.Touch(1150, 275, mouse_x, mouse_y)):
                              landOptions[elementNumber] = False
                              landOptions[0] = True
                              elementNumber = 0;
                              change = True

                        if (controlRoad.Touch(1240, 275, mouse_x, mouse_y)):
                              landOptions[elementNumber] = False
                              landOptions[1] = True
                              elementNumber = 1
                              change = True

                        if (controlRoad.Touch(1330, 275, mouse_x, mouse_y)):
                              landOptions[elementNumber] = False
                              landOptions[2] = True
                              elementNumber = 2
                              change = True
                              
                        option.Button(1150, 275, 60, 60, 255, 0, 0)
                        option.Button(1240, 275, 60, 60, 0, 255, 0)
                        option.Button(1330, 275, 60, 60, 184, 134, 11)
                  else:
                        option.ButtonText(1150, 200, "add land")
                        option.ButtonText(1150, 275, "items")

                  screen.blit(labelOpen, (1000, 0))

            
            #the menu is closed and nonInterctive
            elif visible == False:
                  ball.default()
                  screen.blit(labelClose, (1500, 0))
                  gameMap.myWorld(world, hor, ver)
                  change = False
                  if holdUp == True or holdDown == True or holdRight == True or holdLeft == True:
                        delay = delay + 1

                  if holdUp == True:
                        if (gameMap.wall(world, ballPosX, ballPosY - 1) == 2):
                              if (gameMap.wall(world, ballPosX, ballPosY - 2) == 1):
                                    if delay % 75 == 0:
                                          world[ballPosY - 1][ballPosX] = 2
                                          world[ballPosY - 2][ballPosX] = 3
                                          ballPosY = ballPosY - 1
                                          ver = ver + 1
                                          mapY = ver
                        
                        elif (gameMap.wall(world, ballPosX, ballPosY - 1) == 1): 
                              if delay % 75 == 0:
                                    ballPosY = ballPosY - 1
                                    ver = ver + 1
                                    mapY = ver
                                    
                  elif holdDown == True:
                        if (gameMap.wall(world, ballPosX, ballPosY + 1) == 2):
                              if (gameMap.wall(world, ballPosX, ballPosY + 2) == 1):
                                    if delay % 75 == 0:
                                          world[ballPosY + 1][ballPosX] = 2
                                          world[ballPosY + 2][ballPosX] = 3
                                          ballPosY = ballPosY + 1
                                          ver = ver - 1
                                          mapY = ver
                                    
                        elif (gameMap.wall(world, ballPosX, ballPosY + 1) == 1):
                              if delay % 75 == 0:
                                    ballPosY = ballPosY + 1
                                    ver = ver - 1
                                    mapY = ver

                  elif holdRight == True:
                        if (gameMap.wall(world, ballPosX + 1, ballPosY) == 2):
                              if (gameMap.wall(world, ballPosX + 2, ballPosY) == 1):
                                    if delay % 75 == 0:
                                          world[ballPosY][ballPosX + 1] = 2
                                          world[ballPosY][ballPosX + 2] = 3
                                          ballPosX = ballPosX + 1
                                          hor = hor - 1
                                          mapX = hor
                                    
                        elif (gameMap.wall(world, ballPosX + 1, ballPosY) == 1):
                              if delay % 75 == 0:
                                    ballPosX = ballPosX + 1
                                    hor = hor - 1
                                    mapX = hor

                  elif holdLeft == True:
                        if (gameMap.wall(world, ballPosX - 1, ballPosY) == 2):
                              if (gameMap.wall(world, ballPosX - 2, ballPosY) == 1):
                                    if delay % 75 == 0:
                                          world[ballPosY][ballPosX - 1] = 2
                                          world[ballPosY][ballPosX - 2] = 3
                                          ballPosX = ballPosX - 1
                                          hor = hor + 1
                                          mapX = hor
                        
                        elif (gameMap.wall(world, ballPosX - 1, ballPosY)):
                              if delay % 75 == 0:
                                    ballPosX = ballPosX - 1
                                    hor = hor + 1
                                    mapX = hor
                                    
                  ball.drawBall()
                  ball.moveBall()
                  
            pygame.display.update()

Main_Loop()
