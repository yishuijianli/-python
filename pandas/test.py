import pandas as pd

# 直接检查 Kakuna 是否存在
try:
    df = pd.read_csv("data.csv", index_col="Name")
    
    print("=== Kakuna 专项检查 ===")
    print(f"数据集总大小: {len(df)} 个宝可梦")
    
    # 检查各种可能的 Kakuna 写法
    kakuna_variants = [
        "Kakuna",
        "kakuna", 
        "KAKUNA",
        " Kakuna ",
        "Kakuna ",
        " Kakuna"
    ]
    
    print("\n检查常见变体:")
    for variant in kakuna_variants:
        if variant in df.index:
            print(f"✅ 找到: '{variant}'")
        else:
            print(f"❌ 未找到: '{variant}'")
    
    # 显示所有包含 "kuna" 的名称
    print("\n所有包含 'kuna' 的名称:")
    kuna_pokemon = [name for name in df.index if 'kuna' in name.lower()]
    if kuna_pokemon:
        for name in kuna_pokemon:
            print(f"  - {name}")
    else:
        print("  未找到任何包含 'kuna' 的名称")
        
except Exception as e:
    print(f"检查过程中发生错误: {e}")