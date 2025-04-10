import pygame


class Snake():
    def __init__(self,cellSize,headPos:tuple,segments=None):
        self.cellSize = cellSize
        self.headPosX, self.headPosY = headPos
        self.headRect = pygame.Rect(self.headPosX*self.cellSize,
                                    self.headPosY*self.cellSize,
                                    self.cellSize,self.cellSize)
        if segments == None:
            segments = []
        self.segments = segments
        self.direction = (1,0)
        self.length = len(self.segments)+1

    def update(self):
        self.segments.insert(0, (self.headPosX, self.headPosY))

        dx, dy = self.direction
        self.headPosX += dx
        self.headPosY += dy
        self.headRect.topleft = (self.headPosX * self.cellSize, self.headPosY * self.cellSize)

        if len(self.segments) > self.length-1:
            self.segments.pop()


    def directionChange(self,key,upkey,downkey,leftkey,rightkey):
        currentDirection = self.direction

        if key == upkey and currentDirection != (0, 1):
            self.direction = (0, -1)
        elif key == downkey and currentDirection != (0, -1):
            self.direction = (0, 1)
        elif key == leftkey and currentDirection != (1, 0):
            self.direction = (-1, 0)
        elif key == rightkey and currentDirection != (-1, 0):
            self.direction = (1, 0)

    def draw(self,screen):
        pygame.draw.rect(screen, "green", self.headRect)
        for segment in self.segments:
            x,y = segment
            segmentRect = pygame.Rect(x*self.cellSize,y*self.cellSize,
                                      self.cellSize,self.cellSize)
            pygame.draw.rect(screen,"green",segmentRect,)