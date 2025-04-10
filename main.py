import pygame
from snake import Snake

"""CONSTANTS"""
WIDTH = 900
HEIGHT = 600
cellSize = 20
startPos = (5,5)

def drawGrid():
    
    for x in range(0, WIDTH, cellSize):
        for y in range(0, HEIGHT, cellSize):
            cell = pygame.Rect(x,y,cellSize,cellSize)
            pygame.draw.rect(screen,"white",cell,1)

    
pygame.init()
pygame.display.set_caption("Snake")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)


snake = Snake(cellSize,startPos)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    
    keys = pygame.key.get_pressed()
    snakePos = font.render(f"pos: {snake.headPosX,snake.headPosY}",True,"cyan")
    
    screen.fill("black")
    drawGrid()
    screen.blit(snakePos,(40,40))
    
    snake.draw(screen)
    snake.move(keys,pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT)

    pygame.display.update()
    clock.tick(60)