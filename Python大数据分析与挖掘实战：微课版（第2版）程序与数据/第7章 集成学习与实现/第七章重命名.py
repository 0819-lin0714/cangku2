import os

name_map = {
    "7.2.3.1.py": "7.2.3.1 Bagging算法的Sklearn实现.py",
    "7.2.3.2.py": "7.2.3.2 Bagging算法的应用举例.py",
    "7.3.3.1.py": "7.3.3.1 随机森林算法的Sklearn实现.py",
    "7.3.3.2.py": "7.3.3.2 Python随机森林算法的应用举例.py",
    "7.5.3.1.py": "7.5.3.1 AdaBoost算法的Sklearn实现.py",
    "7.5.3.2.py": "7.5.3.2 AdaBoost算法的应用举例.py",
    "7.6.3.1.py": "7.6.3.1 GBDT算法的Sklearn实现.py",
    "7.6.3.2.py": "7.6.3.2 GBDT算法的应用举例.py",
    "7.7.3.1.py": "7.7.3.1 XGBoost算法的Sklearn实现.py",
    "7.7.3.2.py": "7.7.3.2 XGBoost算法的应用举例.py"
}

for old_name, new_name in name_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✅ {old_name} → {new_name}")
    else:
        print(f"❌ 不存在：{old_name}")