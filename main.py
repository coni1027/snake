import pygame
from snake import Snake

"""CONSTANTS"""
WIDTH = 900
HEIGHT = 600
cellSize = 30
startPos = (5,5)
tail1 = (4,5)
tail2 = (3,5)
moveDelay = 50 # in ms

def drawGrid():
    for x in range(0, WIDTH, cellSize):
        for y in range(0, HEIGHT, cellSize):
            cell = pygame.Rect(x,y,cellSize,cellSize)
            pygame.draw.rect(screen,"white",cell,1)

def drawHUD():
    snakePos = font.render(f"pos: {snake.headPosX,snake.headPosY}",True,"cyan")
    snakeLength = font.render(f"length: {snake.length}",True,"cyan")
    screen.blit(snakePos,(40,40))
    screen.blit(snakeLength,(40,60))
    
pygame.init()
pygame.display.set_caption("Snake")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)


snake = Snake(cellSize,startPos,[tail1,tail2])

lastMoveTime = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    
    keys = pygame.key.get_pressed()
    
    
    screen.fill("black")
    drawGrid()
    drawHUD()
    
    snake.draw(screen)
    now = pygame.time.get_ticks()
    if now - lastMoveTime > moveDelay:
        snake.update()
        lastMoveTime = now
    snake.directionChange(keys,pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT)

    pygame.display.update()
    clock.tick(60)