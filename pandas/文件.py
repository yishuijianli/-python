import pandas as pd
import os

# 检查文件
file_path = "data.csv"
print(f"文件存在: {os.path.exists(file_path)}")
if os.path.exists(file_path):
    print(f"文件大小: {os.path.getsize(file_path)} 字节")

# 读取数据
df = pd.read_csv("data.csv")

# 详细分析数据结构
print("\n=== 数据框基本信息 ===")
print(f"形状: {df.shape} (行数: {df.shape[0]}, 列数: {df.shape[1]})")
print(f"列名列表: {df.columns.tolist()}")

print("\n=== 列名详情 ===")
for i, col in enumerate(df.columns):
    print(f"{i+1}. '{col}' (数据类型: {df[col].dtype})")

print("\n=== 查找类型相关列 ===")
type_columns = []
for col in df.columns:
    if 'type' in col.lower():
        type_columns.append(col)
        print(f"找到类型列: '{col}'")
        print(f"  唯一值: {df[col].unique()}")
        
if not type_columns:
    print("没有找到明确的类型列")
    # 显示所有列的前几个值，帮助识别哪列是类型
    print("\n各列的前几个值:")
    for col in df.columns[:5]:  # 只显示前5列避免输出过多
        print(f"'{col}': {df[col].head(3).tolist()}")

print("\n=== 查找高度相关列 ===")
height_columns = [col for col in df.columns if 'height' in col.lower()]
if height_columns:
    for col in height_columns:
        print(f"找到高度列: '{col}'")
        print(f"  平均值: {df[col].mean()}")
else:
    print("没有找到明确的高度列")
    # 显示数值列
    numeric_cols = df.select_dtypes(include=['number']).columns
    print(f"数值列: {numeric_cols.tolist()}")
    for col in numeric_cols[:3]:  # 只显示前3个数值列
        print(f"  '{col}' 的平均值: {df[col].mean()}")

print("\n=== 数据样本 ===")
print(df.head(3))