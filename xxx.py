import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义游戏区域大小和方格大小
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
GRID_SIZE = 30

# 创建游戏窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 定义蛇的初始位置和长度
snake_head = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
snake_body = [[snake_head[0], snake_head[1] + i * GRID_SIZE] for i in range(3)]
snake_direction = 'up'

# 定义食物的初始位置
food_position = [random.randint(0, SCREEN_WIDTH / GRID_SIZE - 1) * GRID_SIZE,
                 random.randint(0, SCREEN_HEIGHT / GRID_SIZE - 1) * GRID_SIZE]

# 定义游戏循环标志和帧率
running = True
clock = pygame.time.Clock()
FPS = 10

# 游戏循环
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN and snake_direction != 'up':
                snake_direction = 'down'
            elif event.key == pygame.K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'

    # 移动蛇头
    if snake_direction == 'up':
        snake_head[1] -= GRID_SIZE
    elif snake_direction == 'down':
        snake_head[1] += GRID_SIZE
    elif snake_direction == 'left':
        snake_head[0] -= GRID_SIZE
    elif snake_direction == 'right':
        snake_head[0] += GRID_SIZE

    # 判断是否吃到食物
    if snake_head == food_position:
        food_position = [random.randint(0, SCREEN_WIDTH / GRID_SIZE - 1) * GRID_SIZE,
                         random.randint(0, SCREEN_HEIGHT / GRID_SIZE - 1) * GRID_SIZE]
    else:
        snake_body.pop()

    # 判断是否撞到墙或自身
    if snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT:
        running = False
    for body_part in snake_body:
        if snake_head == body_part:
            running = False

    # 添加蛇头和食物到身体列表中
    snake_body.insert(0, list(snake_head))

    # 绘制游戏界面
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [food_position[0], food_position[1], GRID_SIZE, GRID_SIZE])
    for body_part in snake_body:
        pygame.draw.rect(screen, BLACK, [body_part[0], body_part[1], GRID_SIZE, GRID_SIZE])
    pygame.display.update()

    # 控制帧率
    clock.tick(FPS)

# 退出 Pygame
pygame.quit()
