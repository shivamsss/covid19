import numpy as np
import pandas as pd

oddnumber=np.arange(1,100,2)
evennumber=np.arange(0,100,2)
numbers={"oddnumbers":oddnumber,"evennumbers":evennumber}
table=pd.DataFrame(numbers)
print(table)

print("SUM")
print(table.sum())

print("MAX")
print(table.max())