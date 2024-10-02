import torch.nn as nn
import torch.nn.functional as F


class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

        self.layer1 = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU()
        )
        self.layer2 = nn.Sequential(
            nn.Linear(128, 256),
            nn.ReLU()
        )
        self.layer3 = nn.Sequential(
            nn.Linear(256, 512),
            nn.ReLU()
        )
        self.layer4 = nn.Sequential(
            nn.Linear(512, 256),
            nn.ReLU()
        )
        self.layer5 = nn.Sequential(
            nn.Linear(256, 128),
            nn.ReLU()
        )
        self.layer6 = nn.Sequential(
            nn.Linear(128, output_size)
        )
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        x = self.layer6(x)
        return x


class CNN(nn.Module):
    def __init__(self, input_channels, output_size):
        super(CNN, self).__init__()
        self.output_size = output_size
        self.conv1 = nn.Conv2d(input_channels, 32, kernel_size=3, padding=1)  # 第一个卷积层
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)  # 第二个卷积层
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)  # 第三个卷积层
        self.fc1 = nn.Linear(1, 512)  # 全连接层，这里需要确保输入特征数量正确
        self.fc2 = nn.Linear(512, output_size)

    def forward(self, x):
        print(x.shape)
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)  # 池化层，减少维度
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)  # 池化层，减少维度
        x = F.relu(self.conv3(x))
        x = F.max_pool2d(x, 2)  # 池化层，减少维度
        x = x.view(x.size(0), -1)  # 展平
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return x