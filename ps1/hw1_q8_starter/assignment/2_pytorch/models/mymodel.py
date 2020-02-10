import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


class MyModel(nn.Module):
    def __init__(self, im_size, hidden_dim, kernel_size, n_classes):
        '''
        Extra credit model

        Arguments:
            im_size (tuple): A tuple of ints with (channels, height, width)
            hidden_dim (int): Number of hidden activations to use
            kernel_size (int): Width and height of (square) convolution filters
            n_classes (int): Number of classes to score
        '''
        super(MyModel, self).__init__()
        #############################################################################
        # TODO: Initialize anything you need for the forward pass
        #############################################################################
        self.pool_size = 2
        self.num_filters = hidden_dim
        self.num_classes = n_classes
        self.conv = nn.Conv2d(im_size[0], hidden_dim, kernel_size=kernel_size, stride=1, padding=(kernel_size - 1)//2)
        self.ReLU = nn.ReLU(inplace=True)
        self.max_pooling = nn.MaxPool2d(kernel_size=self.pool_size)
        self.fully_connected = nn.Linear(hidden_dim * (im_size[1] // self.pool_size) * (im_size[2] // self.pool_size), n_classes)
        # self.conv_relu_conv_relu_pool_1 = nn.Sequential(
        #     nn.Conv2d(im_size[0], hidden_dim, kernel_size=kernel_size, stride=1, padding=(kernel_size - 1) // 2),
        #     # nn.ReLU(),
        #     # nn.Conv2d(hidden_dim, hidden_dim, kernel_size=kernel_size, stride=1, padding=(kernel_size - 1) // 2),
        #     nn.ReLU(inplace=True),
        #     nn.MaxPool2d(kernel_size=self.pool_size)
        # )
        # self.conv_relu_conv_relu_pool_N = nn.Sequential(
        #     nn.Conv2d(hidden_dim, hidden_dim, kernel_size=kernel_size, stride=1, padding=(kernel_size - 1) // 2),
        #     # nn.ReLU(),
        #     # nn.Conv2d(hidden_dim, hidden_dim, kernel_size=kernel_size, stride=1, padding=(kernel_size - 1) // 2),
        #     nn.ReLU(inplace=True),
        #     nn.MaxPool2d(kernel_size=self.pool_size)
        # )
        #self.softmax = nn.Softmax(dim=0)
        #############################################################################
        #                             END OF YOUR CODE                              #
        #############################################################################

    def forward(self, images):
        '''
        Take a batch of images and run them through the model to
        produce a score for each class.

        Arguments:
            images (Variable): A tensor of size (N, C, H, W) where
                N is the batch size
                C is the number of channels
                H is the image height
                W is the image width

        Returns:
            A torch Variable of size (N, n_classes) specifying the score
            for each example and category.
        '''
        scores = None
        #############################################################################
        # TODO: Implement the forward pass.
        #############################################################################
        # out = None
        # num_convs = 1
        # for i in range(num_convs):
        #     if i == 0:
        #         out = self.compute_conv_1(images)
        #     else:
        #         out = self.compute_conv_N(out)
        # height, width = images.shape[2], images.shape[3]
        # fully_connected = nn.Linear(self.num_filters * (height // (self.pool_size * num_convs)) *
        #                             (width // (self.pool_size * num_convs)), self.num_classes)
        # scores = fully_connected(out.view(out.shape[0], -1))
        out = self.conv(images)
        out = self.ReLU(out)
        out = self.max_pooling(out)
        scores = self.fully_connected(out.view(images.shape[0], -1))
        #scores = self.softmax(out)
        #############################################################################
        #                             END OF YOUR CODE                              #
        #############################################################################
        return scores

    def compute_conv_1(self, images):
        out = self.conv_1(images)
        out = self.ReLU(out)
        return self.max_pooling(out)

    def compute_conv_N(self, params):
        out = self.conv_N(params)
        out = self.ReLU(out)
        return self.max_pooling(out)
