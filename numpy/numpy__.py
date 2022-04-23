import numpy as np

a = np.random.randn(20).reshape(4,5)
print(a)
b = a.argsort()

print(b)
c = b[:,3]
print(c)

import matplotlib as plt
x轴 = np.linspace(-10,10,100) # 在[-10,10]闭区间或半闭区间中，数量为100
y轴 = np.sin(x轴)  # sin正弦、cos余弦
plt.plot(x轴,y轴)
plt.show()