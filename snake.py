from point import Point
class Snake:
    def __init__(self,ROW, COL):
        """
        :param ROW: 格子的行数
        :param COL: 格子的列数
        """
        self.is_crush_food = False
    def initSnake(self,speed,direct,score):
        """
        :param speed: 蛇移动的速度
        :param direct: 蛇移动的方向
        :param score: 蛇的分数
        :param head: 蛇头实例化
        """
        self.speed = speed
        self.direct = direct
        self.score = score
        self.snakes = []
        # 实例化蛇头
        self.head = Point(12, 12)

    def move(self, food):
        """
        :param food: 食物的Point实例
        :param is_crush_food: 是否吃到食物（用于游戏重新生成食物）
        移动并进行吃东西检测
        """
        self.food = food
        # 处理蛇的身体
        self.snakes.insert(0, self.head.copy())
        if self.direct == 'left':
            self.head.col -= self.speed
        elif self.direct == 'right':
            self.head.col += self.speed
        elif self.direct == 'up':
            self.head.row -= self.speed
        elif self.direct == 'down':
            self.head.row += self.speed
        # 吃东西
        if self.is_crush(self.food):
            self.is_crush_food = True
            self.score += 1
        else:
            self.is_crush_food = False
            self.snakes.pop()

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
        for s in self.snakes:
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
