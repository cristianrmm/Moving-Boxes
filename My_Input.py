import pygame
from pygame.locals import *

class textInput():
      def __init__(self, screen):
            self.text = ""
            self.screen = screen
            self.color = (255, 255, 255)
            self.size = (20, 650, 1000, 235)
            self.info = pygame.font.SysFont("monospace", 50)

      def blitText(self, text, span):
            new_text = False
            x = 0
            y = 0
            n = 0
            poped = False
            maximum = 100
            line = ""
            lineCount = 0
            paragraph = self.text.split(' ')
            pygame.draw.rect(self.screen, self.color, self.size)
            wordLength = 0

            for word in paragraph:
                  line = line + word + " "
                  lineLength = self.info.render(line, 1, (200, 0, 0))
                  statement = self.info.render(word + " ", 1, (200, 0, 0))
                  
                  if (lineLength.get_width() < span and n < maximum):
                        
                        self.screen.blit(statement, (20 + x, 650 + y))
                        x = x + statement.get_width()
                       
                  
                  elif (n < maximum):
                        x = 0
                        y = y + statement.get_height()
                        lineCount += 1

                        if (lineCount % 3 == 0):
                              n += 1
                              new_text = True
                        else:
                              self.screen.blit(statement, (20 + x, 650 + y))

                        if (word == paragraph[0] and word.count(word) == 1):
                              y = y - statement.get_height()
                              lineCount -= 1
                        
                        line = word + " "
                        
                        x = x + statement.get_width()

                  if (new_text and n < maximum):
                        new_text = False
                        y = 0
                        x = 0
                        pygame.draw.rect(self.screen, self.color, self.size)
                        self.screen.blit(statement, (20 + x, 650 + y))
                        x = x + statement.get_width()

                  
                                          
                        

            statement = self.info.render(line, 1, (200, 0, 0))
            return statement.get_width()
                  
            

      def Input(self, event, word):
            self.text = word
            lineCount = 1
            wordWidth = 0
            wordHight = 0
            words = []

            wordWidth = self.blitText(self.text, 975)

            if (wordWidth < 975):
                  if event == K_a:
                        self.text = self.text + "a"
                  elif event == K_b:
                        self.text = self.text + "b"
                  elif event == K_c:
                        self.text = self.text + "c"
                  elif event == K_d:
                        self.text = self.text + "d"
                  elif event == K_e:
                        self.text = self.text + "e"
                  elif event == K_f:
                        self.text = self.text + "f"
                  elif event == K_g:
                        self.text = self.text + "g"
                  elif event == K_h:
                        self.text = self.text + "h"
                  elif event == K_i:
                        self.text = self.text + "i"
                  elif event == K_j:
                        self.text = self.text + "j"
                  elif event == K_k:
                        self.text = self.text + "k"
                  elif event == K_l:
                        self.text = self.text + "l"
                  elif event == K_m:
                        self.text = self.text + "m"
                  elif event == K_n:
                        self.text = self.text + "n"
                  elif event == K_o:
                        self.text = self.text + "o"
                  elif event == K_p:
                        self.text = self.text + "p"
                  elif event == K_q:
                        self.text = self.text + "q"
                  elif event == K_r:
                        self.text = self.text + "r"
                  elif event == K_s:
                        self.text = self.text + "s"
                  elif event == K_t:
                        self.text = self.text + "t"
                  elif event == K_u:
                        self.text = self.text + "u"
                  elif event == K_v:
                        self.text = self.text + "v"
                  elif event == K_w:
                        self.text = self.text + "w"
                  elif event == K_x:
                        self.text = self.text + "x"
                  elif event == K_y:
                        self.text = self.text + "y"
                  elif event == K_z:
                        self.text = self.text + "z"
                  elif event == K_PERIOD:
                        self.text = self.text + "."

            if event == K_SPACE:
                        self.text = self.text + " "
            elif event == K_BACKSPACE:
                  self.text = self.text[:-1]
                        
                  
            return self.text
