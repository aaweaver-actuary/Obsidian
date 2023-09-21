[Official Docs](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html)

Parameters:

- `num_embeddings` (int) – size of the dictionary of #embedding's
- `embedding_dim` (int) – the size of each #embedding vector
- `padding_idx` (int, optional) – If specified, the entries at `padding_idx` do not contribute to the [[Gradient Vector|gradient vector]]; therefore, the #embedding vector at `padding_idx` is not updated during training, i.e. it remains as a fixed “pad”. For a newly constructed Embedding, the #embedding vector at `padding_idx` will default to all zeros, but can be updated to another value to be used as the #padding-vector.
- `max_norm` (float, optional) – If given, each #embedding vector with #norm larger than `max_norm` is #renormalized to have #norm `max_norm`.
- `norm_type` (float, optional) – The $p$ of the $p$- #norm to compute for the `max_norm` option. Default `2`.
- `scale_grad_by_freq` (bool, optional) – If given, this will scale a [[Gradient Vector|gradient vector]]  by the inverse of frequency of the words in the mini-batch. Default `False`.
- `sparse` (bool, optional) – If `True`, [[Gradient Vector|gradient vector]] w.r.t. `weight` matrix will be a sparse tensor. See Notes for more details regarding sparse gradients.

Variables:

`weight` (Tensor) – the learnable weights of the module of shape `(num_embeddings, embedding_dim)` initialized from `N(0,1)N(0,1)`

Shape:

- Input: (∗)(∗), IntTensor or LongTensor of arbitrary shape containing the indices to extract
- Output: (∗,H)(∗,H), where \* is the input shape and H=embedding_dimH=embedding_dim

> note
>When `max_norm` is not `None`, [`Embedding`](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding "torch.nn.Embedding")’s forward method will modify the `weight` tensor in-place. Since tensors needed for gradient computations cannot be modified in-place, performing a differentiable operation on `Embedding.weight` before calling [`Embedding`](https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html#torch.nn.Embedding "torch.nn.Embedding")’s forward method requires cloning `Embedding.weight` when `max_norm` is not `None`. For example:

n, d, m = 3, 5, 7
embedding = nn.Embedding(n, d, max_norm=True)
W = torch.randn((m, d), requires_grad=True)
idx = torch.tensor([1, 2])
a = embedding.weight.clone() @ W.t()  # weight must be cloned for this to be differentiable
b = embedding(idx) @ W.t()  # modifies weight in-place
out = (a.unsqueeze(0) + b.unsqueeze(1))
loss = out.sigmoid().prod()
loss.backward()