import pygame
from pygame.locals import *
import random
from point import Point
from snake import Snake


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("贪吃蛇游戏")
clock = pygame.time.Clock()
# 游戏循环标志变量
keep_going = True
# 颜色
bg_color = (0, 0, 0)
body_color = (70, 161, 98) #蛇身体颜色
head_color = (46, 99, 255)  # 蛇头颜色w
food_color = (255, 0, 0)
grid_color = (255, 255, 255)
# 定义格子的行列
ROW = 30
COL = 40
# 游戏地图边长
side = 24
# 地图坐标
x1,x2,y1,y2 = 8, 32, 5, 29

# 网格的宽度和高度
cell_width = width / COL
cell_height = height / ROW
# 控制和移动
speed = 1
direct = 'left'

# 得分
score = 0
# 显示文字
font = pygame.font.SysFont("simhei", 24)

game_over = False

snake = Snake(ROW, COL)
snake.Snake(speed, direct, score)
# 生成食物
def create_food():
    while True:
        pos = Point(row=random.randint(y1,y2 - 1), col=random.randint(x1,x2 - 1))
        # 是否撞到标志布尔值
        is_coll = False
        # 是否跟蛇碰上了
        if snake.head.row == pos.row and snake.head.col == pos.col:
            is_coll = True
        # 蛇的身子是否碰到食物
        for s in snake.snakes:
            if s.row == pos.row and s.col == pos.col:
                is_coll = True
                break

        if not is_coll:
            break
    return pos
food = create_food()
# 绘制网格
def draw_grid():
    # 绘制行
    for r in range(y1, y2 + 1 ):
        pygame.draw.line(screen, grid_color, (x1 * cell_height, r * cell_height),
                         (x2 * cell_height, r * cell_height))
    # 绘制列
    for c in range(x1, x2 + 1 ):
        pygame.draw.line(screen, grid_color, (c * cell_width, y1 * cell_height),
                         (c * cell_width, y2 * cell_height))
# 绘制点
def draw_rect(point, color):
    left = point.col * cell_width
    top = point.row * cell_height
    # 绘制
    pygame.draw.rect(screen, color, (left, top, cell_width, cell_height))

while keep_going:

    # 键盘控制
    for event in pygame.event.get():
        if event.type == QUIT:
            keep_going = False
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
        food = create_food()

    #创到身体就寄
    if snake.is_crush_body():
        keep_going = False
        break
    #创到边缘也寄
    if snake.head.row < y1 or snake.head.row > y2 or snake.head.col < x1 or snake.head.col == x2:
        keep_going = False
        break

    # 背景色填充
    screen.fill(bg_color)

    # # 显示得分
    # l_snakes = len(snake.snakes)

    # score_text = "蛇的长度：" + str(l_snakes) + " 得分："a + str(point)
    # score = font.render(score_text, True, (0, 0, 0))
    # score_rect = score.get_rect()
    # score_rect.centerx = screen.get_rect().centerx
    # score_rect.y = 10
    # screen.blit(score, score_rect)

    # 绘制蛇头
    draw_rect(snake.head, head_color)
    # 绘制蛇的身体
    for s in snake.snakes:
        draw_rect(s, body_color)
    # 绘制食物
    draw_rect(food, food_color)
    # 绘制网格
    draw_grid()


    pygame.display.flip()  # 刷新屏幕
    # 帧速率
    clock.tick(10)

pygame.quit()