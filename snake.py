import pygame

class Snake():
    def __init__(self,size,headPos:tuple,segments=None):
        self.size = size
        self.headPosX, self.headPosY = headPos
        self.headRect = pygame.Rect(self.headPosX*self.size,
                                    self.headPosY*self.size,
                                    self.size,self.size)
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
        self.headRect.topleft = (self.headPosX * self.size, self.headPosY * self.size)

        # Keep the tail length same as size
        if len(self.segments) > self.length-1:
            self.segments.pop()


    def directionChange(self,keylist:list,upkey,downkey,leftkey,rightkey):
        currentDirection = self.direction

        if keylist[upkey] and currentDirection != (0,1):
            self.direction = (0,-1)
        elif keylist[downkey] and currentDirection != (0,-1):
            self.direction = (0,1)
        elif keylist[leftkey] and currentDirection != (1,0):
            self.direction = (-1,0)
        elif keylist[rightkey] and currentDirection != (-1,0):
            self.direction = (1,0)

    def draw(self,screen):
        pygame.draw.rect(screen, "green", self.headRect)
        for segment in self.segments:
            x,y = segment
            segmentRect = pygame.Rect(x*self.size,y*self.size,
                                      self.size,self.size)
            pygame.draw.rect(screen,"green",segmentRect,)