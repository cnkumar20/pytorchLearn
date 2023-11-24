import torch
def p(msg):
    print(msg)

p(torch.__version__)

scalar = torch.tensor(88)
p(scalar)


vect = torch.tensor([1,2])
p(vect)

MATRIX = torch.tensor([[1,2,4,5],[2,5,6,2]])
p(MATRIX.ndim)
p(MATRIX.shape)

TENSOR = torch.tensor([[[1,2,4,5],[2,5,6,2],[3,4,5,1]]])
p(TENSOR.ndim)
p(TENSOR.shape)


TENSOR = torch.zeros(size=(1,1))
p(TENSOR)
p(TENSOR.shape)

TENSOR = torch.zeros(size=(1,3))
p(TENSOR)
p(TENSOR.shape)

TENSOR = torch.ones(size=(1,2,3))
p(TENSOR)
p(TENSOR.shape)


TENSOR = torch.zeros_like(TENSOR)
p(TENSOR)
p(TENSOR.shape)



TENSOR = torch.rand(size=(2,3))
p(TENSOR)
p(TENSOR.shape)

TENSOR = torch.zeros(size=(2,3),dtype=torch.int)
p(TENSOR)
p(TENSOR.shape)

TENSOR = torch.rand(size=(2,3),dtype=torch.float64)
p(TENSOR)
p(TENSOR.shape)


torch.cuda_version
p(torch.cuda)

