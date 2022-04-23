from dataclasses import dataclass
import pandas as pd

path = 'study\pandas\pd001.csv'
# data = pd.DataFrame({'1':[1,2,3,4,5,6,7,8,9],'2':['11','22','33','44','55','66','77','88','99']})
# data = data.set_index('1')
# data.to_csv(path)

data = pd.read_table(path,sep=',')
print(data)

print('新建完成')
