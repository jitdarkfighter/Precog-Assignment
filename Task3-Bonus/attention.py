import torch
import torch.nn as nn


class Attention(nn.Module):
    def __init__(self, encoder_dim, hidden_dim=512):
        super(Attention, self).__init__()
        self.encoder_dim = encoder_dim
        self.hidden_dim = hidden_dim
        
        self.U = nn.Linear(hidden_dim, hidden_dim)
        self.W = nn.Linear(encoder_dim, hidden_dim)
        self.v = nn.Linear(hidden_dim, 1)
        self.tanh = nn.Tanh()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, img_features, hidden_state):
        # img_features: (batch_size, seq_len, encoder_dim)
        # hidden_state: (batch_size, hidden_dim)
        
        batch_size = img_features.size(0)
        seq_len = img_features.size(1)
        
        # Expand hidden state to match sequence length
        U_h = self.U(hidden_state).unsqueeze(1).expand(batch_size, seq_len, self.hidden_dim)
        
        # Transform image features
        W_s = self.W(img_features)
        
        # Compute attention scores
        att = self.tanh(W_s + U_h)
        e = self.v(att).squeeze(2)  # (batch_size, seq_len)
        alpha = self.softmax(e)
        
        # Compute context vector
        context = (img_features * alpha.unsqueeze(2)).sum(1)
        
        return context, alpha
