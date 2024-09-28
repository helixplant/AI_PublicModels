#import statements
import torch
import torch.nn as nn
import torch.nn.functional as F


# model class that inherits module
class Model(nn.Module):
    # input layer
    # self, input features, hidden layer 1, hidden layer 2, output features
    def __init__(self, in_features=4. h1=8, h2=9, out_features=3):
        super().__init__()
        self.fc1 = nn.Linear(in_features, h1)
        self.fc1 = nn.Linear(h1, h2)
        self.out = nn.Linear(h2, out_features)

    def forward(self, x):
        x = F.relu(self.fc1(x)) #rectified linear unit (if <0 then lets call it 0)
        x = F.relu(self.fc2(x))
        x = self.out
        return x