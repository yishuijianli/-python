import pandas as pd
# df =pd.read_csv("data.csv",index_col="Name")
df = pd.read_csv("data.csv")
# pokemon=input("请输入要搜索的宝可梦名称:")
water_pokemon = df[df["Type2"]=="Water"]
print(df["Height"].mean())
df["Type1"]=df["Type1"].str.replace("Grass","Grassy")
print(df.to_string())
df["Legendary"]=df["Legendary"].astype(bool)
print(df.to_string())


# 先不设置索引列，查看文件内容
# try:
#     df = pd.read_csv("data.csv")
#     print("文件的列名:")
#     print(df.columns.tolist())
#     print("\n前几行数据:")
#     print(df.head())
# except Exception as e:
#     print(f"读取文件时出错: {e}")