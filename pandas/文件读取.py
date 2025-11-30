# import pandas as pd
# df =pd.read_csv("data.csv")
# print(df)
# import pandas as pd
# # 使用文件的完整路径

# df = pd.read_csv("C:/用户/q/Desktop/pandas/data.csv")
# print(df)
import pandas as pd
import os
 #查找列   
df =pd.read_csv("data.csv",index_col="Name")
print(df)
print(df["Name"].to_string())  
print(df.iloc[0:11:2,0:3])
# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(current_dir, "data.csv")

print(f"当前脚本目录: {current_dir}")
print(f"尝试读取文件: {data_file}")

try:
    df = pd.read_csv(data_file)
    print(df)
except FileNotFoundError:
    print("文件未找到，请确认 data.csv 是否在以下位置:")
    print(current_dir)


