from point import Point

food = [2, 5] # (列， 行)
head = [20,20]
snakes = [[21, 20], [22, 20], [22, 19], [22, 18],
          [21, 18], [20, 18], [19, 18], [18, 18]]
lab = [[0 for i in range(24)] for j in range(24)]  # 定义一个24x24的迷宫


def search(head,food,bodys,lab):
    '''
    最优化路径选择
    '''
    for body in bodys:
        lab[body[0]][body[1]] = 1
    x, y = head[0], head[1]
    lab[x][y] = 2

    def is_valid(lab,x,y):
        if (x>=0 and x <len(lab) and y >= 0 and lab[x][y]==1):
            return True
        else:
            return False

    def walk(x,y,food):
        if x == food[0] and y == food[1]:
            print('success')
            return True
    if is_valid(lab,x,y):
        lab[x][y] = 2
        walk(x-1, y, lab)
        walk(x, y-1, lab)
        walk(x+1, y, lab)
        walk(x, y+1, lab)



search( head, food , snakes ,lab)
# print(res)








