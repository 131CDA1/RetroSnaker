from point import Point
# ROW = 30
# COL = 40
# q = []
# qRead = []
# def if_in(point):
#     if point in qRead or point.row == ROW or point.row == 4 or point.col == COL or point.col == -1:
#         return False
#     else:
#         return True
# def breadthFS(tail, food):
#     if tail not in qRead:
#         qRead.append(tail)
#     q.append(tail)
#
#     if len(q) != 0:
#         head = q.pop(0)
#
#     up, down, left, right = head.surround()
#     if up not in qRead:
#         qRead.append(up)
#     if down not in qRead:
#         qRead.append(down)
#     if left not in qRead:
#         qRead.append(left)
#     if right not in qRead:
#         qRead.append(right)
#
#     if up == food or down == food or left == food or right == food:
#         return
#
#     if if_in(up):
#         q.append(up)
#     if if_in(up):
#         q.append(down)
#     if if_in(up):
#         q.append(left)
#     if if_in(up):
#         q.append(right)

# food = Point(2, 5) # (行, 列)
# head = Point(20,20)
# snakes = [Point(20, 21), Point(20, 22), Point(19, 22), Point(18, 22),
#           Point(18, 21), Point(18, 20), Point(18, 19), Point(18, 18)]

food = (2, 5) # (列， 行)
head = (20,20)
snakes = [(21, 20), (22, 20), (22, 19), (22, 18),
          (21, 18), (20, 18), (19, 18), (18, 18)]


def search(point, des):
    x, y = point[0], point[1]
    up, down, left, right = (x, y-1), (x, y+1), (x-1, y), (x+1, y)
    if point != des:
        return search(up, des), search(left,des), search(down, des), search(right,des)
    if point == des:
        return point

search(head, food)



