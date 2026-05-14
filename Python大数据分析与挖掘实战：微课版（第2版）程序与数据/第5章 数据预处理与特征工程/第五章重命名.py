import os

name_map = {
    "5.1.py": "5.1 重复数据处理.py",
    "5.2.1.py": "5.2.1 基于数据框的合并.py",
    "5.2.2.py": "5.2.2 基于数据框的关联.py",
    "5.3.1.py": "5.3.1 时间处理函数.py",
    "5.3.2-5.4.py": "5.3.2-5.4 时间元素提取与映射离散化.py",
    "5.5.1.py": "5.5.1 滚动计算.py",
    "5.5.2.py": "5.5.2 分组统计计算.py",
    "5.7.1.py": "5.7.1 单变量插值填充.py",
    "5.7.2.py": "5.7.2 多变量插值填充.py",
    "5.8.1.py": "5.8.1 均值‑方差规范化.py",
    "5.8.2.py": "5.8.2 极差规范化.py",
    "5.8.3.py": "5.8.3 K最近邻插值填充.py",
    "5.9.py": "5.9 特征组合与特征选择.py",
    "5.10.1.py": "5.10.1 基于主成分分析的特征组合.py",
    "5.10.2.py": "5.10.2 特征选择.py"
}

for old_name, new_name in name_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✅ {old_name} → {new_name}")
    else:
        print(f"❌ 不存在：{old_name}")