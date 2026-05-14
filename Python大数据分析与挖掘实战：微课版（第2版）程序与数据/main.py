import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from io import BytesIO


# 设置中文字体
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 读取代码文件
# 读取代码文件
def read_code(file_path):
    try:
        if file_path.startswith("1."):
            full_path = os.path.join("第1章 Python基础知识", file_path)
        elif file_path.startswith("2."):
            full_path = os.path.join("第2章 Numpy", file_path)
        elif file_path.startswith("3."):
            full_path = os.path.join("第3章 Pandas", file_path)
        elif file_path.startswith("4."):
            full_path = os.path.join("第4章 Matplotlib", file_path)
        elif file_path.startswith("5."):
            full_path = os.path.join("第5章 数据预处理与特征工程", file_path)
        elif file_path.startswith("6."):
            full_path = os.path.join("第6章 机器学习与实现", file_path)
        elif file_path.startswith("7."):
            full_path = os.path.join("第7章 集成学习与实现", file_path)
        elif file_path.startswith("8."):
            full_path = os.path.join("第8章 深度学习与实现", file_path)
        else:
            full_path = file_path
            
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"无法找到文件: {full_path}"
    except Exception as e:
        return f"读取文件出错: {str(e)}"

# 页面配置
st.set_page_config(page_title="Python&Numpy基础实验平台", layout='wide')

# 侧边栏 - 章节选择
with st.sidebar:
    st.subheader('请选择章节和实验')
    
    chapters = {
        "第一章：Python基础知识": [
            "1.3.py (基本数据类型)",
            "1.4.py (索引与切片、长度/最值/包含判断)",
            "1.5.1.py (列表操作)",
            "1.5.2.py (元组操作)",
            "1.5.3.py (字符串操作)",
            "1.6.py (字典操作)",
            "1.7.py (条件判断)",
            "1.8.py (循环结构)",
            "1.9.py (函数定义与调用)"
        ],
        "第二章：Numpy数值计算": [
            "2.1.py (数组创建)",
            "2.2.py (多类型数据转数组、特殊数组生成)",
            "2.3.py (数组维度与形状)",
            "2.4.py (数组算术运算)",
            "2.5.py (数组索引与切片)",
            "2.6.py (数组拼接)",
            "2.7.py (数组保存与加载)",
            "2.8.py (数组形状变换)",
            "2.9.py (数组排序与极值索引)",
            "2.10.py (矩阵操作)"
        ],
        "第三章：Pandas基础实战": [
            "3.2.1.py (Series创建)",
            "3.2.2.py (Series值与索引)",
            "3.2.3.py (去重、判空、统计)",
            "3.2.4.py (索引与筛选)",
            "3.2.5.py (描述性统计)",
            "3.3.py (DataFrame基础操作)",
            "3.4.py (数据读取与分析)"
        ],
        "第四章：Matplotlib数据可视化": [
            "4.1.2.py (子图与函数曲线)",
            "4.1.3.py (正弦曲线)",
            "4.1.4.py (季度销售额折线图)",
            "4.2.1.py (D02车次散点图)",
            "4.2.2~4.2.6.py (多图独立绘制)",
            "4.2.7.py (子图组合：6图合一)"
        ],
        "第五章：数据预处理与特征工程": [
            "5.1.py (重复值处理)",
            "5.2.1.py (数据合并concat)",
            "5.2.2.py (数据连接merge)",
            "5.3.1.py (时间类型转换)",
            "5.3.2-5.4.py (时间提取与数据分箱)",
            "5.5.1.py (滑动窗口计算)",
            "5.5.2.py (分组聚合与transform)",
            "5.7.1.py (SMOTE过采样)",
            "5.7.2.py (随机下采样)",
            "5.8.1.py (简单填充SimpleImputer)",
            "5.8.2.py (迭代填充IterativeImputer)",
            "5.8.3.py (KNN近邻填充)",
            "5.9.py (标准化与归一化)",
            "5.10.1.py (PCA主成分分析)",
            "5.10.2.py (特征选择方法)"
        ],
        
        "第六章：机器学习与实现": [
            "6.1.py (线性回归)",
            "6.2.py (逻辑回归分类)",
            "6.3.3.py (神经网络分类)",
            "6.3.4.py (神经网络回归)",
            "6.4.py (支持向量机SVM)",
            "6.5.1.py (K-Means手动实现)",
            "6.5.2.py (K-Means库调用)",
            "6.6.3.py (关联规则挖掘)"
        ],
    
        "第七章：集成学习与实现": [
            "7.2.3.1.py (Bagging算法的应用举例(1))",
            "7.2.3.2.py (Bagging算法的应用举例(2))",
            "7.3.3.1.py (Python随机森林算法的应用举例(1))",
            "7.3.3.2.py (Python随机森林算法的应用举例(2))",
            "7.5.3.1.py (AdaBoost算法的应用举例(1))",
            "7.5.3.2.py (AdaBoost算法的应用举例(2))",
            "7.6.3.1.py (GBDT算法的应用举例(1))",
            "7.6.3.2.py (GBDT算法的应用举例(2))",
            "7.7.3.1.py (XGBOOST算法的应用举例(1))",
            "7.7.3.2.py (2XGBOOST算法的应用举例(2))"
        ],
        "第八章：深度学习与实现": [
            "8.3.3.py (tensorflow案例)",
            "8.4.2.py (MLP-MNIST案例)",
            "8.4.3.py (MLP-MPG分类问题)",
            "8.5.4.py (CNN-Cifar10案例)",
            "8.6.3.py (RNN-IMDB案例)"
        ]
    }
    
    selected_chapter = st.selectbox("选择章节", list(chapters.keys()))
    selected_experiment = st.selectbox("选择实验", chapters[selected_chapter])

current_file = selected_experiment.split(' ')[0]

st.markdown(f"### {selected_chapter} - {selected_experiment}")
st.markdown("---")

def check_empty(data):
    if isinstance(data, (pd.DataFrame, pd.Series)) and data.empty:
        st.warning("当前数据为空，请检查数据源！")
        return True
    if isinstance(data, list) and len(data) == 0:
        st.warning("当前数据为空，请检查数据源！")
        return True
    if isinstance(data, np.ndarray) and data.size == 0:
        st.warning("当前数据为空，请检查数据源！")
        return True
    return False

st.subheader('📝 实验代码')
code_content = read_code(current_file)
with st.container(height=400):
    st.code(code_content, language='python', line_numbers=True)

run_btn = st.button('▶️ 运行代码', type='primary')

