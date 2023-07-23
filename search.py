from point import Point
def is_valid(x, y):
    if (x>=0 and x <= 23 and y >= 0 and y <= 23 and (map[x][y] == 0 or map[x][y] == 4)):
        return True
    else:
        return False
# def surround(qout):
#     return [[qout[0] - 1, qout[1]], [qout[0] + 1, qout[1]], [qout[0], qout[1] - 1], [qout[0], qout[1] + 1]]
# def search(head,food,bodys,lab):
#     '''
#     最优化路径选择
#     '''
#     for body in bodys:
#         lab[body[0]][body[1]] = 1
#     x, y = head[0], head[1]
#     lab[x][y] = 2
#     lab[food[0]][food[1]] = 4
#     q = []
#     q.append(head)
#     qout = head
#     while len(q) > 0 and qout != food:
#         qout = q.pop(0)
#         lab[qout[0]][qout[1]] = 3
#         sur = surround([qout[0], qout[1]])
#         for i in sur:
#             # print(i)
#             if is_valid(lab, i[0], i[1]):
#                 if i not in q:
#                     q.append(i)
#
#
#     print('find')


    # walk(x-1, y)
    # walk(x, y-1)
    # walk(x+1, y)
    # walk(x, y+1)

# print(surround([15,15]))

# search( head, food , snakes ,lab)
# print(res)


food = [2, 5] # (列， 行)
head = [20,20]
snakes = [[21, 20], [22, 20], [22, 19], [22, 18],
          [21, 18], [20, 18], [19, 18], [18, 18]]
map = [[0 for i in range(24)] for j in range(24)]  # 定义一个24x24的迷宫
for body in snakes:
    map[body[0]][body[1]] = 1
x, y = head[0], head[1]
map[x][y] = 2
map[food[0]][food[1]] = 4


flag = []
def DFS(x, y):
    global flag  # 声明全局变量
    if map[x][y] == 4:
        print(flag)
        return
    if is_valid(x + 1, y):  # 如果下⼀步不是墙 且没⾛过
        map[x][y] = 3  # 标记当前坐标⾛过（不是下⼀步）
        flag.append([x + 1, y])
        DFS(x + 1, y)  # 尝试向下⾛
        flag.pop(-1)
        map[x][y] = 0  # 再设置当前坐标为0 重新找路
    if is_valid(x, y - 1):
        map[x][y] = 3
        flag.append([x, y - 1])
        DFS(x, y - 1)
        flag.pop(-1)
        map[x][y] = 0
    if is_valid(x - 1, y):
        map[x][y] = 3
        flag.append([x - 1, y])
        DFS(x - 1, y)
        flag.pop(-1)
        map[x][y] = 0
    if is_valid(x, y + 1):
        map[x][y] = 3
        flag.append([x, y + 1])
        DFS(x, y + 1)
        flag.pop(-1)
        map[x][y] = 0


if __name__ == '__main__':
    DFS(head[0], head[1])
