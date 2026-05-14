import os

name_map = {
    "3.2.1.py": "3.2.1 序列创建及访问.py",
    "3.2.2.py": "3.2.2 序列属性.py",
    "3.2.3.py": "3.2.3 序列方法.py",
    "3.2.4.py": "3.2.4 序列切片.py",
    "3.2.5.py": "3.2.5 序列聚合运算.py",
    "3.3.py": "3.3 数据框.py",
    "3.4.py": "3.4 外部文件读取.py"
}

for old_name, new_name in name_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✅ {old_name} → {new_name}")
    else:
        print(f"❌ 不存在：{old_name}")