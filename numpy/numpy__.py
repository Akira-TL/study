import numpy as np

a = np.random.randn(20).reshape(4,5)
print(a)
b = a.argsort()
print(a.sum())
print(b)
c = b[:,3]
print(c)
