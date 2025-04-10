import pygame
import random


class Fruit():
    def __init__(self,cellSize:int,startPos:tuple):
        self.cellSize = cellSize
        self.posX,self.posY = startPos
        self.rect = pygame.Rect(self.posX*self.cellSize,
                                self.posY*self.cellSize,
                                cellSize,cellSize)
        self.spawned = False
    
    #update this to be random
    def spawn(self,screen:pygame.surface.Surface,screenWidth:int,screenHeight):
        self.posX = random.randint(0,(screenWidth // self.cellSize)-1)
        self.posY = random.randint(0,(screenHeight // self.cellSize)-1)
        self.rect.topleft = (self.posX*self.cellSize, self.posY*self.cellSize)

        pygame.draw.rect(screen,"red",self.rect)
        self.spawned = True

    def draw(self,screen):
        pygame.draw.rect(screen,"red",self.rect)

    def reset(self,screen):
        pygame.draw.rect(screen,"black",self.rect)
        self.spawned = False