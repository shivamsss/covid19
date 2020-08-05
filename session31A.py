import pandas as pd
import matplotlib.pyplot as plt

table=pd.read_csv("BigMartSales.csv")
# print(table)

print("Data Of Table Year 2011")
table_data_2011=table[table['Year'] == 2011]
# print(table_data_2011)
print("Group Data Month Wise for Year 2010")
sales_year_2011_data_monthly = table_data_2011.groupby('Month').sum()['Amount']
print(sales_year_2011_data_monthly)