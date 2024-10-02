import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from collections import deque
import random

from model import MLP, CNN

# 定义智能体
class Agent:
    def __init__(self, input_size, hidden_size, output_size):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = MLP(input_size, hidden_size, output_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.0005)  # 调整学习率为0.0005
        self.criterion = nn.MSELoss()
        self.memory = deque(maxlen=10000)  # 增大经验池的容量
        self.target_model = MLP(input_size, hidden_size, output_size)
        self.target_model.load_state_dict(self.model.state_dict())  # 初始化时同步权重
        self.target_model.eval()  # 目标网络不需要训练
        self.training_step = 0
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.min_epsilon = 0.01

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state, epsilon=0.1):
        if epsilon is None:
            epsilon = self.epsilon
        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)
        if np.random.rand() <= epsilon:
            return random.randrange(self.model.output_size)
        state = torch.tensor(state, dtype=torch.float).unsqueeze(0)
        with torch.no_grad():
            action_values = self.model(state)
        return np.argmax(action_values.cpu().numpy())

    def update_target_model(self):
        self.target_model.load_state_dict(self.model.state_dict())

    def replay(self):

        # 如果记忆中的经验少于64条，那么就不进行训练
        if len(self.memory) < 64:  # 增大批次大小为64
            return

        batch = random.sample(self.memory, 64)
        # 将经验中的状态、动作、奖励、下一个状态和完成标志分别提取出来
        states, actions, rewards, next_states, dones = zip(*batch)
        states = torch.tensor(states, dtype=torch.float).to(self.device)
        actions = torch.tensor(actions, dtype=torch.long).to(self.device)
        rewards = torch.tensor(rewards, dtype=torch.float).to(self.device)
        next_states = torch.tensor(next_states, dtype=torch.float).to(self.device)
        dones = torch.tensor(dones, dtype=torch.float).to(self.device)

        # 计算当前状态下执行动作的Q值
        current_q = self.model(states).gather(1, actions.unsqueeze(1)).squeeze(1)

        next_actions = self.model(next_states).argmax(1)  # 主网络选择动作
        next_q = self.target_model(next_states).gather(1, next_actions.unsqueeze(1)).squeeze(1)  # 目标网络评估Q值
        target_q = rewards + (1 - dones) * 0.99 * next_q

        loss = self.criterion(current_q, target_q)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # 更新训练步数
        self.training_step += 1

        # 每100次训练步数更新一次目标网络
        if self.training_step % 100 == 0:
            self.update_target_model()
        return loss