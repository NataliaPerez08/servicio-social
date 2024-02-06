# https://github.com/rdamianzin/HSCap
import torch
from torch import nn
import torch.optim as optim

from torch.utils.data import Dataset, DataLoader


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
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

X = torch.rand(2151, device=device)
logits = model(X)
print(logits)
pred_probab = nn.Softmax(dim=0)(logits)
y_pred = pred_probab.argmax(-1)
print(f"Predicted class: {y_pred}")

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
