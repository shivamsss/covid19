import pandas as pd
numbers1 = [10, 20, 30, 40, 50]
numbers2 = [11, 22, 33, 44, 55]


employee1 = {"name": "John", "age": 22, "salary": 30000}
employee2 = {"name": "Fionna", "age": 24, "salary": 35000}
employee3 = {"name": "Dave", "age": 26, "salary": 55000}
employee4 = {"name": "Kim", "age": 32, "salary": 60000, "email":"kima@example.com"}

frame1=pd.DataFrame([numbers1,numbers2])
print(frame1)
frame2=pd.DataFrame([employee1,employee2,employee3,employee4])
print(frame2)

print("  ")

print(frame2["name"])
print(frame1[0][1])
print(" ")
print("Slicing data")
print(frame2[0:2])