import os
import matplotlib.pyplot as plt
from snake import Snake
from snakeGame import RetroSnaker
from agent import Agent
import torch
from datetime import datetime

from torch.utils.tensorboard import SummaryWriter

def test_model(model_path, agent, SnakeGame, width, height, ROW, COL, side, seed):
    """
    游戏初始化
    """
    bg_color = (0, 0, 0)
    body_color = (70, 161, 98)  # 蛇身体颜色
    head_color = (46, 99, 255)  # 蛇头颜色
    food_color = (255, 0, 0)
    grid_color = (255, 255, 255)
    game_state = False

    # 控制和移动
    speed = 1
    direct = 'left'
    # 初始得分
    score = 0

    # 定义格子的行列
    ROW = 13
    COL = 13
    # 游戏地图边长
    side = 13
    # 随机数种子
    seed = 114514

    agent.model.load_state_dict(torch.load(model_path))
    agent.model.eval()

    SnakeGame.init_color(bg_color, body_color, head_color, food_color, grid_color)  # 初始化游戏配色
    snake = Snake(speed, direct, score, side // 2, side // 2)  # 新建蛇实例
    SnakeGame.put_in_snake(snake)  # 放置蛇
    state = SnakeGame.get_state_vector()
    total_reward = 0
    while not game_state:
        state_tensor = torch.tensor(state, dtype=torch.float).unsqueeze(0)
        with torch.no_grad():
            action = agent.act(state_tensor.numpy())
        next_state, reward, game_state = SnakeGame.step(action)
        total_reward += reward
        state = next_state

        # 帧速率
        SnakeGame.clock.tick(50)

    print(f'Test Total reward: {total_reward}')

if __name__ == '__main__':
    width, height = 390, 390
    agent = Agent(input_size=13*13+3, hidden_size=128, output_size=3)
    SnakeGame = RetroSnaker(width, height, 13, 13, 13, seed=None)

    model_path = 'model_epoch_15600_reward_208970.pth'  # 替换成你的模型路径

    test_model(model_path, agent, SnakeGame, width, height, 13, 13, 13, 114514)