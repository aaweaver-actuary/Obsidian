
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.manifold import TSNE

import torch
import torch.nn as nn
from transformers import BertModel, BertTokenizer

import matplotlib.pyplot as plt
import numpy as np

# Define model class
class ClassCodeEmbeddingsModel(nn.Module):
    def __init__(self,
			    # class codes as tensor
				 class_codes:torch.Tensor 
				 bert_model_name='bert-base-uncased',
				 embedding_dim=8):
        super(HitRatioModel, self).__init__()

        # Hierarchical embedding (based on the first digit of class codes)
        self.hierarchical_embedding = nn.Embedding(
	        vocab_size_hierarchical,
			embedding_dim=embedding_dim
		)

        # Cluster embedding (based on the remaining digits, assuming 
        # predefined clusters)
        self.cluster_embedding = nn.Embedding(
	        vocab_size_clusters,
			embedding_dim=embedding_dim
		)

        # BERT model for semantic embedding (based on class descriptions)
        self.bert = BertModel.from_pretrained(bert_model_name)
        bert_output_dim = self.bert.config.hidden_size

        # Fully connected layers to predict hit counts
        self.fc1 = nn.Linear(embedding_dim * 2 + bert_output_dim, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, class_code, class_desc):
        # Extract first digit for hierarchical embedding
        hierarchical_codes = class_code[:, 0]

        # Extract remaining digits for cluster embedding
		# (assuming pre-clustered)
        cluster_codes = class_code[:, 1:]

        # Hierarchical and cluster embeddings
        hier_embeds = self.hierarchical_embedding(hierarchical_codes)
        cluster_embeds = self.cluster_embedding(cluster_codes)

        # BERT embeddings for class descriptions
        tokenizer = BertTokenizer.from_pretrained(bert_model_name)
        bert_inputs = tokenizer(class_desc,
								return_tensors="pt",
								padding=True,
								truncation=True)
        bert_outputs = self.bert(**bert_inputs)
        bert_embeddings = bert_outputs.last_hidden_state.mean(dim=1)

        # Concatenate all embeddings
        x = torch.cat((hier_embeds,
					   cluster_embeds,
					   bert_embeddings), dim=1)

        # Feed-forward layers
        x = nn.ReLU()(self.fc1(x))
        
        # Sigmoid activation for #binary output
        x = torch.sigmoid(self.fc2(x)) 
        return x

# Example usage



# Assuming class_code, class_desc, and hit_count are provided as tensors
vocab_size_hierarchical = len(set(class_code[:, 0].tolist()))
vocab_size_clusters = 10 # Or the number of clusters you've chosen


```

### old code:
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
criterion = nn.BCELoss()  # #Binary Cross-Entropy loss for #binary classification

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