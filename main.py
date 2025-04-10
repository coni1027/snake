import pygame
from snake import Snake
from fruit import Fruit

"""CONSTANTS"""
WIDTH = 900
HEIGHT = 600
cellSize = 50
startPos = (5,5)
tail1 = (4,5)
tail2 = (3,5)
moveDelay = 80 # in ms

def drawGrid():
    for x in range(0, WIDTH, cellSize):
        for y in range(0, HEIGHT, cellSize):
            cell = pygame.Rect(x,y,cellSize,cellSize)
            pygame.draw.rect(screen,"white",cell,1)

def drawHUD():
    snakePos = font.render(f"snake pos: {snake.headPosX,snake.headPosY}",True,"cyan")
    fruitPos = font.render(f"fruit pos: {fruit.posX, fruit.posY}",True,"cyan")
    snakeLength = font.render(f"length: {snake.length}",True,"cyan")
    screen.blit(snakePos,(40,40))
    screen.blit(fruitPos,(40,60))
    screen.blit(snakeLength,(40,80))
    
pygame.init()
pygame.display.set_caption("Snake")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)


snake = Snake(cellSize,startPos,WIDTH,HEIGHT,[startPos,startPos])
fruit = Fruit(cellSize,(9,9),WIDTH,HEIGHT)

lastMoveTime = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            snake.directionChange(event.key, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    
    screen.fill("black")
    drawHUD()
    # drawGrid()
    
    snake.draw(screen)
    fruit.draw(screen)

    if not fruit.spawned:
        fruit.spawn(screen)

    now = pygame.time.get_ticks()
    if now - lastMoveTime > moveDelay:
        snake.update()
        lastMoveTime = now

    if snake.headRect.colliderect(fruit.rect):
        print('snake collide w fruit')
        fruit.reset(screen)
        snake.grow()


    pygame.display.update()
    clock.tick(60)