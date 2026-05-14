import os

name_map = {
    "4.1.2.py": "4.1.2 Matplotlib绘图基本流程.py",
    "4.1.3.py": "4.1.3 中文字符显示.py",
    "4.1.4.py": "4.1.4 坐标轴字符刻度标注.py",
    "4.2.1.py": "4.2.1 散点图.py",
    "4.2~4.2.6.py": "4.2.2‑4.2.6 常用图形绘制(线/柱/直方/饼/箱线).py",
    "4.2.7.py": "4.2.7 子图.py"
}

for old_name, new_name in name_map.items():
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"✅ {old_name} → {new_name}")
    else:
        print(f"❌ 不存在：{old_name}")