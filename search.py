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

food = Point(2, 5)#(行, 列)
head = Point(20)








