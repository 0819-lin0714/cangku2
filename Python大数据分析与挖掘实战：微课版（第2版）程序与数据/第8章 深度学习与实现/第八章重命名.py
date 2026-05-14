import os

name_map = {
    "8.3.3.py": "8.3.3 TensorFlow案例.py",
    "8.4.2.py": "8.4.2 多层神经网络分类问题应用举例.py",
    "8.4.3.py": "8.4.3 多层神经网络回归问题应用举例.py",
    "8.5.4.py": "8.5.4 CNN应用案例.py",
    "8.6.3.py": "8.6.3 RNN应用案例.py"
}

for old_name, new_name in name_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✅ {old_name} → {new_name}")
    else:
        print(f"❌ 不存在：{old_name}")