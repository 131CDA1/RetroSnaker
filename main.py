import random
import time
import pygame
import math
"""
          66
         66
        66
       66   6666
      66 6666666666
      666         666
      66           66
      66           66
       666       666
         666666666

"""



def main():
    #颜色初始化
    white = (255,255,255)
    yellow = (255,255,0)
    black = (0,0,0)
    green = (0,0,255)
    blue = (0,255,0)
    red = (255,0,0)

    #游戏初始化，窗口大小设置
    pygame.init()
    height = 600
    width = 800

    #设置窗口
    window = pygame.display.set_mode((height, width))
    pygame.display.set_caption('RetroSnaker')

    #设置游戏帧率
    clock = pygame.time.Clock()

    #设置蛇的大小和速度
    snake_block = 10
    snake_speed = 12

    while True:
        # 事件循环
        for event in pygame.event.get():
            # 如果点击退出，则关闭程序
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # 绘图,更新
        pygame.display.update()




if __name__ == '__main__':
    main()

