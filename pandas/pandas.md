数据帧表格数据结构

```python
data1 = {'Name': ['Tom', 'Joseph', 'Krish', 'John'],

         'Age': [20, 21, 19, 18],

         'City': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']}

df = pd.DataFrame(data1)

  

# 增加新列

df["an"] = [1, 2, 3, 4]

print("添加列后:")

print(df)

  

# 方法1: 使用 loc 添加新行（按索引）

df.loc[len(df)] = ['Alice', 25, 'Hangzhou', 5]  # 注意有4个值对应4列

print("\n使用 loc 添加行后:")

print(df)

  

# 方法2: 使用 concat 添加新行

new_row = pd.DataFrame([{'Name': 'Bob', 'Age': 30, 'City': 'Nanjing', 'an': 6}])

df = pd.concat([df, new_row], ignore_index=True)

print("\n使用 concat 添加行后:")

print(df)
```
