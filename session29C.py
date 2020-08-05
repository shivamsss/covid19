import numpy as np
import pandas as pd
data=np.random.randn(5,4)
print(data)
print(data.shape)
table = pd.DataFrame(data=data, columns=["COL1", "COL2", "COL3", "COL4"])
print(table)

for key,value in table.iteritems():
    print(key)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(value)


for row in table.itertuples():
    print(row)
    print("*******")