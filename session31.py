#Soccer data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

table=pd.read_csv("soccer.csv")
#print(table)
# print(table.head())
# print(table.Name)

# sb.countplot(x=table.Nationality,palette="Set2")
# sb.countplot(x=table.Age,data=table)
# plt.show()
table["Goal_Score"]=table.GK_Positioning+table.GK_Diving+table.GK_Handling+table.GK_Reflexes
# print(table)

sorted_table=table.sort_values('Goal_Score')
print(sorted_table.tail(10))