import os
# 第1章 精准匹配（文件名完全和你图里一致）
name_map = {
    "1.3.py": "1.3 Python基本数据类型.py",
    "1.4.py": "1.4 Python相关的公有方法.py",
    "1.5.1.py": "1.5.1 列表方法.py",
    "1.5.2.py": "1.5.2 元组方法.py",
    "1.5.3.py": "1.5.3 字符串方法.py",
    "1.6.py": "1.6 字典方法.py",
    "1.7.py": "1.7 条件语句.py",
    "1.8.py": "1.8 循环语句.py",
    "1.9.py": "1.9 函数.py"
}
for old, new in name_map.items():
    if os.path.exists(old):
        os.rename(old, new)
        print(f"✅ {old} → {new}")
    else:
        print(f"❌ 不存在：{old}")