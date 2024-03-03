# https://github.com/rdamianzin/HSCap
from sklearn.calibration import LabelEncoder
import torch
from torch import nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
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
            nn.ReLU(),
            nn.Linear(5, 1),
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

X,y = ce.get_x_y(espectros,'pigmento')
lb = LabelEncoder()
y = lb.fit_transform(y)

X_train = torch.tensor(X, dtype=torch.float32)
y_train = torch.tensor(y, dtype=torch.long)

train_data = torch.utils.data.TensorDataset(X_train, y_train)
train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)


def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
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
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_loader, model, criterion, optimizer)
print("Done!")