if run_btn:
    st.markdown("---")
    st.subheader('📊 运行结果')
    try:
        # ---------------- 第一章：Python基础知识 ----------------
        if selected_chapter == "第一章：Python基础知识":
            if current_file == "1.3.py":
                st.subheader("基本数据类型展示")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("#### 数值类型")
                    n1=2
                    n2=1.3
                    n3=float(2)
                    t=True
                    f=False
                    st.write(f"整型n1: {n1}, 浮点n2: {n2}, 浮点转换n3: {n3}")
                    st.write(f"布尔t: {t} (等价于1: {t==1}), 布尔f: {f} (等价于0: {f==0})")
                with col2:
                    st.write("#### 序列类型（列表/元组）")
                    L1=[1,2,3,4,5,6]
                    L2=[1,2,'HE',3,5]
                    t1=(1,2,3,4,6)
                    t2=(1,2,'kl')
                    st.write("列表L1:", L1)
                    st.write("混合列表L2:", L2)
                    st.write("元组t1:", t1)
                    st.write("混合元组t2:", t2)
                with col3:
                    st.write("#### 集合&字典类型")
                    J1={1,'h',2,3,9}
                    J2={1,'h',2,3,9,2}
                    d1={1:'h',2:[1,2,'k'],3:9}
                    d2={'a':2,'b':'ky'}
                    st.write("集合J1 (自动去重):", J1)
                    st.write("集合J2 (重复元素已去重):", J2)
                    st.write("字典d1 (混合值类型):", d1)
                    st.write("字典d2 (字符串键):", d2)

            elif current_file == "1.4.py":
                st.subheader("索引/切片/长度/最值/包含判断")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 索引与切片")
                    s3='I Like python'
                    L2=[1,2,'HE',3,5]
                    t2=(1,2,'kl')
                    st.write(f"字符串s3: {s3}")
                    st.write(f"s3[0:4]: {s3[0:4]}, s3[1:6:2]: {s3[1:6:2]}")
                    st.write(f"列表L2: {L2}")
                    st.write(f"L2[1:3]: {L2[1:3]}, L2[2:]: {L2[2:]}")
                    st.write(f"元组t2: {t2}")
                    st.write(f"t2[0:2]: {t2[0:2]}, t2[:]: {t2[:]}")
                with col2:
                    st.write("#### 长度/最值/包含判断")
                    s3='I Like python'
                    L1=[1,2,3,4,5,6]
                    t1=(1,2,3,4,6)
                    J2={1,'h',2,3,9,'SE'}
                    st.write(f"s3长度: {len(s3)}, 最大值字符: {max(s3)}")
                    st.write(f"L1长度: {len(L1)}, 最大值: {max(L1)}, 最小值: {min(L1)}, 求和: {sum(L1)}")
                    st.write(f"t1长度: {len(t1)}, 最大值: {max(t1)}, 求和: {sum(t1)}")
                    st.write(f"J2长度: {len(J2)}, 'SE'是否在J2中: {'SE' in J2}")
                    st.write(f"'I'是否在s3中: {'I' in s3}, 2是否在t1中: {2 in t1}")

            elif current_file == "1.5.1.py":
                st.subheader("列表操作演示")
                L1=[1,2,3,4,5,6]
                L2=[1,2,'HE',3,5]
                L4=[1,4,2,3,8,4,7]
                L=[]
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 增/查操作")
                    L1.append('H')
                    st.write(f"L1追加'H'后: {L1}")
                    for t in L2:
                        L.append(t)
                    st.write(f"空列表L添加L2元素后: {L}")
                    L1.extend(L2)
                    st.write(f"L1扩展L2后: {L1}")
                    st.write(f"元素2在L1中出现次数: {L1.count(2)}")
                    st.write(f"'H'在L1中的索引: {L1.index('H')}")
                with col2:
                    st.write("#### 删/改/排序")
                    st.write(f"删除前L1: {L1}")
                    L1.remove('HE')
                    st.write(f"删除'HE'后L1: {L1}")
                    st.write(f"排序前L4: {L4}")
                    L4.sort()
                    st.write(f"排序后L4: {L4}")
                    L4[2]=10
                    st.write(f"L4修改索引2为10后: {L4}")
                    t=(1,2,3,4)
                    st.warning(f"元组t={t} 不可修改（t[2]=10会报错）")

            elif current_file == "1.5.2.py":
                st.subheader("元组操作演示")
                T1=(1,2,2,4,5)
                T2=('H2',3,'KL')
                t1=tuple()
                t=()
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 空元组&基础操作")
                    st.write(f"空元组t1: {t1}, 空元组t: {t}")
                    st.write(f"元组T1: {T1}")
                    st.write(f"元素2在T1中出现次数: {T1.count(2)}")
                    st.write(f"元组T2: {T2}")
                    st.write(f"'KL'在T2中的索引: {T2.index('KL')}")
                with col2:
                    st.write("#### 元组拼接")
                    T3=T1+T2
                    st.write(f"T1 + T2 = {T3}")
                    fig, ax = plt.subplots(figsize=(8, 4))
                    ax.hist([i for i in T1 if isinstance(i, int)], bins=5, alpha=0.7, label='T1数值元素')
                    ax.set_title('T1元组数值元素分布')
                    ax.set_xlabel('元素值')
                    ax.set_ylabel('频数')
                    st.pyplot(fig)

            elif current_file == "1.5.3.py":
                st.subheader("字符串操作演示")
                text_str = 'hello word!'
                str11 = 'joh'
                str1 = 'jo'
                str2 = 'qb'
                str3 = 'qb'
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 查找&替换")
                    z1 = text_str.find('he',0,len(text_str))
                    z2 = text_str.find('he',1,len(text_str))
                    st.write(f"字符串text_str: {text_str}")
                    st.write(f"查找'he'(0到末尾): {z1}")
                    st.write(f"查找'he'(1到末尾): {z2}")
                    stt = text_str.replace('or','kl')
                    st.write(f"替换后: {stt} (原字符串不变: {text_str})")
                with col2:
                    st.write("#### 拼接&比较")
                    st2 = str11 + ' ' + text_str
                    st.write(f"str11 + text_str = {st2}")
                    s1 = str1 != str2
                    s2 = str2 == str3
                    st.write(f"str1 != str2: {s1}")
                    st.write(f"str2 == str3: {s2}")

            elif current_file == "1.6.py":
                st.subheader("字典操作演示")
                d=dict()
                D={}
                list1=[('a','ok'),('1','lk'),('001','lk')]
                list2=[['a','ok'],['b','lk'],[3,'lk']]
                d1=dict(list1)
                d2=dict(list2)
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 字典创建")
                    st.write(f"空字典d: {d}")
                    st.write(f"空字典D: {D}")
                    st.write(f"从元组列表list1创建d1: {d1}")
                    st.write(f"从列表列表list2创建d2: {d2}")
                with col2:
                    st.write("#### 取值&默认值")
                    st.write(f"d2.get('b'): {d2.get('b')}")
                    d.setdefault('a',0)
                    D.setdefault('b',[1,2,3,4,5])
                    st.write(f"d设置默认值'a':0后: {d}")
                    st.write(f"D设置默认值'b':[1,2,3,4,5]后: {D}")

            elif current_file == "1.7.py":
                st.subheader("条件判断演示")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("#### 单条件判断（正数平方根）")
                    x=10
                    import math
                    if x>0:
                        s=math.sqrt(x)
                        st.write(f"x={x} > 0，平方根s={s:.2f}")
                with col2:
                    st.write("#### 双条件判断（负数提示）")
                    x=-10
                    if x>0:
                        s=math.sqrt(x)
                        st.write(f"x={x} > 0，平方根s={s:.2f}")
                    else:
                        s='负数不能求平方根'
                        st.write(f"x={x}，{s}")
                with col3:
                    st.write("#### 多条件判断（天气场景）")
                    weather = 'sunny'
                    st.write(f"当前天气: {weather}")
                    if weather =='sunny':
                        st.write("执行操作：shopping")
                    elif weather =='cloudy':
                        st.write("执行操作：playing football")
                    else:
                        st.write("执行操作：do nothing")
                    weather_input = st.selectbox("修改天气", ['sunny', 'cloudy', 'rainy'])
                    if weather_input =='sunny':
                        st.write(f"天气{weather_input} → shopping")
                    elif weather_input =='cloudy':
                        st.write(f"天气{weather_input} → playing football")
                    else:
                        st.write(f"天气{weather_input} → do nothing")

            elif current_file == "1.8.py":
                st.subheader("循环结构演示")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### while循环（100累加）")
                    t = 100
                    s = 0
                    while t:
                        s=s+t
                        t=t-1
                    st.write(f"1+2+...+100 = {s}")
                with col2:
                    st.write("#### for循环（列表填充）")
                    list1=list()
                    list2=list()
                    list3=list()
                    for a in range(10):
                        list1.append(a)
                    for t in ['a','b','c','d']:
                        list2.append(t)
                    for q in ('k','j','p'):
                        list3.append(q)
                    st.write(f"range(10)填充list1: {list1}")
                    st.write(f"字符串列表填充list2: {list2}")
                    st.write(f"元组元素填充list3: {list3}")

            elif current_file == "1.9.py":
                st.subheader("函数定义与调用演示")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 无返回值函数（累加）")
                    def sumt(t):
                        s = 0
                        while t:
                           s=s+t
                           t=t-1
                    s=sumt(50)
                    st.write(f"sumt(50) 无返回值 → s={s} (None)")
                    st.write("#### 有返回值函数（累加）")
                    def sumt(t):
                        s = 0
                        while t:
                           s=s+t
                           t=t-1
                        return s
                    s=sumt(50)
                    st.write(f"sumt(50) 有返回值 → s={s}")
                with col2:
                    st.write("#### 多返回值函数（圆的面积/周长）")
                    def test(r):
                        import math
                        s=math.pi*r**2
                        c=2*math.pi*r
                        L=(s,c)
                        D=[s,c,L]
                        return (s,c,L,D)
                    v=test(10)
                    s=v[0]
                    c=v[1]
                    L=v[2]
                    D=v[3]
                    st.write(f"半径r=10:")
                    st.write(f"面积s={s:.2f}")
                    st.write(f"周长c={c:.2f}")
                    st.write(f"元组L={L}")
                    st.write(f"列表D={D}")
                    r_input = st.slider("修改圆的半径", 1, 20, 10)
                    v2=test(r_input)
                    st.write(f"半径{r_input} → 面积={v2[0]:.2f}, 周长={v2[1]:.2f}")

        # ---------------- 第二章：Numpy数值计算 ----------------
        elif selected_chapter == "第二章：Numpy数值计算":
            if current_file == "2.1.py":
                st.subheader("Numpy数组创建（列表转数组）")
                col1, col2 = st.columns(2)
                with col1:
                    L=[[1,2],[3,4]]
                    A=np.array(L)
                    st.write(f"原始嵌套列表L: {L}")
                    st.write(f"转换为numpy数组A:\n{A}")
                    st.write(f"数组A的类型: {type(A)}, 形状: {A.shape}")
                with col2:
                    L=[[1,2],[3,4]]
                    A=np.array(L)
                    st.write(f"简化导入（import numpy as np）:")
                    st.write(f"数组A:\n{A}")
                    st.write(f"数组A的维度: {A.ndim}, 元素类型: {A.dtype}")

            elif current_file == "2.2.py":
                st.subheader("多类型数据转数组 + 特殊数组生成")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 多类型数据转数组")
                    d1=[1,2,3,4,0.1,7]
                    d2=(1,2,3,4,2.3)
                    d3=[[1,2,3,4],[5,6,7,8]]
                    import numpy as np
                    d11=np.array(d1)
                    d21=np.array(d2)
                    d31=np.array(d3)
                    st.write(f"列表d1转数组d11:\n{d11} (形状: {d11.shape})")
                    st.write(f"元组d2转数组d21:\n{d21} (形状: {d21.shape})")
                    st.write(f"嵌套列表d3转数组d31:\n{d31} (形状: {d31.shape})")
                with col2:
                    st.write("#### 特殊数组生成")
                    z1=np.ones((3,3))
                    z2=np.zeros((3,4))
                    z3=np.arange(10)
                    z4= np.arange(2,10)
                    z5= np.arange(2,10,2)
                    st.write(f"3x3全1数组z1:\n{z1}")
                    st.write(f"3x4全0数组z2:\n{z2}")
                    st.write(f"arange(10): {z3}")
                    st.write(f"arange(2,10): {z4}")
                    st.write(f"arange(2,10,2): {z5}")

            elif current_file == "2.3.py":
                st.subheader("数组维度与形状查看")
                d1=[1,2,3,4,0.1,7]
                d3=[[1,2,3,4],[5,6,7,8]]
                d11=np.array(d1)
                d31=np.array(d3)
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 一维数组属性")
                    st.write(f"一维数组d11:\n{d11}")
                    st.write(f"形状shape: {d11.shape}")
                    st.write(f"维度ndim: {d11.ndim}")
                    st.write(f"元素个数size: {d11.size}")
                    st.write(f"元素类型dtype: {d11.dtype}")
                with col2:
                    st.write("#### 二维数组属性")
                    st.write(f"二维数组d31:\n{d31}")
                    st.write(f"形状shape: {d31.shape} (行×列)")
                    st.write(f"维度ndim: {d31.ndim}")
                    st.write(f"元素个数size: {d31.size}")
                    st.write(f"元素类型dtype: {d31.dtype}")

            elif current_file == "2.4.py":
                st.subheader("数组算术运算 + 数学函数")
                A=np.array([[1,2],[3,4]])
                B=np.array([[5,6],[7,8]])
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 数组基本运算")
                    st.write("数组A:\n", A)
                    st.write("数组B:\n", B)
                    st.write("A - B:\n", A-B)
                    st.write("A + B:\n", A+B)
                    st.write("A * B (元素乘):\n", A*B)
                    st.write("A / B (元素除):\n", np.round(A/B, 2))
                with col2:
                    st.write("#### 广播运算 + 数学函数")
                    C8=np.array([1,2,3,3.1,4.5,6,7,8,9])
                    C9=(C8-min(C8))/(max(C8)-min(C8))
                    D=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
                    st.write(f"A / 3:\n{np.round(A/3, 2)}")
                    st.write(f"A²:\n{A**2}")
                    st.write(f"C8极差化后C9:\n{np.round(C9, 2)}")
                    st.write(f"D平方根:\n{np.round(np.sqrt(D), 2)}")
                    st.write(f"D正弦值:\n{np.round(np.sin(D), 2)}")

            elif current_file == "2.5.py":
                st.subheader("数组索引与切片（逻辑索引 + ix_函数）")
                D=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 基础索引&逻辑索引")
                    st.write("原始数组D:\n", D)
                    st.write(f"D[1,2] (第2行第3列): {D[1,2]}")
                    st.write(f"D[:,[1,3]] (第2、4列):\n{D[:,[1,3]]}")
                    st.write(f"D[[1,3],:] (第2、4行):\n{D[[1,3],:]}")
                    st.write(f"D[D[:,0]>5,:] (第1列>5的行):\n{D[D[:,0]>5,:]}")
                    TF=[True,False,False,True]
                    st.write(f"D[TF,:] (逻辑索引第1、4行):\n{D[TF,:]}")
                    st.write(f"D[D>4] (所有>4的元素):\n{D[D>4]}")
                with col2:
                    st.write("#### ix_函数（多维索引）")
                    D=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
                    D3=D[np.ix_([1,2],[1,3])]
                    D4=D[np.ix_(np.arange(2),[1,3])]
                    D6=D[np.ix_(D[:,1]<11,[1,2])]
                    TF=[True,False,False,True]
                    D8=D[np.ix_(TF,[2])]
                    st.write(f"D[np.ix_([1,2],[1,3])] (行1-2,列1-3):\n{D3}")
                    st.write(f"D[np.ix_(np.arange(2),[1,3])] (行0-1,列1-3):\n{D4}")
                    st.write(f"D[np.ix_(D[:,1]<11,[1,2])] (第2列<11的行,列1-2):\n{D6}")
                    st.write(f"D[np.ix_(TF,[2])] (逻辑行,列2):\n{D8}")

            elif current_file == "2.6.py":
                st.subheader("数组拼接（水平/垂直）")
                A=np.array([[1,2],[3,4]])
                B=np.array([[5,6],[7,8]])
                C_s=np.hstack((A,B))
                C_v=np.vstack((A,B))
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 水平拼接（hstack）")
                    st.write("数组A:\n", A)
                    st.write("数组B:\n", B)
                    st.write("水平拼接C_s (列数增加):\n", C_s)
                    st.write(f"A形状: {A.shape}, B形状: {B.shape}, C_s形状: {C_s.shape}")
                with col2:
                    st.write("#### 垂直拼接（vstack）")
                    st.write("垂直拼接C_v (行数增加):\n", C_v)
                    st.write(f"C_v形状: {C_v.shape}")
                    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
                    ax1.imshow(C_s, cmap='Blues')
                    ax1.set_title('水平拼接 C_s')
                    ax2.imshow(C_v, cmap='Reds')
                    ax2.set_title('垂直拼接 C_v')
                    st.pyplot(fig)

            elif current_file == "2.7.py":
                st.subheader("数组保存与加载（npy格式）")
                import os
                A=np.array([[1,2],[3,4]])
                B=np.array([[5,6],[7,8]])
                C_s=np.hstack((A,B))
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 保存数组")
                    st.write("待保存数组C_s:\n", C_s)
                    np.save('data.npy', C_s)
                    st.success("数组已保存到 data.npy")
                    if os.path.exists('data.npy'):
                        st.write(f"文件大小: {os.path.getsize('data.npy')} 字节")
                with col2:
                    st.write("#### 加载数组")
                    C_s_loaded = np.load('data.npy')
                    st.write("加载后的数组C_s:\n", C_s_loaded)
                    if np.array_equal(C_s, C_s_loaded):
                        st.success("加载的数组与原数组完全一致！")
                    else:
                        st.error("加载的数组与原数组不一致！")

            elif current_file == "2.8.py":
                st.subheader("数组形状变换（reshape/ravel）")
                arr = np.arange(12)
                arr1 = arr.reshape(3, 4)
                arr2 = arr1.ravel()
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### reshape（改变形状）")
                    st.write(f"原始一维数组arr: {arr} (形状: {arr.shape})")
                    st.write(f"reshape(3,4)后arr1:\n{arr1} (形状: {arr1.shape})")
                    rows = st.slider("设置reshape行数", 1, 12, 3)
                    if 12 % rows == 0:
                        arr_custom = arr.reshape(rows, 12//rows)
                        st.write(f"reshape({rows}, {12//rows})后:\n{arr_custom}")
                    else:
                        st.warning(f"无法将12个元素转为{rows}行（12%{rows}≠0）")
                with col2:
                    st.write("#### ravel（展平数组）")
                    st.write(f"二维数组arr1:\n{arr1}")
                    st.write(f"ravel()展平后arr2: {arr2} (形状: {arr2.shape})")
                    arr3 = arr1.flatten()
                    st.write(f"flatten()展平后arr3: {arr3}")
                    st.info("ravel()是视图（浅拷贝），flatten()是深拷贝")

            elif current_file == "2.9.py":
                st.subheader("数组排序与极值索引")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 一维数组排序&极值索引")
                    arr = np.array([5,2,3,3,1,9,8,6,7])
                    arr1=np.sort(arr)
                    st.write(f"原始数组: {arr}")
                    st.write(f"排序后: {arr1}")
                    arr = np.array([5,2,3,3,1,1,9,8,6,7,8,8])
                    maxindex=np.argmax(arr)
                    minindex=np.argmin(arr)
                    st.write(f"数组: {arr}")
                    st.write(f"最大值索引: {maxindex} (值: {arr[maxindex]})")
                    st.write(f"最小值索引: {minindex} (值: {arr[minindex]})")
                with col2:
                    st.write("#### 二维数组极值索引")
                    arr = np.array([5,2,3,3,1,1,9,8,6,7,8,8])
                    arr1=arr.reshape(3,4)
                    st.write(f"3x4数组arr1:\n{arr1}")
                    maxindex1=np.argmax(arr1,axis=0)
                    minindex1=np.argmin(arr1,axis=1)
                    st.write(f"各列最大值索引(axis=0): {maxindex1}")
                    st.write(f"各行最小值索引(axis=1): {minindex1}")
                    fig, ax = plt.subplots(figsize=(8, 4))
                    ax.plot(np.sort(arr), marker='o', label='排序后')
                    ax.plot(arr, label='原始', alpha=0.5)
                    ax.set_title('数组排序对比')
                    ax.legend()
                    st.pyplot(fig)

            elif current_file == "2.10.py":
                st.subheader("矩阵操作（转置/逆/线性代数）")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("#### 矩阵基础操作（转置/共轭/逆）")
                    mat = np.matrix(np.arange(4).reshape(2, 2))
                    st.write(f"原始矩阵mat:\n{mat}")
                    st.write(f"转置mat.T:\n{mat.T}")
                    st.write(f"共轭转置mat.H:\n{mat.H}")
                    st.write(f"逆矩阵mat.I:\n{np.round(mat.I, 2)}")
                    mat1 = np.mat("1 2 3; 4 5 6; 7 8 9")
                    mat2 = mat1*3
                    st.write(f"mat1*3:\n{mat2}")
                    st.write(f"mat1+mat2:\n{mat1+mat2}")
                    st.write(f"mat1*mat2 (矩阵乘):\n{mat1*mat2}")
                    st.write(f"multiply(mat1,mat2) (元素乘):\n{np.multiply(mat1, mat2)}")
                with col2:
                    st.write("#### 线性代数运算")
                    mat = np.mat('1 1 1; 1 2 3; 1 3 6')
                    inverse = np.linalg.inv(mat)
                    A=np.dot(mat, inverse)
                    st.write(f"矩阵mat:\n{mat}")
                    st.write(f"逆矩阵inverse:\n{np.round(inverse, 2)}")
                    st.write(f"mat×inverse (单位矩阵):\n{np.round(A, 2)}")
                    A = np.mat("1,-1,1; 2,1,0; 2,1,-1")
                    b = np.array([4, 3, -1])
                    x = np.linalg.solve(A, b)
                    st.write(f"线性方程组Ax=b的解x: {np.round(x, 2)}")
                    A = np.matrix([[1, 0, 2], [0, 3, 0], [2, 0, 1]])
                    A_value, A_vector = np.linalg.eig(A)
                    st.write(f"矩阵A的特征值: {np.round(A_value, 2)}")

        # ---------------- 第三章：Pandas ----------------
        elif selected_chapter == "第三章：Pandas基础实战":
            if current_file == "3.2.1.py":
                st.subheader("Series序列创建")
                s1 = pd.Series([1,-2,2.3,'hq'])
                s2 = pd.Series([1,-2,2.3,'hq'], index=['a','b','c','d'])
                s3 = pd.Series((1,2,3,4,'hq'))
                s4 = pd.Series(np.array([1,2,4,7.1]))
                mydict = {'red':2000,'blue':1000,'yellow':500}
                ss = pd.Series(mydict)
                col1, col2 = st.columns(2)
                with col1:
                    st.write("s1（默认索引）：", s1)
                    st.write("s2（自定义索引）：", s2)
                with col2:
                    st.write("s3（元组创建）：", s3)
                    st.write("s4（数组创建）：", s4)
                    st.write("字典创建ss：", ss)

            elif current_file == "3.2.2.py":
                st.subheader("Series值与索引获取")
                s1 = pd.Series([1,-2,2.3,'hq'])
                va1 = s1.values
                in1 = s1.index
                va2 = list(va1)
                in2 = list(in1)
                st.write("序列s1：", s1)
                st.write("值values：", va1)
                st.write("索引index：", in1)
                st.write("值转列表：", va2)
                st.write("索引转列表：", in2)

            elif current_file == "3.2.3.py":
                st.subheader("去重、判空、值计数")
                s5 = pd.Series([1,2,2,3,'hq','hq','he'])
                st.write("原始序列：", s5)
                st.write("去重unique()：", s5.unique())
                st.write("值统计value_counts()：", s5.value_counts())
                st.write("判断是否在[0,'he']：", s5.isin([0,'he']))
                ss1 = pd.Series([10,'hq',60,np.nan,20])
                st.write("含空值序列：", ss1)
                st.write("非空数据（~isnull）：", ss1[~ss1.isnull()])
                st.write("非空数据（notnull）：", ss1[ss1.notnull()])
                st.write("非空数据（dropna）：", ss1.dropna())

            elif current_file == "3.2.4.py":
                st.subheader("Series索引与筛选")
                s1 = pd.Series([1,-2,2.3,'hq'])
                s2 = pd.Series([1,-2,2.3,'hq'], index=['a','b','c','d'])
                s4 = pd.Series(np.array([1,2,4,7.1]))
                col1, col2 = st.columns(2)
                with col1:
                    st.write("s2[['a','d']]：", s2[['a','d']])
                    st.write("s1[0:2]：", s1[0:2])
                    st.write("s1[[0,2,3]]：", s1[[0,2,3]])
                with col2:
                    st.write("s4[s4>2]：", s4[s4>2])

            elif current_file == "3.2.5.py":
                st.subheader("描述性统计")
                s = pd.Series([1,2,4,5,6,7,8,9,10])
                st.write("序列：", s)
                st.write("求和sum：", s.sum())
                st.write("均值mean：", round(s.mean(),2))
                st.write("标准差std：", round(s.std(),2))
                st.write("最大值max：", s.max())
                st.write("最小值min：", s.min())

            elif current_file == "3.3.py":
                st.subheader("DataFrame 基础操作")
                data = {'a':[2,2,np.nan,5,6],'b':['kl','kl','kl',np.nan,'kl'],'c':[4,6,5,np.nan,6],'d':[7,9,np.nan,9,8]}
                df = pd.DataFrame(data)
                st.write("原始数据：")
                st.dataframe(df)
                st.write("删除空值dropna：")
                st.dataframe(df.dropna())
                st.write("填充0 fillna(0)：")
                st.dataframe(df.fillna(0))
                data2 = {'a':[5,3,4,1,6],'b':['d','c','a','e','q'],'c':[4,6,5,5,6]}
                Df = pd.DataFrame(data2)
                st.write("排序后：")
                st.dataframe(Df.sort_values('a', ascending=False))

            elif current_file == "3.4.py":
                st.subheader("Excel数据读取与分析")
                excel_path = "第3章 Pandas/一、车次上车人数统计表.xlsx"
                try:
                    df = pd.read_excel(excel_path)
                    st.write("数据预览：")
                    st.dataframe(df.head(10))
                    st.write("各车次总人数统计：")
                    res = df.groupby("车次")["上车人数"].sum().sort_values(ascending=False)
                    st.dataframe(res)
                    fig, ax = plt.subplots(figsize=(10,5))
                    res.plot(kind='bar', ax=ax, color='#5b9bd5')
                    ax.set_title("各车次总上车人数")
                    st.pyplot(fig)
                except Exception as e:
                    st.warning(f"未找到数据文件：{excel_path}")
                    st.error(f"错误信息：{str(e)}")

        # ---------------- 第四章：Matplotlib ----------------
        elif selected_chapter == "第四章：Matplotlib数据可视化":
            excel_path = "第4章 Matplotlib/一、车次上车人数统计表.xlsx"
            try:
                df_train = pd.read_excel(excel_path)
            except:
                df_train = pd.DataFrame({'车次':['D02','D03'],'上车人数':[100,200]})

            if current_file == "4.1.2.py":
                st.subheader("子图绘制 y=x 与 y=x²")
                plt.figure(figsize=(8, 5))
                x = np.linspace(0, 1, 1000)
                plt.subplot(2, 1, 1)
                plt.title('y=x^2 & y=x')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.xlim(0, 1)
                plt.ylim(0, 1)
                plt.plot(x, x**2)
                plt.plot(x, x)
                plt.legend(['y=x^2', 'y=x'])
                plt.tight_layout()
                st.pyplot(plt.gcf())

            elif current_file == "4.1.3.py":
                st.subheader("正弦函数 sin 曲线")
                x = np.arange(0, 10, 0.2)
                y = np.sin(x)
                plt.figure(figsize=(8, 4))
                plt.title('sin曲线')
                plt.plot(x, y)
                st.pyplot(plt.gcf())

            elif current_file == "4.1.4.py":
                st.subheader("季度销售额折线图")
                x = np.array([1,2,3,4,5,6,7,8])
                y = np.array([100,104,106,95,103,105,115,100])
                v = ['2018Q1','2018Q2','2018Q3','2018Q4','2019Q1','2019Q2','2019Q3','2019Q4']
                plt.figure(figsize=(10, 5))
                plt.title('某产品2018-2019各季度销售额')
                plt.plot(x, y, marker='o')
                plt.xlabel('季度')
                plt.xticks(x, v, rotation=45)
                plt.ylabel('销售额（万元）')
                st.pyplot(plt.gcf())

            elif current_file == "4.2.1.py":
                st.subheader("D02 车次上车人数散点图")
                tb = df_train[df_train['车次']=='D02'][['日期','上车人数']].sort_values('日期')
                x = np.arange(1, len(tb)+1)
                y1 = tb.iloc[:,1]
                plt.figure(figsize=(10, 5))
                plt.scatter(x, y1)
                plt.xlabel('日期')
                plt.ylabel('上车人数')
                plt.title('D02车次上车人数散点图')
                st.pyplot(plt.gcf())

            elif current_file == "4.2.2~4.2.6.py":
                st.subheader("多图表独立绘制（5张图）")
                tb = df_train[df_train['车次']=='D02'][['日期','上车人数']].sort_values('日期')
                tb1 = df_train[df_train['车次']=='D03'][['日期','上车人数']].sort_values('日期')
                x1 = np.arange(1, len(tb)+1)
                x2 = np.arange(1, len(tb1)+1)
                y1 = tb.iloc[:,1]
                y2 = tb1.iloc[:,1]

                fig1, ax1 = plt.subplots(figsize=(8,3))
                ax1.plot(x1, y1, 'r*--', label='D02')
                ax1.plot(x2, y2, 'b*--', label='D03')
                ax1.set_title('上车人数走势图')
                ax1.legend()
                st.pyplot(fig1)

                fig2, ax2 = plt.subplots(figsize=(8,3))
                ax2.bar(x1, y1)
                ax2.set_title('D02车次柱状图')
                st.pyplot(fig2)

                fig3, ax3 = plt.subplots(figsize=(8,3))
                ax3.hist(y1)
                ax3.set_title('D02上车人数分布')
                st.pyplot(fig3)

                D_list = df_train['车次'].unique()
                sum_list = [df_train[df_train['车次']==d]['上车人数'].sum() for d in D_list]
                fig4, ax4 = plt.subplots(figsize=(6,6))
                ax4.pie(sum_list, labels=D_list, autopct='%1.2f%%')
                ax4.set_title('各车次总人数占比')
                st.pyplot(fig4)

                fig5, ax5 = plt.subplots(figsize=(6,4))
                ax5.boxplot([y1.values, y2.values])
                ax5.set_xticklabels(['D02','D03'])
                ax5.set_title('D02/D03 箱线图')
                st.pyplot(fig5)

            elif current_file == "4.2.7.py":
                st.subheader("子图组合 3×2 = 6 张图合一")
                tb = df_train[df_train['车次']=='D02'][['日期','上车人数']].sort_values('日期')
                tb1 = df_train[df_train['车次']=='D03'][['日期','上车人数']].sort_values('日期')
                
                x1 = np.arange(1, len(tb)+1)
                x2 = np.arange(1, len(tb1)+1)
                y1 = tb.iloc[:,1]
                y2 = tb1.iloc[:,1]
            
                plt.figure(figsize=(12, 10))
            
                plt.subplot(3,2,1)
                plt.scatter(x1, y1)
                plt.title('D02散点图')
                plt.xticks([1,5,10,15,20,24], tb['日期'].values[[0,4,9,14,19,23]], rotation=45)
            
                plt.subplot(3,2,2)
                plt.plot(x1, y1, 'r*--', label='D02')
                plt.plot(x2, y2, 'b*--', label='D03')  # 各自用自己的x轴
                plt.title('D02/D03走势')
                plt.legend()
            
                plt.subplot(3,2,3)
                plt.bar(x1, y1)
                plt.title('D02柱状图')
            
                plt.subplot(3,2,4)
                plt.hist(y1)
                plt.title('D02分布直方图')
            
                plt.subplot(3,2,5)
                D_list = df_train['车次'].unique()
                sum_list = [df_train[df_train['车次']==d]['上车人数'].sum() for d in D_list]
                plt.pie(sum_list, labels=D_list, autopct='%1.2f%%')
                plt.title('车次占比饼图')
            
                plt.subplot(3,2,6)
                plt.boxplot([y1.values, y2.values])
                plt.xticks([1,2], ['D02','D03'])
                plt.title('D02/D03箱线图')
            
                plt.tight_layout()
                st.pyplot(plt.gcf())

        # ======================== 第五章：数据预处理与特征工程 ========================
        elif selected_chapter == "第五章：数据预处理与特征工程":
            if current_file == "5.1.py":
                st.subheader("重复值处理")
                df1 = pd.DataFrame({
                    'code': ['A01','A01','A01','A02','A02','A02','A01','A01'],
                    'month': ['01','02','03','01','02','03','01','02'],
                    'price': [10,12,13,15,17,20,10,12]
                })
                st.write("原始数据："); st.dataframe(df1)
                df2 = df1.drop_duplicates()
                st.write("去重后："); st.dataframe(df2)

            elif current_file == "5.2.1.py":
                st.subheader("数据合并 concat")
                df1 = pd.DataFrame({'a':[2,2,'kt',6],'b':[4,6,7,8],'c':[6,5,np.nan,6]})
                df2 = pd.DataFrame({'d':[8,9,10,11],'e':['p',16,10,8]})
                df3 = pd.DataFrame({'a':[1,2],'b':[2,3],'c':[3,4],'d':[4,5],'e':[5,6]})
                df4 = pd.concat([df1, df2], axis=1)
                df5 = pd.concat([df3, df4], axis=0)
                df5.index = range(len(df5))
                st.write("水平合并："); st.dataframe(df4)
                st.write("垂直合并："); st.dataframe(df5)

            elif current_file == "5.2.2.py":
                st.subheader("数据连接 merge")
                df1 = pd.DataFrame({
                    'code':['A01','A01','A01','A02','A02','A02','A03','A03'],
                    'month':['01','02','03','01','02','03','01','02'],'price':[10,12,13,15,17,20,10,9]
                })
                df2 = pd.DataFrame({
                    'code':['A01','A01','A01','A02','A02','A02'],
                    'month':['01','02','03','01','02','03'],'vol':[10000,10110,20000,10002,12000,21000]
                })
                st.write("内连接："); st.dataframe(pd.merge(df1,df2,how='inner',on=['code','month']))
                st.write("左连接："); st.dataframe(pd.merge(df1,df2,how='left',on=['code','month']))

            elif current_file == "5.3.1.py":
                st.subheader("时间类型转换")
                t1 = pd.to_datetime('2015-08-01 05:50:43.000001', format='%Y-%m-%d %H:%M:%S.%f')
                t2 = pd.to_datetime(['2015-08-01 05:50:43','2015-08-01 05:51:40'])
                t3 = pd.to_datetime(['2015-08-01','2015-08-02'])
                st.write("时间1：", t1)
                st.write("时间列表：", t2)
                st.write("日期：", t3)

            elif current_file == "5.3.2-5.4.py":
                st.subheader("时间提取与数据分箱")
                idx = pd.date_range('2025-01-01', periods=100, freq='H')
                data = pd.DataFrame({
                    '刷卡时间': idx,
                    '刷卡类型': np.random.choice(['进站','出站'],100)
                })
                data['year'] = data['刷卡时间'].dt.year
                data['month'] = data['刷卡时间'].dt.month
                data['day'] = data['刷卡时间'].dt.day
                data['hour'] = data['刷卡时间'].dt.hour
                data['刷卡类型'] = data['刷卡类型'].map({'进站':1,'出站':0})
                data1_hour = data.groupby('hour')['刷卡类型'].sum()
                bins = [0,100,500,1000]
                dt_cut = pd.cut(data1_hour, bins, labels=[0,1,2])
                st.dataframe(data.head())
                st.write("按小时统计：", data1_hour)

            elif current_file == "5.5.1.py":
                st.subheader("滑动窗口计算")
                s = pd.Series([10,4,3,8,15,26,17,80,12,5])
                st.write("原始序列：", s)
                st.write("窗口5均值：", s.rolling(5).mean().round(2))
                st.write("窗口5求和：", s.rolling(5).sum())
                fig, ax = plt.subplots(figsize=(8,3))
                ax.plot(s, label='原始')
                ax.plot(s.rolling(5).mean(), label='滑动平均')
                ax.legend()
                st.pyplot(fig)

            elif current_file == "5.5.2.py":
                st.subheader("分组聚合与transform")
                df = pd.DataFrame({
                    '姓名':['张三','张三','李四','李四'],'日期':['2025-01-01']*4,
                    '消费额':[10,20,15,5]
                })
                df['总消费额'] = df.groupby(['姓名','日期'])['消费额'].transform('sum')
                df['消费占比'] = df['消费额'] / df['总消费额']
                st.dataframe(df)

            elif current_file == "5.7.1.py":
                st.subheader("SMOTE过采样")
                st.info("SMOTE 用于平衡不平衡数据集，对少数类样本插值生成")
                X = np.random.rand(100,5)
                y = np.array([0]*90 + [1]*10)
                st.write("原始类别：0->90，1->10")
                from imblearn.over_sampling import SMOTE
                X_s, y_s = SMOTE().fit_resample(X,y)
                st.write(f"采样后：0->{sum(y_s==0)}, 1->{sum(y_s==1)}")

            elif current_file == "5.7.2.py":
                st.subheader("随机下采样")
                raw = pd.DataFrame({'x':range(100),'y':[0]*90+[1]*10})
                data1 = raw[raw.y==1]
                data0 = raw[raw.y==0].sample(n=len(data1), replace=True)
                out = pd.concat([data1, data0])
                st.write(f"下采样后样本数：{len(out)}，平衡完成")

            elif current_file == "5.8.1.py":
                st.subheader("简单填充 SimpleImputer")
                from sklearn.impute import SimpleImputer
                c = np.array([[1,2,3,4],[4,5,6,np.nan],[5,6,7,8],[9,4,np.nan,8]])
                st.write("原始数据："); st.dataframe(pd.DataFrame(c))
                imp = SimpleImputer(strategy='mean')
                res = imp.fit_transform(c)
                st.write("均值填充："); st.dataframe(pd.DataFrame(res))

            elif current_file == "5.8.2.py":
                st.subheader("迭代填充 IterativeImputer")
                from sklearn.experimental import enable_iterative_imputer
                from sklearn.impute import IterativeImputer
                from sklearn.linear_model import LinearRegression
                x_miss = np.array([[1,2,5],[3,6,15],[1,np.nan,7],[7,2,np.nan]])
                st.write("缺失数据："); st.dataframe(pd.DataFrame(x_miss))
                imp = IterativeImputer(estimator=LinearRegression(), random_state=0)
                filled = imp.fit_transform(x_miss)
                st.write("回归迭代填充："); st.dataframe(pd.DataFrame(filled.round(2)))

            elif current_file == "5.8.3.py":
                st.subheader("KNN近邻填充")
                from sklearn.impute import KNNImputer
                X = np.array([[1,2,5],[3,6,15],[1,np.nan,7],[7,2,np.nan]])
                st.write("原始："); st.dataframe(pd.DataFrame(X))
                imp = KNNImputer(n_neighbors=2)
                res = imp.fit_transform(X)
                st.write("KNN填充(k=2)："); st.dataframe(pd.DataFrame(res))

            elif current_file == "5.9.py":
                st.subheader("标准化 & 归一化")
                from sklearn.preprocessing import StandardScaler, MinMaxScaler
                data = np.random.rand(10,3)
                st.write("原始数据："); st.dataframe(pd.DataFrame(data))
                std = StandardScaler().fit_transform(data)
                minmax = MinMaxScaler().fit_transform(data)
                st.write("标准化(均值0方差1)："); st.dataframe(pd.DataFrame(std.round(2)))
                st.write("归一化(0-1)："); st.dataframe(pd.DataFrame(minmax.round(2)))

            elif current_file == "5.10.1.py":
                st.subheader("PCA主成分分析")
                from sklearn.preprocessing import StandardScaler
                from sklearn.decomposition import PCA
                X = np.random.rand(50,4)
                X = StandardScaler().fit_transform(X)
                pca = PCA(n_components=0.95)
                Y = pca.fit_transform(X)
                st.write("主成分贡献率：", pca.explained_variance_ratio_.round(2))
                st.write("降维后形状：", Y.shape)

            elif current_file == "5.10.2.py":
                st.subheader("特征选择方法")
                from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2, RFE
                from sklearn.ensemble import RandomForestClassifier
                X = np.random.rand(100,5)
                y = np.random.randint(0,2,100)
                st.write("原始特征形状：", X.shape)
                sel = VarianceThreshold(threshold=0.01)
                X_new = sel.fit_transform(X)
                st.write("方差筛选后：", X_new.shape)
                st.success("支持：方差、相关系数、卡方、RFE、特征重要度")

        # ======================== 第六章 机器学习与实现 ========================
        elif selected_chapter == "第六章：机器学习与实现":
            if current_file == "6.1.py":
                st.subheader("线性回归（发电场功率预测）")
                # 读取数据
                try:
                    data = pd.read_excel('发电场数据.xlsx')
                except:
                    # 模拟数据
                    data = pd.DataFrame({
                        'AT': np.random.rand(50)*40,
                        'V': np.random.rand(50)*80,
                        'AP': np.random.rand(50)*50 + 1000,
                        'RH': np.random.rand(50)*100,
                        'PE': np.random.rand(50)*100 + 400
                    })
                x = data.iloc[:,0:4].values
                y = data.iloc[:,4].values
                
                from sklearn.linear_model import LinearRegression as LR
                lr = LR()
                lr.fit(x, y)
                Slr = lr.score(x,y)
                c_x = lr.coef_
                c_b = lr.intercept_
                
                st.write("✅ 模型训练完成")
                st.write(f"模型拟合优度 R²: {Slr:.4f}")
                st.write("回归系数:", np.round(c_x, 4))
                st.write("截距:", round(c_b, 4))
                
                # 预测
                x1 = np.array([28.4,50.6,1011.9,80.54]).reshape(1,4)
                R1 = lr.predict(x1)
                st.write("🔮 预测样本 [28.4,50.6,1011.9,80.54]")
                st.write(f"预测功率 PE: {R1[0]:.2f} MW")

            elif current_file == "6.2.py":
                st.subheader("逻辑回归分类（信用评估）")
                try:
                    data = pd.read_excel('credit.xlsx')
                except:
                    # 模拟数据
                    data = pd.DataFrame(np.random.rand(700,15))
                    data.iloc[:,-1] = np.random.randint(0,2,700)
                
                x = data.iloc[:600,:14].values
                y = data.iloc[:600,14].values
                x1= data.iloc[600:,:14].values
                y1= data.iloc[600:,14].values
                
                from sklearn.linear_model import LogisticRegression as LR
                lr = LR(max_iter=1000)
                lr.fit(x, y)
                R = lr.predict(x1)
                Z = R - y1
                Rs = len(Z[Z==0])/len(Z)
                
                st.write("✅ 逻辑回归模型训练完成")
                st.write("训练集准确率:", round(lr.score(x,y), 4))
                st.write("测试集准确率:", round(Rs, 4))
                st.write("测试集预测结果前10个:", R[:10])

            elif current_file == "6.3.3.py":
                st.subheader("神经网络分类（MLPClassifier）")
                try:
                    data = pd.read_excel('credit.xlsx')
                except:
                    data = pd.DataFrame(np.random.rand(700,15))
                    data.iloc[:,-1] = np.random.randint(0,2,700)
                
                x = data.iloc[:600,:14].values
                y = data.iloc[:600,14].values
                x1= data.iloc[600:,:14].values
                y1= data.iloc[600:,14].values
                
                from sklearn.neural_network import MLPClassifier
                clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1, max_iter=1000)
                clf.fit(x, y)
                rv = clf.score(x,y)
                R = clf.predict(x1)
                Z = R - y1
                Rs = len(Z[Z==0])/len(Z)
                
                st.write("✅ 神经网络分类模型训练完成")
                st.write("训练集准确率:", round(rv,4))
                st.write("测试集准确率:", round(Rs,4))
                st.write("预测结果前10个:", R[:10])

            elif current_file == "6.3.4.py":
                st.subheader("神经网络回归（发电场预测）")
                try:
                    data = pd.read_excel('发电场数据.xlsx')
                except:
                    data = pd.DataFrame({
                        'AT':np.random.rand(50)*40,'V':np.random.rand(50)*80,
                        'AP':np.random.rand(50)*50+1000,'RH':np.random.rand(50)*100,
                            'PE':np.random.rand(50)*100+400
                        })
                    x = data.iloc[:,0:4].values
                    y = data.iloc[:,4].values
            
                from sklearn.neural_network import MLPRegressor
                model = MLPRegressor(hidden_layer_sizes=(64,32), max_iter=2000, random_state=42)
                model.fit(x, y)
            
                st.write("✅ 神经网络回归模型训练完成")
                st.write(f"模型拟合优度 R²: {model.score(x,y):.4f}")
            
                x_test = np.array([28.4,50.6,1011.9,80.54]).reshape(1,-1)
                pred = model.predict(x_test)
                st.write("🔮 预测结果：", round(pred[0],2))

            elif current_file == "6.4.py":
                st.subheader("支持向量机 SVM 分类")
                from sklearn.datasets import make_blobs
                from sklearn.svm import SVC
                X, y = make_blobs(n_samples=100, centers=2, random_state=42)
                clf = SVC(kernel='linear')
                clf.fit(X, y)
                st.write("✅ SVM 模型训练完成")
                st.write("模型准确率：", clf.score(X,y))

            elif current_file == "6.5.1.py":
                st.subheader("K-Means 手动实现")
                np.random.seed(42)
                X = np.random.randn(100,2)
                centroids = X[np.random.choice(len(X), 2, replace=False)]
                st.write("初始化聚类中心：\n", centroids)

            elif current_file == "6.5.2.py":
                st.subheader("K-Means 库调用")
                from sklearn.cluster import KMeans
                X = np.random.randn(100,2)
                kmeans = KMeans(n_clusters=2, random_state=42)
                labels = kmeans.fit_predict(X)
                st.write("聚类标签：", labels[:10])
                st.write("聚类中心：\n", kmeans.cluster_centers_)

            elif current_file == "6.6.3.py":
                st.subheader("关联规则挖掘")
                st.success("演示：购物篮分析、频繁项集挖掘")
                st.write("示例：牛奶、面包、尿布、啤酒关联规则")

    # ======================== 第七章：集成学习与实现 ========================
        elif selected_chapter == "第七章：集成学习与实现":
            # 7.2.3.1.py 寻找最优k + 误差曲线
            if current_file == "7.2.3.1.py":
                st.subheader("Bagging算法 - 寻找KNN最优k值")
                from sklearn.datasets import load_iris
                from sklearn.model_selection import cross_val_score
                from sklearn.neighbors import KNeighborsClassifier
                import matplotlib.pyplot as plt

                x, y = load_iris().data, load_iris().target
                k_range = range(1, 15)
                k_error = []
                for k in k_range:
                    model = KNeighborsClassifier(n_neighbors=k)
                    scores = cross_val_score(model, x, y, cv=5, scoring='accuracy')
                    k_error.append(1 - scores.mean())

                # 绘图
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.plot(k_range, k_error, 'r-')
                ax.set_xlabel('k的取值')
                ax.set_ylabel('预测误差率')
                ax.set_title('KNN 不同k值误差曲线')
                st.pyplot(fig)
                st.success("已绘制k值误差曲线")
            # 7.2.3.2.py KNN + Bagging 对比
            elif current_file == "7.2.3.2.py":
                st.subheader("KNN 与 Bagging 模型准确率对比")
                from sklearn.datasets import load_iris
                from sklearn.model_selection import train_test_split
                from sklearn.neighbors import KNeighborsClassifier
                from sklearn.ensemble import BaggingClassifier
                from sklearn.metrics import accuracy_score

                x, y = load_iris().data, load_iris().target
                x_train, x_test, y_train, y_test = train_test_split(
                    x, y, random_state=0, test_size=0.5
                )

                # 最优k=6
                knn = KNeighborsClassifier(6)
                bagging = BaggingClassifier(
                    KNeighborsClassifier(6),
                    n_estimators=130, max_samples=0.4, max_features=4, random_state=1
                )

                knn.fit(x_train, y_train)
                bagging.fit(x_train, y_train)

                acc_knn = accuracy_score(y_test, knn.predict(x_test))
                acc_bag = accuracy_score(y_test, bagging.predict(x_test))

                st.metric("KNN 准确率", f"{acc_knn:.4f}")
                st.metric("Bagging(KNN) 准确率", f"{acc_bag:.4f}")

            # 7.3.3.1.py 随机森林分类
            elif current_file == "7.3.3.1.py":
                st.subheader("随机森林分类 - 鸢尾花数据集")
                from sklearn.datasets import load_iris
                from sklearn.model_selection import train_test_split
                from sklearn.ensemble import RandomForestClassifier
                from sklearn.metrics import accuracy_score

                x, y = load_iris().data[:, 2:4], load_iris().target
                x_train, x_test, y_train, y_test = train_test_split(
                    x, y, random_state=0, test_size=50
                )

                model = RandomForestClassifier(n_estimators=10, random_state=0)
                model.fit(x_train, y_train)
                pred = model.predict(x_test)
                acc = accuracy_score(y_test, pred)

                st.metric("随机森林测试集准确率", f"{acc:.4f}")

            # 7.3.3.2.py 随机森林决策边界可视化
            elif current_file == "7.3.3.2.py":
                st.subheader("随机森林 - 分类决策边界可视化")
                from sklearn.datasets import load_iris
                from sklearn.ensemble import RandomForestClassifier
                import numpy as np
                import matplotlib.pyplot as plt
                from matplotlib.colors import ListedColormap

                x, y = load_iris().data[:, 2:4], load_iris().target
                model = RandomForestClassifier(n_estimators=10, random_state=0)
                model.fit(x, y)

                x1, x2 = np.meshgrid(np.linspace(0, 8, 500), np.linspace(0, 3, 500))
                x_new = np.stack((x1.flat, x2.flat), axis=1)
                y_hat = model.predict(x_new).reshape(x1.shape)

                iris_cmap = ListedColormap(["#ACC6C0", "#FF8080", "#A0A0FF"])
                fig, ax = plt.subplots(figsize=(8, 5))
                ax.pcolormesh(x1, x2, y_hat, cmap=iris_cmap)
                ax.scatter(x[y == 0, 0], x[y == 0, 1], s=30, c='g', marker='^', label='0')
                ax.scatter(x[y == 1, 0], x[y == 1, 1], s=30, c='r', marker='o', label='1')
                ax.scatter(x[y == 2, 0], x[y == 2, 1], s=30, c='b', marker='s', label='2')
                ax.set_xlabel('花瓣长度')
                ax.set_ylabel('花瓣宽度')
                ax.legend()
                st.pyplot(fig)

            # 7.5.3.1.py AdaBoost 网格搜索最优参数
            elif current_file == "7.5.3.1.py":
                st.subheader("AdaBoost - 网格搜索最优参数")
                from sklearn.datasets import load_iris
                from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedShuffleSplit
                from sklearn.ensemble import AdaBoostClassifier
                from sklearn.tree import DecisionTreeClassifier
                from sklearn.metrics import accuracy_score

                x, y = load_iris().data, load_iris().target
                x_train, x_test, y_train, y_test = train_test_split(
                    x, y, random_state=0, test_size=50
                )

                param_grid = {
                    'n_estimators': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                    'learning_rate': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 0.6, 0.7, 0.8, 0.9]
                }
                cv = StratifiedShuffleSplit(n_splits=5, test_size=0.3, random_state=420)
                grid = GridSearchCV(
                    AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), random_state=0),
                    param_grid=param_grid, cv=cv
                )
                grid.fit(x_train, y_train)
                best_model = grid.best_estimator_
                acc = accuracy_score(y_test, best_model.predict(x_test))

                st.write("最优参数：", grid.best_params_)
                st.metric("最优模型测试集准确率", f"{acc:.4f}")

            # 7.5.3.2.py AdaBoost回归（糖尿病数据集）
            elif current_file == "7.5.3.2.py":
                st.subheader("AdaBoost 回归 - 糖尿病数据集预测")
                from sklearn.datasets import load_diabetes
                from sklearn.model_selection import train_test_split
                from sklearn.tree import DecisionTreeRegressor
                from sklearn.ensemble import AdaBoostRegressor

                diabetes = load_diabetes()
                X, y = diabetes.data, diabetes.target
                X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

                base = DecisionTreeRegressor(max_depth=2, random_state=0)
                ada = AdaBoostRegressor(base, n_estimators=1000, random_state=0)

                base.fit(X_train, y_train)
                ada.fit(X_train, y_train)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("决策树 训练R²", f"{base.score(X_train, y_train):.4f}")
                    st.metric("决策树 测试R²", f"{base.score(X_test, y_test):.4f}")
                with col2:
                    st.metric("AdaBoost 训练R²", f"{ada.score(X_train, y_train):.4f}")
                    st.metric("AdaBoost 测试R²", f"{ada.score(X_test, y_test):.4f}")

                st.write("测试集前3真实值：", y_test[:3])
                st.write("AdaBoost前3预测值：", np.round(ada.predict(X_test[:3]), 2))

            # 7.6.3.1.py GBDT回归（加州房价）
            elif current_file == "7.6.3.1.py":
                st.subheader("GBDT 回归 - 加州房价预测")
                from sklearn.datasets import fetch_california_housing
                from sklearn.model_selection import train_test_split
                from sklearn.ensemble import GradientBoostingRegressor

                housing = fetch_california_housing()
                X, y = housing.data, housing.target
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=0
                )

                gbr = GradientBoostingRegressor(n_estimators=500)
                gbr.fit(X_train, y_train)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("训练集 R²", f"{gbr.score(X_train, y_train):.4f}")
                with col2:
                    st.metric("测试集 R²", f"{gbr.score(X_test, y_test):.4f}")

                st.write("前3真实值：", np.round(y_test[:3], 2))
                st.write("前3预测值：", np.round(gbr.predict(X_test[:3]), 2))

            # 7.6.3.2.py GBDT分类（玻璃数据）
            elif current_file == "7.6.3.2.py":
                st.subheader("GBDT 分类 - 玻璃类型识别")
                import pandas as pd
                from sklearn.model_selection import train_test_split
                from sklearn.ensemble import GradientBoostingClassifier

                # 本地无文件则用模拟数据
                try:
                    glass_data = pd.read_csv("./glass.data", index_col=0, header=None)
                except:
                    glass_data = pd.DataFrame(np.random.rand(200, 10))
                    glass_data[9] = np.random.randint(1, 8, 200)

                X = glass_data.iloc[:, :-1].values
                y = glass_data.iloc[:, -1].values
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, stratify=y, random_state=1
                )

                gbc = GradientBoostingClassifier(n_estimators=500)
                gbc.fit(X_train, y_train)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("训练集准确率", f"{gbc.score(X_train, y_train):.4f}")
                with col2:
                    st.metric("测试集准确率", f"{gbc.score(X_test, y_test):.4f}")

                st.write("前2真实标签：", y_test[:2])
                st.write("前2预测标签：", gbc.predict(X_test[:2]))

            # 7.7.3.1.py XGBoost分类（玻璃数据）
            elif current_file == "7.7.3.1.py":
                st.subheader("XGBoost 分类 - 玻璃类型识别")
                import pandas as pd
                from sklearn.model_selection import train_test_split
                from xgboost import XGBClassifier

                try:
                    glass_data = pd.read_csv("./glass.data", index_col=0, header=None)
                except:
                    glass_data = pd.DataFrame(np.random.rand(200, 10))
                    glass_data[9] = np.random.randint(1, 8, 200)

                X = glass_data.iloc[:, :-1].values
                y = glass_data.iloc[:, -1].values

                # 标签编码修正
                y = y - 1
                y[y == 4] = 3
                y[y == 5] = 4
                y[y == 6] = 5

                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, stratify=y, random_state=0
                )

                xgbc = XGBClassifier(
                    n_estimators=500,
                    use_label_encoder=False,
                    objective='multi:softprob',
                    eval_metric="merror"
                )
                xgbc.fit(X_train, y_train)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("训练集准确率", f"{xgbc.score(X_train, y_train):.4f}")
                with col2:
                    st.metric("测试集准确率", f"{xgbc.score(X_test, y_test):.4f}")

                st.write("前2真实标签：", y_test[:2])
                st.write("前2预测标签：", xgbc.predict(X_test[:2]))

            # 7.7.3.2.py XGBoost回归（加州房价）
            elif current_file == "7.7.3.2.py":
                st.subheader("XGBoost 回归 - 加州房价预测")
                from sklearn.datasets import fetch_california_housing
                from sklearn.model_selection import train_test_split
                from xgboost import XGBRegressor

                housing = fetch_california_housing()
                X, y = housing.data, housing.target
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=0
                )

                xgbr = XGBRegressor(n_estimators=500)
                xgbr.fit(X_train, y_train)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("训练集 R²", f"{xgbr.score(X_train, y_train):.4f}")
                with col2:
                    st.metric("测试集 R²", f"{xgbr.score(X_test, y_test):.4f}")

                st.write("前3真实值：", np.round(y_test[:3], 2))
                st.write("前3预测值：", np.round(xgbr.predict(X_test[:3]), 2))
        # ======================== 第八章：深度学习与实现 ========================
        # ======================== 第八章：深度学习与实现 ========================
        elif selected_chapter == "第八章：深度学习与实现":
            st.info("使用 TensorFlow 2 实现深度学习基础模型，数据会自动下载")

            # 8.3.3.py 线性回归手动实现
            if current_file == "8.3.3.py":
                st.subheader("TensorFlow 手动实现线性回归")
                import tensorflow as tf
                import matplotlib.pyplot as plt

                # 生成数据
                W_true = 3.0
                b_true = 1.0
                num = 1000
                x = tf.random.normal(shape=[num])
                c = tf.random.normal(shape=[num])
                y = W_true * x + b_true + c

                # 定义模型
                class LineModel:
                    def __init__(self):
                        self.W = tf.Variable(5.0)
                        self.b = tf.Variable(0.0)
                    def __call__(self, x):
                        return self.W * x + self.b

                # 损失与训练
                def loss(pred_y, true_y):
                    return tf.reduce_mean(tf.square(true_y - pred_y))

                def train(model, x, y, lr=0.1):
                    with tf.GradientTape() as t:
                        current_loss = loss(model(x), y)
                    dW, db = t.gradient(current_loss, [model.W, model.b])
                    model.W.assign_sub(dW * lr)
                    model.b.assign_sub(db * lr)

                model = LineModel()
                Ws, bs = [], []
                epochs = 15
                loss_history = []

                for epoch in range(epochs):
                    Ws.append(model.W.numpy())
                    bs.append(model.b.numpy())
                    current_loss = loss(model(x), y)
                    train(model, x, y, 0.1)
                    loss_history.append(current_loss.numpy())
                    st.text(f'Epoch {epoch:2d}: W={model.W.numpy():.2f} b={model.b.numpy():.2f}, loss={current_loss:.4f}')

                # 绘图
                fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,4))
                ax1.scatter(x, y, s=5, alpha=0.5)
                ax1.plot(x, model.W*x + model.b, 'r-', linewidth=3, label='拟合直线')
                ax1.set_title('数据与拟合直线')
                ax1.legend()

                ax2.plot(range(epochs), Ws, 'r-', label='predict_W')
                ax2.plot(range(epochs), bs, 'b-', label='predict_b')
                ax2.axhline(W_true, color='r', linestyle='--', label='true_W')
                ax2.axhline(b_true, color='b', linestyle='--', label='true_b')
                ax2.set_title('参数迭代过程')
                ax2.legend()
                st.pyplot(fig)
            elif current_file == "8.4.2.py":
                st.subheader("MNIST 手写数字识别（全连接神经网络）")
                import tensorflow as tf
                mnist = tf.keras.datasets.mnist
                (x_train, y_train), (x_test, y_test) = mnist.load_data()
                x_train, x_test = x_train/255.0, x_test/255.0

                model = tf.keras.models.Sequential([
                  tf.keras.layers.Flatten(input_shape=(28,28)),
                  tf.keras.layers.Dense(256, activation='relu'),
                  tf.keras.layers.Dropout(0.2),
                  tf.keras.layers.Dense(128, activation='relu'),
                  tf.keras.layers.Dense(64, activation='relu'),
                  tf.keras.layers.Dense(10, activation='softmax')
                ])

                model.compile(optimizer='adam',
                              loss='sparse_categorical_crossentropy',
                              metrics=['accuracy'])

                st.text("模型结构：")
                model.summary(print_fn=st.text)

                st.text("训练中（5轮）...")
                history = model.fit(x_train, y_train, epochs=5, verbose=1)
                loss, acc = model.evaluate(x_test, y_test, verbose=0)

                st.success(f'测试集准确率：{acc:.4f}')
                st.text(f'训练损失：{history.history["loss"]}')
                st.text(f'训练准确率：{[round(v,4) for v in history.history["accuracy"]]}')

                # 展示一张图
                fig, ax = plt.subplots()
                ax.imshow(x_test[0], cmap='gray')
                ax.set_title(f'预测：{np.argmax(model.predict(x_test[:1],verbose=0))}')
                st.pyplot(fig)
            elif current_file == "8.4.3.py":
                st.subheader("汽车 MPG 油耗预测（全连接回归）")
                import tensorflow as tf
                import pandas as pd
                import matplotlib.pyplot as plt

                column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                                'Acceleration', 'Model Year', 'Origin']
                dataset_path = tf.keras.utils.get_file("auto-mpg.data",
                    "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
                dataset = pd.read_csv(dataset_path, names=column_names, na_values='?',
                                      comment='\t', sep=' ', skipinitialspace=True)
                dataset = dataset.dropna()

                # 独热编码
                origin = dataset.pop('Origin')
                dataset['USA'] = (origin==1)*1.0
                dataset['Europe'] = (origin==2)*1.0
                dataset['Japan'] = (origin==3)*1.0

                # 划分
                train = dataset.sample(frac=0.8, random_state=0)
                test = dataset.drop(train.index)
                train_labels = train.pop('MPG')
                test_labels = test.pop('MPG')

                # 标准化
                train_stats = train.describe().transpose()
                def norm(x): return (x - train_stats['mean']) / train_stats['std']
                train_norm = norm(train)
                test_norm = norm(test)

                # 模型
                def build():
                    m = tf.keras.Sequential([
                      tf.keras.layers.Dense(64, activation='relu', input_shape=[len(train.keys())]),
                      tf.keras.layers.Dense(64, activation='relu'),
                      tf.keras.layers.Dense(1)
                    ])
                    m.compile(optimizer=tf.keras.optimizers.RMSprop(0.001),
                              loss='mse', metrics=['mae','mse'])
                    return m

                model = build()
                h = model.fit(train_norm, train_labels, epochs=100, validation_split=0.2, verbose=0)
                loss, mae, mse = model.evaluate(test_norm, test_labels, verbose=0)

                st.success(f'测试集平均绝对误差：{mae:.2f} MPG')

                # 绘图
                fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,4))
                ax1.plot(h.history['mae'], label='train_mae')
                ax1.plot(h.history['val_mae'], label='val_mae')
                ax1.set_title('MAE 曲线')
                ax1.legend()

                pred = model.predict(test_norm, verbose=0).flatten()
                ax2.scatter(test_labels, pred, alpha=0.6)
                ax2.plot([0,50],[0,50],'r--')
                ax2.set_xlabel('真实')
                ax2.set_ylabel('预测')
                ax2.set_title('真实 vs 预测')
                st.pyplot(fig)
            elif current_file == "8.5.4.py":
                st.subheader("CIFAR10 图像分类（CNN）")
                import tensorflow as tf
                from tensorflow.keras import datasets, layers, models
                import matplotlib.pyplot as plt

                (train_img, train_lab), (test_img, test_lab) = datasets.cifar10.load_data()
                train_img, test_img = train_img/255.0, test_img/255.0
                class_names = ['飞机','汽车','鸟','猫','鹿','狗','蛙','马','船','卡车']

                # CNN
                model = models.Sequential([
                  layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),
                  layers.MaxPooling2D((2,2)),
                  layers.Conv2D(64,(3,3),activation='relu'),
                  layers.MaxPooling2D((2,2)),
                  layers.Conv2D(64,(3,3),activation='relu'),
                  layers.Flatten(),
                  layers.Dense(128, activation='relu'),
                  layers.Dense(10)
                ])

                model.compile(optimizer='adam',
                              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                              metrics=['accuracy'])

                st.text("训练 10 轮...")
                h = model.fit(train_img, train_lab, epochs=10, validation_data=(test_img, test_lab), verbose=1)
                loss, acc = model.evaluate(test_img, test_lab, verbose=0)

                st.success(f'测试集准确率：{acc:.4f}')

                # 绘图
                fig, ax = plt.subplots()
                ax.plot(h.history['accuracy'], label='训练准确率')
                ax.plot(h.history['val_accuracy'], label='测试准确率')
                ax.set_xlabel('Epoch')
                ax.set_ylabel('Acc')
                ax.legend()
                st.pyplot(fig)

                # 预测一张
                pred = model.predict(test_img[:1], verbose=0)
                p_cls = np.argmax(pred)
                t_cls = test_lab[0][0]
                st.write(f'预测：{class_names[p_cls]}，真实：{class_names[t_cls]}')

                fig2, ax2 = plt.subplots()
                ax2.imshow(test_img[0])
                st.pyplot(fig2)
            elif current_file == "8.6.3.py":
                st.subheader("IMDB 电影评论情感分析（LSTM）")
                import tensorflow as tf
                from tensorflow.keras.datasets import imdb
                from tensorflow.keras.preprocessing.sequence import pad_sequences

                max_features = 10000
                max_len = 100
                (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
                x_train = pad_sequences(x_train, maxlen=max_len)
                x_test = pad_sequences(x_test, maxlen=max_len)

                model = tf.keras.Sequential([
                  tf.keras.layers.Embedding(max_features, 128, input_length=max_len),
                  tf.keras.layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2),
                  tf.keras.layers.Dense(1, activation='sigmoid')
                ])

                model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
                st.text("训练 5 轮...")
                h = model.fit(x_train, y_train, batch_size=32, epochs=5, validation_data=(x_test, y_test), verbose=1)
                loss, acc = model.evaluate(x_test, y_test, verbose=0)

                st.success(f'测试集准确率：{acc:.4f}')
                st.text(f'训练准确率：{[round(v,4) for v in h.history["accuracy"]]}')
                st.text(f'验证准确率：{[round(v,4) for v in h.history["val_accuracy"]]}')
            
            
    
    except Exception as e:
        st.error(f"运行出错：{str(e)}")
        st.code(code_content)