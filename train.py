import os
import matplotlib.pyplot as plt
from snake import Snake
from snakeGame import RetroSnaker
from agent import Agent
import torch
from datetime import datetime

from torch.utils.tensorboard import SummaryWriter


def save_model(agent, episode, total_reward, model_dir='model_weights', filename=None):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # 定义文件名，包括日期时间、训练周期和总奖励
    # timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    if filename is None:
        filename = f"model_epoch_{episode}_reward_{total_reward}.pth"
    filepath = os.path.join(model_dir, filename)

    # 保存模型权重
    torch.save(agent.model.state_dict(), filepath)

    # 打印保存路径
    # print(f"Model saved to {filepath}")

    # # 可选：保存额外的训练信息
    # with open(os.path.join(model_dir, f"training_info_{timestamp}.txt"), 'w') as f:
    #     f.write(f"Epoch: {episode}\n")
    #     f.write(f"Total Reward: {total_reward}\n")
    #     # 可以添加更多的信息，如损失、准确率等

if __name__ == '__main__':
    """
    游戏初始化
    """
    width, height = 390, 390
    bg_color = (0, 0, 0)
    body_color = (70, 161, 98)  # 蛇身体颜色
    head_color = (46, 99, 255)  # 蛇头颜色
    food_color = (255, 0, 0)
    grid_color = (255, 255, 255)

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


    """
    模型初始化
    """

    agent = Agent(input_size=13*13+3, hidden_size=128, output_size=3)
    loss_history = []
    reward_history = []
    total_rewards = []

    # 创建一个SummaryWriter实例（可以选择指定日志目录）
    daytime = datetime.now().strftime("%Y%m%d-%H%M%S")
    writer = SummaryWriter('runs/{}'.format(daytime))
    best_reward = 0
    for episode in range(1, 100000):
        # 游戏循环标志变量
        game_state = False
        SnakeGame = RetroSnaker(width, height, ROW, COL, side, seed)
        SnakeGame.init_color(bg_color, body_color, head_color, food_color, grid_color)  # 初始化游戏配色
        snake = Snake(speed, direct, score, side // 2, side // 2)  # 新建蛇实例
        SnakeGame.put_in_snake(snake)  # 放置蛇
        state = SnakeGame.get_state_vector()
        total_reward = 0
        while not game_state:
            state_vector = SnakeGame.get_state_vector()

            action = agent.act(state)
            # print(action)
            next_state, reward, game_state = SnakeGame.step(action)
            total_reward += reward
            agent.remember(state, action, reward, next_state, game_state)
            state = next_state
            total_reward += reward

            if len(agent.memory) > 100:
                loss = agent.replay()
                loss_history.append(loss.item())
                writer.add_scalar('Loss/train', loss.item(), episode)


            # 帧速率
            SnakeGame.clock.tick(50)
        # print("Reward: ", total_reward)
        # pygame.quit()
        writer.add_scalar('Reward/train', total_reward, episode)
        print(f'Episode: {episode}, Total reward: {total_reward}')
        # print(f"Average Loss {sum(loss_history) / len(loss_history)}")
        total_rewards.append(total_reward)
        if total_reward > best_reward:
            best_reward = total_reward
            save_model(agent, episode, total_reward, model_dir=f'model_weights/{daytime}', filename="best.pth")

        if episode % 100 == 0:
            # torch.save(agent.model.state_dict(), f'model_weights_episode_{episode}.pth')
            save_model(agent, episode, total_reward, model_dir=f'model_weights/{daytime}')

    plt.plot(loss_history, label='Loss')
    plt.plot(total_rewards, label='Total Reward')
    plt.legend()
    plt.show()
writer.close()

