import random
from snake import Point
import pygame
from pygame.locals import *

Direction = {
    'up': 0,
    'left': 1,
    'down': 2,
    'right': 3
}

class RetroSnaker:
    def __init__(self, width, height, ROW, COL, side, seed=None):
        self.size = self.width, self.height = width, height
        self.clock = pygame.time.Clock()


        self.ROW = 0
        self.COL = 0

        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode(self.size)

        # 定义格子的行列
        self.ROW = ROW
        self.COL = COL
        # 游戏地图边长
        self.side = side
        # 地图坐标
        self.x1, self.x2 = int((self.COL - self.side) / 2), int((self.COL + self.side) / 2)
        self.y1, self.y2 = int((self.ROW - self.side) / 2), int((self.ROW + self.side) / 2)
        # 网格的宽度和高度
        self.cell_width = self.width / self.COL
        self.cell_height = self.height / self.ROW

        self.reward = 0

        if seed != None:
            random.seed(seed)

        self.distance_list = []

    def manhattan_distance(self, point1, point2):
        return abs(point1.row - point2.row) + abs(point1.col - point2.col)

    def init_color(self, bg_color, body_color, head_color, food_color, grid_color):
        # 颜色
        self.bg_color = bg_color
        self.body_color = body_color  # 蛇身体颜色
        self.head_color = head_color  # 蛇头颜色
        self.food_color = food_color
        self.grid_color = grid_color
        # 背景色填充
        self.screen.fill(self.bg_color)
    def refresh_screen(self):
        # 背景色填充
        self.screen.fill(self.bg_color)
        # 绘制蛇头
        self.draw_rect(self.snake.head, self.head_color)
        # 绘制蛇的身体
        for s in self.snake.snake_nodes:
            self.draw_rect(s, self.body_color)
        # 绘制食物
        self.draw_rect(self.food, self.food_color)
        # 绘制网格
        self.draw_grid()
        pygame.display.flip()
    def is_crush(self):
        # 如果吃到食物，就生成新食物
        if self.snake.is_crush_food:
            self.food = self.create_food()
        # 创到身体就寄
        if self.snake.is_crush_body():
            return True
        if self.snake.food_timer == 0:
            return True
        # 创到边缘也寄
        if self.snake.head.row < 0 or self.snake.head.row >= self.side or self.snake.head.col < 0 or self.snake.head.col >= self.side:
            return True
        return False

    def create_food(self):
        while True:
            pos = Point(row=random.randint(0, self.side-1), col=random.randint(0,self.side-1))
            # 是否撞到标志布尔值
            is_coll = False
            # 是否跟蛇碰上了
            if self.snake.head.row == pos.row and self.snake.head.col == pos.col:
                is_coll = True
            # 蛇的身子是否碰到食物
            for s in self.snake.snake_nodes:
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

    def put_in_snake(self, snake):
        self.snake = snake
        self.food = self.create_food()

    def step(self, action):
        # # 键盘控制
        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         game_state = False
        #     elif event.type == KEYDOWN:
        #         if event.key == K_LEFT or event.key == K_a:
        #             self.snake.LEFT()
        #             break
        #         elif event.key == K_RIGHT or event.key == K_d:
        #             self.snake.RIGHT()
        #             break
        #         elif event.key == K_UP or event.key == K_w:
        #             self.snake.UP()
        #             break
        #         elif event.key == K_DOWN or event.key == K_s:
        #             self.snake.DOWN()
        #             break

        # 模型控制
        if action == 0:
            self.snake.keep()
        elif action == 1:
            self.snake.turn_left()
        elif action == 2:
            self.snake.turn_right()

        game_state = False
        # 移动
        self.snake.move(self.food)
        if self.is_crush():
            game_state = True
        self.refresh_screen()

        # self.reward -= 1

        if game_state:
            self.reward += -10

        else:
            self.next_state = self.get_state_vector()

            # 计算蛇头和食物之间的距离
            distance = self.manhattan_distance(self.snake.head, self.food)
            if len(self.distance_list) < 2:
                self.distance_list.append(distance)
            else:
                self.distance_list.pop(0)
                self.distance_list.append(distance)
                distance = self.distance_list[1] - self.distance_list[0]
                # 根据距离调整奖励
                if distance < 0:
                    distance_reward = 2  # 靠近食物时的奖励
                else:
                    distance_reward = -2  # 远离食物时的小惩罚
                self.reward += self.snake.score + distance_reward

            if self.snake.is_crush_food:  # 吃到食物
                # print("Add ,", 20 * self.snake.score)
                self.reward += 50 * self.snake.score  # 增加吃到食物的奖励
            else:
                self.reward -= 1

            self.next_state = self.get_state_vector()
            self.reward += self.snake.score

        # print(self.reward)
        return self.next_state, self.reward, game_state

    def get_state_vector(self):
        """
        :return: 返回游戏状态向量
        """
        # state = []
        # # 蛇头的位置
        # state.append(self.snake.head.tuple())
        # # 蛇的身体
        # body = []
        # for s in self.snake.snake_nodes:
        #     body.append(s.tuple())
        # state.append(body)
        # # 食物的位置
        # state.append(self.food.row)
        # state.append(self.food.col)
        # # 方向
        # state.append(self.snake.direct)
        # # 分数
        # state.append(self.snake.score)
        # return state
        # 将整个游戏地图转换为一个向量
        state = [0] * (self.side * self.side)
        state[self.snake.head.row * self.side + self.snake.head.col] = 1  # 蛇头位置
        state[self.food.row * self.side + self.food.col] = 2  # 食物位置
        # 蛇的身体部分
        for s in self.snake.snake_nodes:
            state[s.row * self.side + s.col] = 3
        # 蛇头的位置
        state.append(self.snake.head.tuple()[0])
        state.append(self.snake.head.tuple()[1])
        # 方向
        state.append(Direction[self.snake.direct])



        # # 将整个游戏地图转换为一个向量
        # state = [[0] * self.side]*self.side
        # # 蛇头位置
        # state[self.snake.head.row][self.snake.head.col] = 1
        # # 食物位置
        # state[self.food.row][self.food.col] = 2
        #
        # # 蛇的身体部分
        # for s in self.snake.snake_nodes:
        #     state[s.row][s.col] = 3
        return state