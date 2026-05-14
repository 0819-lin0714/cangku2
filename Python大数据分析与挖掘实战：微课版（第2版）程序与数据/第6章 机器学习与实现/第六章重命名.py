import os

name_map = {
    "6.1.py": "6.1 线性回归.py",
    "6.2.py": "6.2 逻辑回归.py",
    "6.3.3.py": "6.3.3 Python神经网络分类应用举例.py",
    "6.3.4.py": "6.3.4 Python神经网络回归应用举例.py",
    "6.4.py": "6.4 支持向量机.py",
    "6.5.1.py": "6.5.1 K‑均值聚类的基本原理.py",
    "6.5.2.py": "6.5.2 Python K‑均值聚类算法应用举例.py",
    "6.6.3.py": "6.6.3 一对一关联规则挖掘及Python实现.py"
}

for old_name, new_name in name_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✅ {old_name} → {new_name}")
    else:
        print(f"❌ 不存在：{old_name}")