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

