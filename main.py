import pygame
from pygame.locals import *
from snake import Snake
from snakeGame import RetroSnaker

if __name__ == '__main__':
    bg_color = (0, 0, 0)
    body_color = (70, 161, 98)  # 蛇身体颜色
    head_color = (46, 99, 255)  # 蛇头颜色
    food_color = (255, 0, 0)
    grid_color = (255, 255, 255)
    # 定义格子的行列
    ROW = 30
    COL = 40
    # 游戏地图边长
    side = 24
    # 游戏循环标志变量
    game_state = True
    SnakeGame = RetroSnaker(800, 600)
    SnakeGame.initColor(bg_color, body_color, head_color, food_color, grid_color)  # 初始化游戏配色
    SnakeGame.initMap(ROW, COL, side)  # 初始化游戏地图大小
    snake = Snake(SnakeGame.ROW, SnakeGame.COL)  # 新建蛇实例
    snake.initSnake(SnakeGame.speed, SnakeGame.direct, SnakeGame.score)  # 初始化蛇参数
    # 生成食物
    food = SnakeGame.create_food(snake)
    while game_state:
        # 键盘控制
        for event in pygame.event.get():
            if event.type == QUIT:
                game_state = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    snake.LEFT()
                    break
                elif event.key == K_RIGHT or event.key == K_d:
                    snake.RIGHT()
                    break
                elif event.key == K_UP or event.key == K_w:
                    snake.UP()
                    break
                elif event.key == K_DOWN or event.key == K_s:
                    snake.DOWN()
                    break
        # 移动
        snake.move(food)
        # 如果吃到食物，就生成新食物
        if snake.is_crush_food:
            food = SnakeGame.create_food(snake)
        # 创到身体就寄
        if snake.is_crush_body():
            game_state = False
            break
        # 创到边缘也寄
        if snake.head.row < 0 or snake.head.row > 23 or snake.head.col < 0 or snake.head.col > 23:
            game_state = False
            break
        # 刷新屏幕
        SnakeGame.refreshScreen(food, snake)
        pygame.display.flip()
        # 帧速率
        SnakeGame.clock.tick(10)
    pygame.quit()