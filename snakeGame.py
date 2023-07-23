import random
from point import Point
import pygame

class RetroSnaker:
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.clock = pygame.time.Clock()
        # 控制和移动
        self.speed = 1
        self.direct = 'left'

        # 得分
        self.score = 0
        pygame.init()
        pygame.display.set_caption("贪吃蛇")
        self.screen = pygame.display.set_mode(self.size)

    def initColor(self, bg_color, body_color, head_color, food_color, grid_color):
        # 颜色
        self.bg_color = bg_color
        self.body_color = body_color  # 蛇身体颜色
        self.head_color = head_color  # 蛇头颜色
        self.food_color = food_color
        self.grid_color = grid_color
        # 背景色填充
        self.screen.fill(self.bg_color)
    def refreshScreen(self, food, snake):
        # 背景色填充
        self.screen.fill(self.bg_color)
        # 绘制蛇头
        self.draw_rect(snake.head, self.head_color)
        # 绘制蛇的身体
        for s in snake.snakes:
            self.draw_rect(s, self.body_color)
        # 绘制食物
        self.draw_rect(food, self.food_color)
        # 绘制网格
        self.draw_grid()

    def initMap(self, ROW, COL, side):
        # 定义格子的行列
        self.ROW = ROW
        self.COL = COL
        # 游戏地图边长
        self.side = side
        # 地图坐标
        self.x1, self.x2 = int((self.COL - self.side) / 2), int((self.COL + self.side) / 2)
        self.y1, self.y2 = int((self.ROW - self.side) / 2), int((self.ROW + self.side) / 2)  # 5,29
        # 网格的宽度和高度
        self.cell_width = self.width / self.COL
        self.cell_height = self.height / self.ROW
    def create_food(self, snake):
        while True:
            self.snake = snake
            pos = Point(row=random.randint(0,23), col=random.randint(0,23))
            # 是否撞到标志布尔值
            is_coll = False
            # 是否跟蛇碰上了
            if self.snake.head.row == pos.row and self.snake.head.col == pos.col:
                is_coll = True
            # 蛇的身子是否碰到食物
            for s in self.snake.snakes:
                if s.row == pos.row and s.col == pos.col:
                    is_coll = True
                    break

            if not is_coll:
                break
        return pos
    # 绘制网格
    def draw_grid(self):
        # 绘制行
        for r in range(self.y1, self.y2 + 1 ):
            pygame.draw.line(self.screen, self.grid_color, (self.x1 * self.cell_height, r * self.cell_height),
                             (self.x2 * self.cell_height, r * self.cell_height))
        # 绘制列
        for c in range(self.x1, self.x2 + 1 ):
            pygame.draw.line(self.screen, self.grid_color, (c * self.cell_width, self.y1 * self.cell_height),
                             (c * self.cell_width, self.y2 * self.cell_height))
    # 绘制点
    def draw_rect(self, point, color):
        row = point.row + self.y1
        col = point.col + self.x1
        left = col * self.cell_width
        top = row * self.cell_height
        # 绘制
        pygame.draw.rect(self.screen, color, (left, top, self.cell_width, self.cell_height))
