class Point:
    row = 0
    col = 0

    ROW = 30
    COL = 40

    def __init__(self, row, col):
        """
        :param row: 行
        :param col: 列
        :param is_edge:是否为边缘
        """
        self.row = row
        self.col = col

    def __str__(self):
        return (self.row, self.col)

    def tuple(self):
        return (self.row, self.col)

    def copy(self):
        return Point(row=self.row, col=self.col)

    def surround(self):
        # 返回四周的四个点
        # 上下左右
        self.up = Point(row = self.row-1,col = self.col)
        self.down = Point(row = self.row+1,col = self.col)
        self.left = Point(row = self.row,col = self.col-1)
        self.right = Point(row = self.row,col = self.col+1)

        return self.up, self.down, self.left, self.right


class Snake:
    def __init__(self, speed, direct, score, init_x, init_y):
        """
        :param speed: 蛇移动的速度
        :param direct: 蛇移动的方向
        :param score: 蛇的分数
        :param head: 蛇头实例化
        """
        self.is_crush_food = False
        self.speed = speed
        self.direct = direct
        self.score = score
        self.snake_nodes = []
        # 实例化蛇头
        self.head = Point(init_x, init_y)
        self.init_food_time = -1
        self.food_timer = self.init_food_time    # 50步就饿死

    def move(self, food):
        """
        :param food: 食物的Point实例
        :param is_crush_food: 是否吃到食物（用于游戏重新生成食物）
        移动并进行吃东西检测
        """
        self.food = food
        # 处理蛇的身体
        self.snake_nodes.insert(0, self.head.copy())
        if self.direct == 'left':
            self.head.col -= self.speed
        elif self.direct == 'right':
            self.head.col += self.speed
        elif self.direct == 'up':
            self.head.row -= self.speed
        elif self.direct == 'down':
            self.head.row += self.speed

        self.food_timer -= 1
        # 吃东西
        if self.is_crush(self.food):
            self.is_crush_food = True
            self.score += 1

            self.food_timer = self.init_food_time
        else:
            self.is_crush_food = False
            self.snake_nodes.pop()

    def is_crush(self, point):
        """
        :param point: 被撞击的点
        :return: 是否撞击
        """
        self.point = point
        if self.head.row == point.row and self.head.col == point.col:
            return True
        else:
            return False
    def is_crush_body(self):
        """
        :return: 是否撞到自己
        """
        for s in self.snake_nodes:
            if s.row == self.head.row and s.col == self.head.col:
                return True
        return False
    def LEFT(self):
        if self.direct == 'up' or self.direct == 'down':
            self.direct = 'left'
    def RIGHT(self):
        if self.direct == 'up' or self.direct == 'down':
                self.direct = 'right'
    def UP(self):
        if self.direct == 'left' or self.direct == 'right':
            self.direct = 'up'
    def DOWN(self):
        if self.direct == 'left' or self.direct == 'right':
            self.direct = 'down'

    def keep(self):
        pass
    def turn_left(self):
        if self.direct == 'up':
            self.direct = 'left'
        elif self.direct == 'left':
            self.direct = 'down'
        elif self.direct == 'down':
            self.direct = 'right'
        elif self.direct == 'right':
            self.direct = 'up'
    def turn_right(self):
        if self.direct == 'up':
            self.direct = 'right'
        elif self.direct == 'right':
            self.direct = 'down'
        elif self.direct == 'down':
            self.direct = 'left'
        elif self.direct == 'left':
            self.direct = 'up'