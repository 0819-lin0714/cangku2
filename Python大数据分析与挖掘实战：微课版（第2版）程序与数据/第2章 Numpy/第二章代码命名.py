import os

name_map = {
    "2.1.py": "2.1 NumPy简介.py",
    "2.2.py": "2.2 创建数组.py",
    "2.3.py": "2.3 数组尺寸.py",
    "2.4.py": "2.4 数组运算.py",
    "2.5.py": "2.5 数组切片.py",
    "2.6.py": "2.6 数组连接.py",
    "2.7.py": "2.7 数据存取.py",
    "2.8.py": "2.8 数组形态变换.py",
    "2.9.py": "2.9 数组排序与搜索.py",
    "2.10.py": "2.10 矩阵与线性代数运算.py"
}

for old_name, new_name in name_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✅ {old_name} → {new_name}")
    else:
        print(f"❌ 不存在：{old_name}")