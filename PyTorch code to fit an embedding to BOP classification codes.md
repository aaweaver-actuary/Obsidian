```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define dimensions
input_dim = 1500  # Number of unique BOP codes
embedding_dim = 20  # Desired lower-dimensional space

# Create a PyTorch model
class EmbeddingClassifier(nn.Module):
    def __init__(self):
        super(EmbeddingClassifier, self).__init__()
        self.embedding = nn.Embedding(input_dim, embedding_dim)
        self.flatten = nn.Flatten()
        self.fc = nn.Linear(embedding_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.embedding(x)
        x = self.flatten(x)
        x = self.fc(x)
        x = self.sigmoid(x)
        return x

# Example usage with dummy data
model = EmbeddingClassifier()
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.BCELoss()  # Binary Cross-Entropy loss for binary classification

# Dummy training loop (replace with your data and training loop)
for epoch in range(10):
    input_data = torch.randint(0, input_dim, (64, 1)) # Example input data
    target = torch.randint(0, 2, (64, 1), dtype=torch.float) # Example target data
    optimizer.zero_grad()
    output = model(input_data)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()

# Extract embeddings
embeddings = model.embedding.weight.detach().numpy()
```