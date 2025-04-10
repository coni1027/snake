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

    def move(self,keylist:list,upkey,downkey,leftkey,rightkey):
        if keylist[upkey]:
            self.headPosY -= 1
        if keylist[downkey]:
            self.headPosY += 1
        if keylist[leftkey]:
            self.headPosX -= 1
        if keylist[rightkey]:
            self.headPosX += 1

        self.headRect.topleft = (self.headPosX*self.size, self.headPosY*self.size)
    
    def draw(self,screen):
        pygame.draw.rect(screen, "green", self.headRect)
        for segment in self.segments:
            x,y = segment
            segmentRect = pygame.Rect(x*self.size,y*self.size,
                                      self.size,self.size)
            pygame.draw.rect(screen,"green",segmentRect,)