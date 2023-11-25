# -*- coding: utf-8 -*-
"""pytorchlearn_learn_tensor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xCM-FpMZBceWUOSQG7Cz3MBX9D0GLkSs
"""

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(torch.__version__)



scalar = torch.tensor(8)

scalar.item()

some_tensor = torch.rand(size=(2,3))
some_tensor

t1 = torch.rand(size=(3,3))

t2 = torch.rand(size=(3,3))
t2

t1.matmul(t2)

torch.matmul(t1,t2)

t1.device

t2.device

t1 = torch.rand(size=(4, 3),device='cuda')

t1.device
t1

t2 = torch.rand(size=(4, 3),device='cuda')

t3 = torch.rand(size=(3,4),device='cpu')

t1.matmul(t2.T)

temp = torch.rand(size=(3,4))
temp.matmul(t3.T)

t1.reshape((3,4))

t1.squeeze(dim=0)

"""**Note ** Tensor view point to the same existing in memory"""



view = t1.view((6,2))
view

t1.squeeze(dim=-1)

t1

t1.unsqueeze(dim=2)

t1.permute(dims=(1,0))

t1.permute(dims=(0,1))

"""**Note** permute is a view with specified dimension"""

t1.permute(dims=(-1,0))

t1+t2

t1-t2

t1*t2

t1
3*t1

t1 @ t2.T
