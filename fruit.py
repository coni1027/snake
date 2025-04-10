import pygame
import random


class Fruit():
    def __init__(self,cellSize:int,startPos:tuple,screenWidth:int,screenHeight:int):
        self.cellSize = cellSize
        self.posX,self.posY = startPos
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.rect = pygame.Rect(self.posX*self.cellSize,
                                self.posY*self.cellSize,
                                cellSize,cellSize)
        self.spawned = False
    
    def spawn(self,screen:pygame.surface.Surface,snakeSegments:list,snakeHead:tuple):
        while True:    
            self.posX = random.randint(0,(self.screenWidth // self.cellSize)-1)
            self.posY = random.randint(0,(self.screenHeight // self.cellSize)-1)
            fruitPos = (self.posX, self.posY)

            if fruitPos not in snakeSegments and fruitPos != snakeHead:
                break
        
        self.rect.topleft = (self.posX*self.cellSize, self.posY*self.cellSize)
        pygame.draw.rect(screen,"red",self.rect)
        self.spawned = True

    def draw(self,screen):
        pygame.draw.rect(screen,"red",self.rect)

    def reset(self,screen):
        pygame.draw.rect(screen,"black",self.rect)
        self.spawned = False