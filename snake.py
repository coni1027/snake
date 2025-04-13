import pygame


class Snake():
    def __init__(self,cellSize,headPos:tuple,screenWidth:int,screenHeight:int):
        self.cellSize = cellSize
        self.headPosX, self.headPosY = headPos
        self.headRect = pygame.Rect(self.headPosX*self.cellSize,
                                    self.headPosY*self.cellSize,
                                    self.cellSize,self.cellSize)
        self.segments = [(self.headPosX,self.headPosY),(self.headPosX,self.headPosY)]
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.direction = (0,0)
        self.nextDirection = (0,0)
        self.length = len(self.segments)+1
        self.isLost = False

    def lost(self):
        self.isLost = True

    def update(self):
        self.direction = self.nextDirection
        self.segments.insert(0, (self.headPosX, self.headPosY))

        dx, dy = self.direction        
        self.headPosX += dx
        self.headPosY += dy
        self.headRect.topleft = (self.headPosX * self.cellSize, self.headPosY * self.cellSize)

        if self.headPosX > (self.screenWidth // self.cellSize)-1:
            self.headPosX = 0
        if self.headPosX < 0:
            self.headPosX = (self.screenWidth // self.cellSize)-1
        if self.headPosY > (self.screenHeight // self.cellSize)-1:
            self.headPosY = 0
        if self.headPosY < 0:
            self.headPosY = (self.screenHeight // self.cellSize)-1

        if len(self.segments) > self.length-1:
            self.segments.pop()

        if (self.headPosX, self.headPosY) in self.segments and self.direction != (0,0):
            self.lost()


    def directionChange(self,key,upkey,downkey,leftkey,rightkey):
        currentDirection = self.direction

        if key == upkey and currentDirection != (0, 1):
            self.nextDirection = (0, -1)
        elif key == downkey and currentDirection != (0, -1):
            self.nextDirection = (0, 1)
        elif key == leftkey and currentDirection != (1, 0):
            self.nextDirection = (-1, 0)
        elif key == rightkey and currentDirection != (-1, 0):
            self.nextDirection = (1, 0)

    def draw(self,screen):
        pygame.draw.rect(screen, "mediumseagreen", self.headRect)
        for segment in self.segments:
            x,y = segment
            segmentRect = pygame.Rect(x*self.cellSize,y*self.cellSize,
                                      self.cellSize,self.cellSize)
            pygame.draw.rect(screen,"lawngreen",segmentRect,)

    def grow(self):
        self.length += 1