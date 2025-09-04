import torch
import torch.nn as nn
import torch.nn.functional as F

class Encoder(nn.Module):
    def __init__(self, input_channels, num_classes, img_height, img_width):
        super(Encoder, self).__init__()

        # Deeper CNN for spatial features, follows VGG arch
        self.conv1 = nn.Conv2d(input_channels, 64, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.conv4 = nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.conv5 = nn.Conv2d(256, 512, kernel_size=3, padding=1)
        self.conv6 = nn.Conv2d(512, 512, kernel_size=3, padding=1)
        self.conv7 = nn.Conv2d(512, 512, kernel_size=2, padding=0)
        
        # Batch normalization layers
        self.bn4 = nn.BatchNorm2d(256)
        self.bn6 = nn.BatchNorm2d(512)
        
        # Pooling layers
        self.pool = nn.MaxPool2d(2, 2)
        self.pool_h = nn.MaxPool2d(kernel_size=(2, 1))  

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))  
        x = self.pool(F.relu(self.conv2(x)))  
        # conv3 and conv4 do not have pooling
        x = F.relu(self.conv3(x))  
        x = F.relu(self.bn4(self.conv4(x)))  
        x = self.pool_h(x) 
        # conv5 and conv6 with batch normalization and pooling with respect to height at the end
        x = F.relu(self.conv5(x))  
        x = F.relu(self.bn6(self.conv6(x)))  
        x = self.pool_h(x)  
        x = F.relu(self.conv7(x))  

        """
        According to the paper
        from left to right, a vector of feature sequence is generated from the feature maps. 
        This means the ith feature vector is the concatenation of the ith column of all maps
        """
        b, c, h, w = x.size()
        # (Batch size, channels*height, width)
        x = x.view(b, c*h, w)
        # (sequence length = width, batch = b, features = channels*height)
        x = x.permute(2, 0, 1)  

        return x
    