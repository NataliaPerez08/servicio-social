# https://github.com/rdamianzin/HSCap
import torch
from torch import nn
import torch.optim as optim

from torch.utils.data import Dataset, DataLoader

import control_entrenador as ce

class Estandar(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(2151,512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 5),
        )
        
    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits
    
device = "cuda" if not torch.cuda.is_available() else "mps"
if torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

model = Estandar()
print(model)

espectros = ce.recupera_espectros()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

def train(model, loss_fn, optimizer):
    for e in espectros:
        X, y = ce.get_x_y(e,'pigmento')
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

epochs = 5

train(model, criterion, optimizer)
"""
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, criterion, optimizer)
print("Done!")
"""

