import streamlit as st
import os, re, pandas as pd, matplotlib.pyplot as plt, sys, io, warnings, threading
import plotly.express as px
from streamlit_lottie import st_lottie
import requests, datetime, random
import pyperclip
from cozepy import Coze, TokenAuth, Message, COZE_CN_BASE_URL

warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="视“见”AI—人工智能可视化学习平台",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🤖"
)

CHAPTER_NAMES = {
    "第1章": "第1章 Python基础",
    "第2章": "第2章 科学计算包NumPy",
    "第3章": "第3章 数据分析工具Pandas",
    "第4章": "第4章 数据可视化Matplotlib",
    "第5章": "第5章 数据预处理",
    "第6章": "第6章 机器学习基础",
    "第7章": "第7章 深度学习入门",
    "第8章": "第8章 综合项目实战"
}
HOT_QUESTIONS = ["如何安装numpy？", "pandas如何分组统计？", "Matplotlib怎么设置中文？", "有哪些常用机器学习算法？"]
DAILY_QUESTIONS = [
    {"content": "写出用 Pandas 读取csv方法的代码", "answer": "pd.read_csv"},
    {"content": "如何用Matplotlib画柱状图？", "answer": "plt.bar"},
    {"content": "NumPy用什么创建全零数组？", "answer": "np.zeros"},
]

CODE_EXERCISES = {
    "第1章": [
        {
            "title": "Python基础 - 列表推导式",
            "description": "补全列表推导式代码，生成1-10的平方数列表",
            "code_template": "squares = [{}**2 for {} in range(1, 11)]",
            "blanks": ["x", "x"],
            "difficulty": "简单"
        },
        {
            "title": "Python基础 - 函数定义",
            "description": "补全函数定义，计算两个数的和",
            "code_template": "def add(a, b):\n    return {} + {}",
            "blanks": ["a", "b"],
            "difficulty": "简单"
        }
    ],
    "第2章": [
        {
            "title": "NumPy - 创建数组",
            "description": "补全代码，创建一个3x3的全零数组",
            "code_template": "import numpy as np\nzeros_arr = np.{}((3, 3))",
            "blanks": ["zeros"],
            "difficulty": "简单"
        },
        {
            "title": "NumPy - 数组运算",
            "description": "补全代码，计算两个数组的点积",
            "code_template": "import numpy as np\narr1 = np.array([1,2,3])\narr2 = np.array([4,5,6])\ndot_product = np.{}({}, {})",
            "blanks": ["dot", "arr1", "arr2"],
            "difficulty": "中等"
        }
    ],
    "第3章": [
        {
            "title": "Pandas - 读取CSV文件",
            "description": "补全代码，读取CSV格式的数据文件",
            "code_template": "import pandas as pd\ndf = pd.{}('data.csv', encoding='utf-8')",
            "blanks": ["read_csv"],
            "difficulty": "简单"
        },
        {
            "title": "Pandas - 分组统计",
            "description": "补全代码，按类别列分组计算数值列的平均值",
            "code_template": "grouped = df.{}('类别列')['数值列'].{}()",
            "blanks": ["groupby", "mean"],
            "difficulty": "中等"
        }
    ],
    "第4章": [
        {
            "title": "Matplotlib - 绘制柱状图",
            "description": "补全代码，使用Matplotlib绘制柱状图",
            "code_template": "import matplotlib.pyplot as plt\nx = ['A', 'B', 'C']\ny = [10, 20, 15]\nplt.{}({}, {})\nplt.{}('柱状图示例')\nplt.{}()",
            "blanks": ["bar", "x", "y", "title", "show"],
            "difficulty": "中等"
        },
        {
            "title": "Matplotlib - 设置中文显示",
            "description": "补全代码，设置Matplotlib支持中文显示",
            "code_template": "plt.rcParams['font.sans-serif'] = ['{}']\nplt.rcParams['axes.unicode_minus'] = {}",
            "blanks": ["SimHei", "False"],
            "difficulty": "简单"
        }
    ],
    "第5章": [
        {
            "title": "数据预处理 - 缺失值处理",
            "description": "补全代码，填充数据框中的缺失值为0",
            "code_template": "import pandas as pd\ndf = df.{}({})",
            "blanks": ["fillna", "0"],
            "difficulty": "中等"
        },
        {
            "title": "数据预处理 - 重复值删除",
            "description": "补全代码，删除数据框中的重复行",
            "code_template": "df = df.{}()",
            "blanks": ["drop_duplicates"],
            "difficulty": "简单"
        }
    ],
    "第6章": [
        {
            "title": "机器学习 - 数据划分",
            "description": "补全代码，划分训练集和测试集",
            "code_template": "from sklearn.model_selection import {}\nX_train, X_test, y_train, y_test = {}({}, {}, test_size=0.2, random_state=42)",
            "blanks": ["train_test_split", "train_test_split", "X", "y"],
            "difficulty": "中等"
        },
        {
            "title": "机器学习 - 线性回归",
            "description": "补全代码，创建并训练线性回归模型",
            "code_template": "from sklearn.linear_model import {}\nmodel = {}()\nmodel.{}({}, {})",
            "blanks": ["LinearRegression", "LinearRegression", "fit", "X_train", "y_train"],
            "difficulty": "较难"
        }
    ],
    "第7章": [
        {
            "title": "深度学习 - 创建Sequential模型",
            "description": "补全代码，创建简单的深度学习模型",
            "code_template": "from tensorflow.keras.models import {}\nfrom tensorflow.keras.layers import Dense\nmodel = {}()\nmodel.add(Dense(64, activation='{}', input_shape=(10,)))\nmodel.add(Dense(1, activation='linear'))",
            "blanks": ["Sequential", "Sequential", "relu"],
            "difficulty": "较难"
        }
    ],
    "第8章": [
        {
            "title": "综合项目 - 数据可视化",
            "description": "补全代码，使用Plotly绘制交互式折线图",
            "code_template": "import plotly.express as px\nfig = px.{}({}, x='日期', y='销量', title='销量趋势')\npx.{}({})",
            "blanks": ["line", "df", "show", "fig"],
            "difficulty": "较难"
        }
    ]
}

st.markdown("""
<style>
.stApp {background:linear-gradient(135deg, #f8f5ff 0%, #ebe2fc 100%)!important; font-family:"Microsoft YaHei","SimHei",sans-serif;}
[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #ece4ff 0%, #e3fbfc 100%) !important;
    border-radius: 18px 10px 10px 36px !important;
    margin-left:4px !important;
    border-right:3px solid #b18afe20 !important;
    box-shadow:0 6px 24px 2px #b18afe13 !important;
    min-width: 260px !important;
}
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div {
    color:#3d2377 !important;
}
[data-testid="stSidebar"] .stButton>button {
    background:#8981f8 !important;
    color:white !important;
    border-radius:12px !important;
}
[data-testid="stSidebar"] .stButton>button:hover {background:#6357b8!important}
.card-primary {background:linear-gradient(135deg,#7c3aed 0,#8b5cf6 100%)!important;color:#fff!important; border-radius:22px!important;padding:30px;margin-bottom:24px;
box-shadow:0 8px 28px #7c3aed23!important;}
.card-white {background:#fff!important;border-radius:24px!important;padding:28px!important;border:1px solid #e7dfff!important;box-shadow:0 2px 12px #efe5ff;}
.card-dark {background:#2e1065!important;color:#fff!important;border-radius:24px!important;padding:28px!important;}
.ai-chat-block {background:linear-gradient(120deg,#f8f2ff 85%,#e0e0f5 100%);border-radius:18px 22px 20px 8px;padding:13px 16px 13px 18px;box-shadow:0 6px 16px #9174e910;margin-bottom:8px;max-width:88%;border:1px solid #e9d5ff;}
.ai-avatar {display:inline-block; background:#7c3aed; color:#fff; font-size:26px; border-radius:100px; width:37px; height:37px;text-align:center; line-height:39px; position:relative; left:-12px; top:8px; float:left;}
.user-chat-block {background:linear-gradient(110deg,#fbeed8 60%,#fdeacc 100%); border-radius:22px 18px 8px 20px;padding:13px 20px 13px 16px; margin-bottom:8px; text-align:right; box-shadow:0 4px 14px #fec16618;max-width:88%; border:1px solid #ffe8bb; margin-left:auto;}
.user-avatar {display:inline-block; background:#fec241; color:#fff; font-size:22px; border-radius:100px; width:32px; height:32px;text-align:center; line-height:34px; position:relative; right:-8px; top:8px; float:right;}
.ai-chat-zone {background:linear-gradient(129deg,#f5eefd 76%,#f8fafc 100%);border-radius:18px; min-height:235px; border:1px solid #efe1ff;padding:20px 10px 20px 10px;margin-bottom:13px;box-shadow:0 6px 28px #7c3aed13;}
.ai-zone-title {font-size:21px;font-weight:800;color:#6d34b0}
.footer {text-align:center;color:#999;padding:36px 0 10px 0;}
.progress-bar {height:24px;border-radius:12px;background:#f3e8ff;overflow:hidden;margin:8px 0;}
.progress-fill {height:100%;background:linear-gradient(90deg,#7c3aed,#8b5cf6);border-radius:12px;}
.loader {border: 4px solid #f3e8ff; border-top: 4px solid #7c3aed; border-radius: 50%; width: 20px; height: 20px; animation: spin 1s linear infinite; display: inline-block; margin-right: 8px;}
@keyframes spin {0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); }}
::-webkit-scrollbar {width: 8px; height: 8px;}
::-webkit-scrollbar-track {background: #f3e8ff; border-radius: 4px;}
::-webkit-scrollbar-thumb {background: #7c3aed; border-radius: 4px;}
::-webkit-scrollbar-thumb:hover {background: #6357b8;}
.chat-timestamp {font-size: 10px; color: #94a3b8; margin-top: 2px; display: block;}
.code-editor {border-radius: 12px; border: 1px solid #e9d5ff; padding: 16px; background: #f8f5ff; font-family: Consolas, monospace;}
.exercise-card {background:#fdfaff!important;border-radius:20px!important;padding:24px!important;border-left:4px solid #7c3aed!important;margin:16px 0!important;box-shadow:0 4px 12px #efe5ff;}
.blank-input {width:80px!important;height:36px!important;margin:0 4px!important;border-radius:8px!important;border:1px solid #d8b4fe!important;text-align:center!important;}
.correct-answer {background:#dcfce7!important;border:1px solid #86efac!important;padding:4px 8px!important;border-radius:6px!important;color:#166534!important;}
.wrong-answer {background:#fee2e2!important;border:1px solid #fca5a5!important;padding:4px 8px!important;border-radius:6px!important;color:#991b1b!important;}
</style>
""", unsafe_allow_html=True)

def load_lottieurl(url:str):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        if r.status_code == 200:
            return r.json()
    except Exception as e:
        st.warning(f"加载动画失败：{str(e)}")
    return None

def reset_all_data():
    default_progress = {k: False for k in CHAPTER_NAMES.keys()}
    default_states = {
        "progress": default_progress,
        "collection": [],
        "wrong_book": [],
        "page": "welcome",
        "chat_history": [],
        "active_chapter": list(CHAPTER_NAMES.keys())[0],
        "qa_history": [],
        "today_ques": None,
        "loading": False,
        "exercise_answers": {},
        "exercise_scores": {}
    }
    for key in list(st.session_state.keys()):
        if key.startswith("chap_") and key.endswith("_history"):
            del st.session_state[key]
    for key, default_value in default_states.items():
        st.session_state[key] = default_value

def init_session_state():
    default_progress = {k: False for k in CHAPTER_NAMES.keys()}
    default_states = {
        "progress": default_progress,
        "collection": [],
        "wrong_book": [],
        "page": "welcome",
        "chat_history": [],
        "active_chapter": list(CHAPTER_NAMES.keys())[0],
        "qa_history": [],
        "today_ques": None,
        "loading": False,
        "exercise_answers": {},
        "exercise_scores": {}
    }
    for key, default_value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

init_session_state()

def render_auto_code_exercise(chapter_key, current_file="未指定文件"):
    st.markdown('<div class="card-white"><h4>🎯 代码填空练习</h4>', unsafe_allow_html=True)
    if 'code' not in globals() or not code:
        st.info("暂无代码可练习，请先选择代码文件")
        st.markdown('</div>', unsafe_allow_html=True)
        return

    blank_code = code
    blank_keys = []
    chap_full = CHAPTER_NAMES.get(chapter_key, chapter_key)

    if chapter_key == "第1章":
        blank_code = blank_code.replace("print", "____")
        blank_code = blank_code.replace("for", "____")
        blank_code = blank_code.replace("if", "____")
        blank_code = blank_code.replace("else", "____")
        blank_code = blank_code.replace("input", "____")
        blank_keys = ["print"]
    else:
        keywords = ["pandas", "plt", "df", "numpy", "pd", "np", "matplotlib",
                    "read_csv", "groupby", "bar", "zeros", "dot", "fillna"]
        blank_keys = []
        for kw in keywords:
            if kw in blank_code and len(blank_keys) < 2:
                blank_code = blank_code.replace(kw, "____", 1)
                blank_keys.append(kw)

    st.code(blank_code)
    ans = st.text_input("请输入答案（多个用英文逗号分隔）", key=f"blank_ans_{chapter_key}")

    if st.button("提交答案", key=f"submit_blank_{chapter_key}"):
        correct_str = ",".join(blank_keys)
        if ans.strip() == correct_str:
            st.success("回答正确！")
        else:
            st.error(f"错误，正确答案：{correct_str}，已记录错题")
            st.session_state.wrong_book.append({
                "chap": chap_full,
                "file": current_file,
                "blank_code": blank_code,
                "your_ans": ans,
                "correct_ans": correct_str
            })
    st.markdown('</div>', unsafe_allow_html=True)

class AIConfig:
    API_TOKEN = 'pat_SK50e0BNFAVdz03dze5uFTtrBZ3Hxk7EVQRE819m1ixx5e5PKmUmyofuDyivnQ1c'
    BASE_URL = COZE_CN_BASE_URL
    BOT_ID = '7630036637476978715'
    USER_ID = 'student'
    PROMPT_PREFIX = "你是Python大数据分析助教，仅根据教材1-8章内容回答，简洁专业："

@st.cache_resource
def get_coze_client():
    try:
        return Coze(auth=TokenAuth(token=AIConfig.API_TOKEN), base_url=AIConfig.BASE_URL)
    except:
        return None

coze_client = get_coze_client()

def get_coze_answer(question: str):
    if not coze_client:
        return "⚠️ AI 初始化失败，请检查配置"
    try:
        chat = coze_client.chat.create_and_poll(
            bot_id=AIConfig.BOT_ID,
            user_id=AIConfig.USER_ID,
            additional_messages=[
                Message.build_user_question_text(f"{AIConfig.PROMPT_PREFIX}\n{question}")
            ]
        )
        ans = []
        for msg in chat.messages:
            if msg.role == "assistant" and msg.type == "answer":
                ans.append(msg.content.strip())
        return "\n".join(ans) if ans else "暂无回答"
    except Exception as e:
        return f"❌ AI 出错：{str(e)}"


plt.rcParams.update({
    "font.sans-serif": ["SimHei", "Microsoft YaHei", "DejaVu Sans"],
    "axes.unicode_minus": False,
    "figure.figsize": (9, 6),
    "figure.dpi": 110
})

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Python大数据分析与挖掘实战：微课版（第2版）程序与数据")
def get_chapters(root: str):
    if not os.path.exists(root):
        st.warning(f"章节目录不存在：{root}")
        return list(CHAPTER_NAMES.keys())
    chapters = [f for f in os.listdir(root) if os.path.isdir(os.path.join(root, f))]
    chapters.sort(key=lambda s: int(re.search(r'(\d+)', s).group())
                  if re.search(r'(\d+)', s) else 999)
    return chapters

def get_files(path: str):
    if not os.path.exists(path): return []
    return [f for f in os.listdir(path) if f.endswith('.py') and not f.startswith('.')]

def read_code(fp: str):
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        try:
            with open(fp, 'r', encoding='gbk') as f:
                return f.read()
        except Exception as e:
            st.warning(f"读取GBK编码文件失败：{fp}，错误：{str(e)}")
            return ""
    except Exception as e:
        st.error(f"读取文件失败：{fp}，错误：{str(e)}")
        return ""

def load_preview_data(folder: str):
    if not os.path.exists(folder): return None
    data_files = [f for f in os.listdir(folder) if f.endswith(('.csv', '.xlsx')) and not f.startswith('.')]
    if not data_files:
        return None
    for f in data_files:
        file_path = os.path.join(folder, f)
        try:
            if f.endswith('.csv'):
                return pd.read_csv(file_path, encoding='utf-8', low_memory=False)
            elif f.endswith('.xlsx'):
                return pd.read_excel(file_path)
        except UnicodeDecodeError:
            try:
                return pd.read_csv(file_path, encoding='gbk', low_memory=False)
            except Exception as e:
                st.warning(f"读取GBK编码CSV失败：{f}，错误：{str(e)}")
                continue
        except Exception as e:
            st.warning(f"读取数据文件失败：{f}，错误：{str(e)}")
            continue
    return None

def run_code_simple(code: str, code_dir: str):
    if not code.strip(): return [], "", "代码为空，无法运行"
    dangerous_patterns = [
        r"os\.system", r"subprocess", r"eval\(", r"exec\(",
        r"open\(", r"__import__", r"sys\.exit", r"os\.rmdir"
    ]
    for pattern in dangerous_patterns:
        if re.search(pattern, code, re.IGNORECASE):
            return [], "", "⚠️ 代码包含危险操作，禁止执行！"
    cwd = os.getcwd()
    try:
        os.chdir(code_dir)
        plt.close('all')
        out = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = out
        exec_globals = {
            'plt': plt,
            'pd': pd,
            'np': __import__('numpy') if 'numpy' in code else None,
            'os': os,
            'sys': sys
        }
        result = {"figs": [], "output": "", "error": None}
        def execute_code():
            try:
                exec(code, exec_globals)
                result["figs"] = [plt.figure(n) for n in plt.get_fignums()]
                result["output"] = out.getvalue()
            except Exception as e:
                result["error"] = str(e)
        thread = threading.Thread(target=execute_code)
        thread.start()
        thread.join(timeout=10)
        if thread.is_alive():
            result["error"] = "代码执行超时（10秒），请检查代码是否有死循环！"
        sys.stdout = old_stdout
        return result["figs"], result["output"], result["error"]
    except Exception as e:
        sys.stdout = old_stdout
        return [], "", str(e)
    finally:
        os.chdir(cwd)

hour = datetime.datetime.now().hour
greeting = "早上好" if hour < 12 else ("下午好" if hour < 18 else "晚上好")

if st.session_state.page == "welcome":
    lottie_ai = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_zrqthn6o.json")
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.write("")
        if lottie_ai:
            st_lottie(lottie_ai, height=180, key="welcome_ai")
        else:
            st.markdown('<div style="text-align:center; font-size:80px; color:#7c3aed;">🤖</div>', unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center;'>"
                f"<h1 style='color:#7c3aed'>🤖 视“见”AI</h1>"
                f"<h2>人工智能可视化学习平台</h2>"
                f"<p style='color:#727B8A;font-size:20px;'>{greeting}，欢迎来到智能微课！</p>"
                f"</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card-white" style="max-width:800px;margin:24px auto 16px auto;">
        <ul>
            <li><b>AI 智能答疑</b>（支持热门提问/类Chat交互）</li>
            <li><b>交互式数据可视化</b>（Plotly/Matplotlib双支持）</li>
            <li><b>每日一题</b>，学业打卡提示</li>
            <li><b>收藏错题本/进度追踪/成就激励</b></li>
            <li><b>自定义代码编辑与运行</b></li>
            <li><b>代码填空练习题</b></li>
        </ul></div>
    """, unsafe_allow_html=True)
    if st.button("🚀 进入学习平台", use_container_width=True, type="primary"):
        st.session_state.page = "main"
        st.rerun()
    st.stop()

with st.sidebar:
    st.markdown(
        '<h2 style="color:#4a044e !important; text-align:center; font-size:26px; line-height:1.4; margin-bottom:20px;">'
        '视“见”AI<br>智能可视化学习平台</h2>',
        unsafe_allow_html=True
    )
    st.divider()
    nav_options = ["🏠 首页概览", "📂 章节学习", "✏️ 代码编辑", "✅ 学习进度", "⭐ 我的收藏", "❌ 错题本"]
    page = st.radio("", nav_options, key="sidebar_nav")
    st.divider()
    with st.expander("🔧 系统设置", expanded=False):
        if st.button("🗑️ 数据重置", type="secondary"):
            confirm_reset = st.checkbox("确认重置所有数据？（不可恢复）", key="confirm_reset")
            if confirm_reset:
                reset_all_data()
                st.success("已重置所有数据！")
                st.rerun()
        st.write(f"📚 完成章节：{sum(st.session_state.progress.values())}/8")
        st.write(f"⭐ 收藏数：{len(st.session_state.collection)}")
        st.write(f"❌ 错题数：{len(st.session_state.wrong_book)}")
        total_exercises = sum([len(exercises) for exercises in CODE_EXERCISES.values()])
        completed_exercises = 0
        for chap_scores in st.session_state["exercise_scores"].values():
            if chap_scores.get("completed", False):
                completed_exercises += chap_scores.get("total", 0)
        st.write(f"📝 完成练习题：{completed_exercises}/{total_exercises}")

if page == "🏠 首页概览":
    st.markdown(f"""<div class="card-primary">
        <h1 style='margin:0;font-size:34px;'>欢迎回到视“见”AI</h1>
        <p style="font-size:18px; margin-top:10px;">一站式 AI 与大数据学习系统</p>
        <p style="font-size:12px; opacity:0.8; margin-top:4px;">
            智能互动学习，每天进步一点点
        </p></div>""", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    total_done = sum(st.session_state.progress.values())
    with c1: st.metric("🎯 已完成章节", total_done, f"{(total_done/8)*100:.0f}%")
    with c2: st.metric("⭐ 收藏代码", len(st.session_state.collection))
    with c3: st.metric("❌ 错题数量", len(st.session_state.wrong_book))

    st.markdown("""<div class="ai-chat-zone"><span class="ai-zone-title">🤖 AI 智能答疑</span>""", unsafe_allow_html=True)
    sample_q = st.selectbox("🔥 热门/推荐问题", HOT_QUESTIONS + ["自定义..."], index=0, key="hotq")
    quick_input = st.text_input("输入提问内容（如留空使用热门问题）", key="quick_question2")
    askq = quick_input.strip() if quick_input else (sample_q if sample_q!="自定义..." else "")

    colqa1, colqa2 = st.columns([12,1])
    with colqa2:
        if st.button("问 AI", type="primary", key="ask_ai_home", disabled=st.session_state.loading) and askq:
            st.session_state.loading = True
            try:
                with st.spinner("AI正在思考..."):
                    answer = get_coze_answer(askq)
                current_time = datetime.datetime.now().strftime("%H:%M")
                st.session_state.qa_history.append({
                    "role":"user",
                    "content":askq,
                    "time": current_time
                })
                st.session_state.qa_history.append({
                    "role":"ai",
                    "content":answer,
                    "time": current_time
                })
            finally:
                st.session_state.loading = False

    for h in st.session_state.qa_history[-10:]:
        time_str = h.get("time", "")
        if h["role"]=="user":
            st.markdown(f"""<div class="user-chat-block">
            <span>{h["content"]}</span>
            <span class="user-avatar">👤</span>
            <span class="chat-timestamp">{time_str}</span>
            </div>""",unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="ai-chat-block">
            <span class="ai-avatar">🤖</span> <span>{h["content"]}</span>
            <span class="chat-timestamp" style="margin-left:45px;">{time_str}</span>
            </div>""",unsafe_allow_html=True)

    col_clear, col_empty = st.columns([2, 10])
    with col_clear:
        if st.session_state.qa_history:
            if st.button("🗑️ 清空对话历史", key="qa_clear"):
                st.session_state.qa_history = []
                st.rerun()
    st.markdown("</div>",unsafe_allow_html=True)

    dq = random.choice(DAILY_QUESTIONS) if st.session_state["today_ques"] is None else st.session_state["today_ques"]
    st.session_state["today_ques"] = dq
    st.divider()
    st.markdown('<div class="card-white"><h4>🌟 每日一题</h4>', unsafe_allow_html=True)
    ans = st.text_input(dq["content"], key="daily_ans")

    if st.button("提交答案", key="submit_daily", disabled=st.session_state.loading):
        st.session_state.loading = True
        try:
            if ans.strip() == dq["answer"]:
                st.success("答对啦，每日一题已完成！")
                unfinished_chapters = [k for k, v in st.session_state.progress.items() if not v]
                if unfinished_chapters:
                    random_chapter = random.choice(unfinished_chapters)
                    st.session_state.progress[random_chapter] = True
                    st.success(f"🎉 已自动标记「{CHAPTER_NAMES[random_chapter]}」为完成！")
            else:
                st.error(f"答错了，正确答案：{dq['answer']}")
                wrong_item = {
                    "question": dq["content"],
                    "user_answer": ans.strip(),
                    "correct_answer": dq["answer"],
                    "add_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                if not any(w["question"] == wrong_item["question"] and w["user_answer"] == wrong_item["user_answer"] for w in st.session_state.wrong_book):
                    st.session_state.wrong_book.append(wrong_item)
        finally:
            st.session_state.loading = False
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "✏️ 代码编辑":
    st.markdown(f"""<div class="card-primary">
        <h1 style='margin:0;font-size:34px;'>✏️ 自定义代码编辑</h1>
        <p style="font-size:18px; margin-top:10px;">编写并运行你的Python代码</p>
    </div>""", unsafe_allow_html=True)
    st.markdown('<div class="card-white">', unsafe_allow_html=True)
    if "custom_code" not in st.session_state:
        st.session_state.custom_code = "# 在这里编写你的Python代码\n# 支持Pandas/NumPy/Matplotlib等库\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\n\n# 示例：绘制简单折线图\nx = np.linspace(0, 10, 100)\ny = np.sin(x)\nplt.plot(x, y)\nplt.title('正弦曲线')\nplt.xlabel('X轴')\nplt.ylabel('Y轴')\nplt.show()"
    st.subheader("📝 代码编辑区")
    custom_code = st.text_area("", value=st.session_state.custom_code, height=400, key="code_editor", placeholder="请输入Python代码...", label_visibility="collapsed")
    st.session_state.custom_code = custom_code

    col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([1,1,1,7])
    with col_btn1:
        if st.button("▶️ 运行代码", type="primary"):
            with st.spinner("正在运行代码..."):
                code_dir = os.path.dirname(os.path.abspath(__file__))
                figs, output, error = run_code_simple(custom_code, code_dir)
            st.markdown('<div style="margin-top:20px;">', unsafe_allow_html=True)
            if error:
                st.error(f"❌ 运行错误：{error}")
            else:
                st.success("✅ 运行成功！")
                if output:
                    st.subheader("📊 输出结果")
                    st.code(output, language="text")
                if figs:
                    st.subheader("🎨 生成图表")
                    for fig in figs:
                        st.pyplot(fig)
            st.markdown('</div>', unsafe_allow_html=True)
    with col_btn2:
        if st.button("🗑️ 清空代码"):
            st.session_state.custom_code = "# 在这里编写你的Python代码\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\n"
            st.rerun()
    with col_btn3:
        if st.button("📋 复制代码"):
            try:
                pyperclip.copy(custom_code)
                st.success("代码已复制到剪贴板！")
            except:
                st.code(custom_code, language="python")
                st.info("复制功能需要安装pyperclip库，已显示代码供手动复制")
    st.markdown('<hr style="margin:20px 0;">', unsafe_allow_html=True)
    st.subheader("📚 常用代码示例")
    example_tab1, example_tab2, example_tab3 = st.tabs(["Pandas", "NumPy", "Matplotlib"])
    with example_tab1:
        st.code("""# 读取CSV文件
df = pd.read_csv('data.csv', encoding='utf-8')
# 查看数据基本信息
print(df.info())
# 数据筛选
filtered_df = df[df['数值列'] > 100]
# 分组统计
grouped = df.groupby('分类列')['数值列'].mean()
# 保存结果
df.to_excel('result.xlsx', index=False)""", language="python")
    with example_tab2:
        st.code("""# 创建数组
arr = np.array([1, 2, 3, 4, 5])
# 全零数组
zeros = np.zeros((3, 3))
# 随机数组
random_arr = np.random.rand(2, 2)
# 矩阵运算
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
result = mat1 @ mat2  # 矩阵乘法""", language="python")
    with example_tab3:
        st.code("""# 柱状图
x = ['A', 'B', 'C', 'D']
y = [10, 20, 15, 25]
plt.bar(x, y, color='skyblue')
plt.title('柱状图示例')
plt.show()

# 散点图
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, c='red', alpha=0.6)
plt.title('散点图示例')
plt.show()""", language="python")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📂 章节学习":
    chapters = get_chapters(ROOT)
    chap_key = st.sidebar.selectbox("选择章节", chapters, index=chapters.index(st.session_state.active_chapter) if st.session_state.active_chapter in chapters else 0, key="chapter_selector")
    st.session_state.active_chapter = chap_key
    chap_full = CHAPTER_NAMES.get(chap_key, chap_key)
    current_path = os.path.join(ROOT, chap_key)
    st.markdown(f'<div class="card-primary"><h2>📂 {chap_full}</h2></div>', unsafe_allow_html=True)

    col_status, col_empty = st.columns([1, 9])
    with col_status:
        is_complete = st.session_state.progress.get(chap_key, False)
        new_complete = st.checkbox("标记为已完成", value=is_complete, key=f"chap_complete_{chap_key}")
        if new_complete != is_complete:
            st.session_state.progress[chap_key] = new_complete
            st.success(f"「{chap_full}」已{'标记为完成' if new_complete else '取消完成标记'}")

    df = load_preview_data(current_path)
    if df is not None:
        st.markdown('<div class="card-white"><h4>📊 数据预览</h4>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.write(f"📏 行数：{len(df)}"); col2.write(f"📋 列数：{len(df.columns)}"); col3.write(f"📈 非空值：{df.notna().sum().sum()}")
        with st.expander("🔍 数据筛选", expanded=False):
            filter_col = st.selectbox("选择筛选列", df.columns, key="filter_col")
            if df[filter_col].dtype in ['int64', 'float64']:
                min_val = st.number_input("最小值", value=float(df[filter_col].min()), key="min_val")
                max_val = st.number_input("最大值", value=float(df[filter_col].max()), key="max_val")
                filtered_df = df[(df[filter_col] >= min_val) & (df[filter_col] <= max_val)]
            else:
                filter_val = st.text_input("包含关键词", key="filter_val")
                filtered_df = df[df[filter_col].astype(str).str.contains(filter_val, na=False)]
        display_df = filtered_df if 'filtered_df' in locals() else df
        st.dataframe(display_df.head(10), use_container_width=True)
        st.markdown('---')
        st.subheader("🎨 交互式数据可视化")
        cols = list(df.columns)
        if cols:
            x_col = st.selectbox("X轴字段", cols, key="plotly_x")
            y_col = st.selectbox("Y轴字段", cols, index=1 if len(cols) > 1 else 0, key="plotly_y")
            chart_type = st.selectbox("类型", ["折线图", "柱状图", "散点图", "饼图"], key="plotly_type")
            color_col = st.selectbox("颜色分组字段（可选）", ["无"] + cols, key="color_col")
            plot_btn = st.button("生成交互可视图", key="plotly_go")
            if plot_btn:
                try:
                    if chart_type == "折线图":
                        fig = px.line(df, x=x_col, y=y_col, color=color_col if color_col != "无" else None, markers=True)
                    elif chart_type == "柱状图":
                        fig = px.bar(df, x=x_col, y=y_col, color=color_col if color_col != "无" else None)
                    elif chart_type == "散点图":
                        fig = px.scatter(df, x=x_col, y=y_col, color=color_col if color_col != "无" else None)
                    elif chart_type == "饼图":
                        fig = px.pie(df, names=x_col, values=y_col if y_col != x_col else None)
                    fig.update_layout(
                        plot_bgcolor='rgba(255,255,255,0.8)',
                        paper_bgcolor='rgba(255,255,255,0)',
                        font=dict(family="Microsoft YaHei", size=12),
                        margin=dict(l=20, r=20, t=40, b=20)
                    )
                    st.plotly_chart(fig, use_container_width=True)
                except Exception as e:
                    st.error(f"生成图表失败：{str(e)}")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("暂无可用数据文件")

    st.markdown('<div class="card-white"><h4>🔍 代码查看</h4>', unsafe_allow_html=True)
    py_files = get_files(current_path)
    code = ""
    if py_files:
        fsel = st.selectbox("选择代码文件", py_files, key="code_file_selector")
        code = read_code(os.path.join(current_path, fsel))
        with st.expander("📝 查看代码", expanded=True):
            st.code(code, language="python", line_numbers=True)
        with st.expander("▶️ 运行代码", expanded=False):
            st.warning("⚠️ 运行前请确保代码安全，建议先查看代码内容！")
            if st.button("运行代码", key=f"run_code_{fsel}"):
                with st.spinner("正在运行代码..."):
                    figs, output, error = run_code_simple(code, current_path)
                if error:
                    st.error(f"运行错误：{error}")
                else:
                    if output:
                        st.success("运行成功！输出结果：")
                        st.code(output, language="text")
                    for fig in figs:
                        st.pyplot(fig)
        cc1, cc2 = st.columns([10,1])
        with cc2:
            if st.button("⭐ 收藏", key=f"collect_{fsel}"):
                item = {
                    "chap": chap_full,
                    "file": fsel,
                    "code": code,
                    "add_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                if not any(c["chap"] == item["chap"] and c["file"] == item["file"] for c in st.session_state.collection):
                    st.session_state.collection.append(item)
                    st.success("收藏成功！")
                else:
                    st.info("已收藏过该文件")
    else:
        st.info("暂无Python代码文件")
    st.markdown('</div>', unsafe_allow_html=True)

    render_auto_code_exercise(chap_key)

    st.markdown("""<div class="ai-chat-zone"><span class="ai-zone-title">🤖 当前章节智能问答</span>""", unsafe_allow_html=True)
    hiskey = f"chap_{chap_key}_history"
    if hiskey not in st.session_state:
        st.session_state[hiskey] = []
    user_input = st.text_input("提问/答疑(仅针对此章节)", key="chapter_ai_input")
    if st.button("提交章节提问", key="ask_ai_chap", disabled=st.session_state.loading) and user_input.strip():
        st.session_state.loading = True
        try:
            with st.spinner("AI正在解答..."):
                answer = get_coze_answer(user_input)
            current_time = datetime.datetime.now().strftime("%H:%M")
            st.session_state[hiskey].append({
                "role":"user",
                "content":user_input,
                "time": current_time
            })
            st.session_state[hiskey].append({
                "role":"ai",
                "content":answer,
                "time": current_time
            })
        finally:
            st.session_state.loading = False
    for h in st.session_state[hiskey][-10:]:
        time_str = h.get("time", "")
        if h["role"] == "user":
            st.markdown(f"""<div class="user-chat-block">
            <span>{h["content"]}</span>
            <span class="user-avatar">👤</span>
            <span class="chat-timestamp">{time_str}</span>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="ai-chat-block">
            <span class="ai-avatar">🤖</span> <span>{h["content"]}</span>
            <span class="chat-timestamp" style="margin-left:45px;">{time_str}</span>
            </div>""", unsafe_allow_html=True)
    if st.session_state[hiskey]:
        col_cls, col_empty = st.columns([2, 10])
        with col_cls:
            if st.button("清空章节对话", key=f"cls_chathis_{chap_key}"):
                st.session_state[hiskey] = []
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "✅ 学习进度":
    st.markdown(f"""<div class="card-primary">
        <h1 style='margin:0;font-size:34px;'>📚 学习进度</h1>
        <p style="font-size:18px; margin-top:10px;">你的学习旅程一目了然</p>
    </div>""", unsafe_allow_html=True)
    total_progress = sum(st.session_state.progress.values()) / len(st.session_state.progress) * 100
    st.markdown('<div class="card-white"><h4>📈 整体完成进度</h4>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width:{total_progress}%"></div>
        </div>
        <p>已完成 {sum(st.session_state.progress.values())}/8 章节 ({total_progress:.1f}%)</p>
    """, unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top:20px;">📋 章节完成状态</h4>', unsafe_allow_html=True)
    chap_cols = st.columns(2)
    for idx, (chap_key, chap_name) in enumerate(CHAPTER_NAMES.items()):
        with chap_cols[idx % 2]:
            is_done = st.session_state.progress.get(chap_key, False)
            status_icon = "✅" if is_done else "🔲"
            chap_progress = 100 if is_done else 0
            st.markdown(f"""
                <div style="display:flex;flex-direction:column;padding:12px;border-radius:12px;background:#f8f5ff;margin:8px 0;">
                    <div style="display:flex;align-items:center;margin-bottom:4px;">
                        <span style="font-size:18px;margin-right:10px;">{status_icon}</span>
                        <span>{chap_name}</span>
                    </div>
                    <div class="progress-bar" style="height:8px;margin:0;">
                        <div class="progress-fill" style="width:{chap_progress}%"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            btn_col1, btn_col2 = st.columns([1, 3])
            with btn_col1:
                if st.button(f"{'取消' if is_done else '标记'}完成", key=f"progress_{chap_key}", type="secondary"):
                    st.session_state.progress[chap_key] = not is_done
                    st.rerun()

    st.markdown('<h4 style="margin-top:30px;">📝 练习题完成情况</h4>', unsafe_allow_html=True)
    total_exercises = 0
    completed_exercises = 0
    correct_exercises = 0
    exercise_stats = {}
    for chap_key, exercises in CODE_EXERCISES.items():
        total = len(exercises)
        exercise_stats[chap_key] = {"total": total, "completed": 0, "correct": 0}
        total_exercises += total
        for idx in range(total):
            exercise_id = f"{chap_key}_exercise_{idx}"
            if f"{exercise_id}_result" in st.session_state:
                exercise_stats[chap_key]["completed"] += 1
                completed_exercises += 1
                if st.session_state[f"{exercise_id}_result"]:
                    exercise_stats[chap_key]["correct"] += 1
                    correct_exercises += 1
    exercise_completion_rate = (completed_exercises / total_exercises * 100) if total_exercises > 0 else 0
    exercise_accuracy_rate = (correct_exercises / completed_exercises * 100) if completed_exercises > 0 else 0
    st.markdown(f"""
        <div style="background:#fdfaff;padding:20px;border-radius:16px;margin:16px 0;">
            <div style="display:flex;justify-content:space-between;margin-bottom:8px;">
                <span style="font-weight:600;">练习题总进度：</span>
                <span>{completed_exercises}/{total_exercises} 题 ({exercise_completion_rate:.1f}%)</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width:{exercise_completion_rate}%"></div>
            </div>
            <div style="display:flex;justify-content:space-between;margin-top:12px;margin-bottom:8px;">
                <span style="font-weight:600;">练习题正确率：</span>
                <span>{correct_exercises}/{completed_exercises} 题 ({exercise_accuracy_rate:.1f}%)</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width:{exercise_accuracy_rate}%;background:linear-gradient(90deg,#10b981,#34d399);"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<h5 style="margin-top:20px;">各章节练习详情：</h5>', unsafe_allow_html=True)
    exercise_cols = st.columns(2)
    for idx, (chap_key, stats) in enumerate(exercise_stats.items()):
        with exercise_cols[idx % 2]:
            chap_name = CHAPTER_NAMES.get(chap_key, chap_key)
            completion_rate = (stats["completed"] / stats["total"] * 100) if stats["total"] > 0 else 0
            accuracy_rate = (stats["correct"] / stats["completed"] * 100) if stats["completed"] > 0 else 0
            st.markdown(f"""
                <div style="background:#f8f5ff;padding:16px;border-radius:12px;margin:8px 0;">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                        <span style="font-weight:600;">{chap_name}</span>
                        <span>{stats["completed"]}/{stats["total"]}</span>
                    </div>
                    <div class="progress-bar" style="height:6px;margin-bottom:6px;">
                        <div class="progress-fill" style="width:{completion_rate}%"></div>
                    </div>
                    <div style="font-size:12px;color:#6b7280;">
                        正确率：{accuracy_rate:.1f}% ({stats["correct"]}/{stats["completed"]})
                    </div>
                </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-dark"><h4>📊 学习统计</h4>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    completed = sum(st.session_state.progress.values())
    uncompleted = len(st.session_state.progress) - completed
    with c1: st.metric("已完成章节", completed)
    with c2: st.metric("未完成章节", uncompleted)
    with c3: st.metric("完成练习题数", completed_exercises)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "⭐ 我的收藏":
    st.markdown(f"""<div class="card-primary">
        <h1 style='margin:0;font-size:34px;'>⭐ 我的收藏</h1>
        <p style="font-size:18px; margin-top:10px;">保存你感兴趣的代码片段</p>
    </div>""", unsafe_allow_html=True)
    if not st.session_state.collection:
        st.markdown('<div class="card-white"><h4>暂无收藏内容</h4><p>在章节学习页面收藏代码片段后会显示在这里</p></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="card-white">', unsafe_allow_html=True)
        with st.expander("🔍 筛选收藏", expanded=False):
            chap_filter = st.selectbox("按章节筛选", ["全部"] + list(CHAPTER_NAMES.values()), key="col_chap_filter")
            search_key = st.text_input("搜索文件名", key="col_search")
        filtered_collection = st.session_state.collection
        if chap_filter != "全部":
            filtered_collection = [c for c in filtered_collection if c["chap"] == chap_filter]
        if search_key:
            filtered_collection = [c for c in filtered_collection if search_key in c["file"]]
        if not filtered_collection:
            st.info("没有匹配的收藏内容")
        else:
            for idx, item in enumerate(filtered_collection):
                st.markdown(f"""
                    <div style="border-bottom:1px solid #f3e8ff;padding:16px 0;">
                        <div style="display:flex;justify-content:space-between;align-items:center;">
                            <h5 style="margin:0;color:#7c3aed;">{item['chap']} - {item['file']}</h5>
                            <span style="color:#9333ea;font-size:12px;">收藏时间：{item.get('add_time', '未知')}</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                with st.expander("📝 查看代码", expanded=False):
                    st.code(item['code'], language="python", line_numbers=True)
                col_ops = st.columns([1, 1, 10])
                with col_ops[0]:
                    if st.button("🗑️ 取消收藏", key=f"del_col_{idx}"):
                        original_idx = next(i for i, c in enumerate(st.session_state.collection) if c["chap"] == item["chap"] and c["file"] == item["file"])
                        st.session_state.collection.pop(original_idx)
                        st.success("已取消收藏！")
                        st.rerun()
                with col_ops[1]:
                    if st.button("📋 复制代码", key=f"copy_col_{idx}"):
                        try:
                            pyperclip.copy(item['code'])
                            st.success("代码已复制到剪贴板！")
                        except:
                            st.code(item['code'], language="python", line_numbers=True)
                            st.info("复制功能需要安装pyperclip库，已显示代码供手动复制")
                st.markdown('<hr style="border:none;border-top:1px solid #f3e8ff;margin:16px 0;">', unsafe_allow_html=True)
        col_batch = st.columns([1, 10])
        with col_batch[0]:
            if st.session_state.collection:
                if st.button("🗑️ 清空收藏"):
                    confirm_clear = st.checkbox("确认清空所有收藏？", key="confirm_clear_col")
                    if confirm_clear:
                        st.session_state.collection = []
                        st.success("已清空所有收藏！")
                        st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "❌ 错题本":
    st.markdown(f"""<div class="card-primary">
        <h1 style='margin:0;font-size:34px;'>❌ 错题本</h1>
        <p style="font-size:18px; margin-top:10px;">记录你的错题，巩固知识点</p>
    </div>""", unsafe_allow_html=True)
    if not st.session_state.wrong_book:
        st.markdown('<div class="card-white"><h4>暂无错题</h4><p>答错每日一题后会自动添加到这里</p></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="card-white">', unsafe_allow_html=True)
        for idx, wrong in enumerate(st.session_state.wrong_book):
            st.markdown(f"""
                <div style="border-bottom:1px solid #f3e8ff;padding:16px 0;">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                        <h5 style="margin:0;">错题 {idx+1}</h5>
                        <span style="color:#9333ea;font-size:12px;">添加时间：{wrong.get('add_time', '未知')}</span>
                    </div>
                    <p style="margin:4px 0;"><strong>问题：</strong>{wrong['题目']}</p>
                    <p style="margin:4px 0;color:#dc2626;"><strong>你的答案：</strong>{wrong['user_answer']}</p>
                    <p style="margin:4px 0;color:#059669;"><strong>正确答案：</strong>{wrong['correct_answer']}</p>
                </div>
            """, unsafe_allow_html=True)
            col_del = st.columns([1, 10])
            with col_del[0]:
                if st.button("🗑️ 删除此题", key=f"del_wrong_{idx}"):
                    st.session_state.wrong_book.pop(idx)
                    st.success("已删除此题！")
                    st.rerun()
        if st.session_state.wrong_book:
            st.markdown('<hr style="margin:20px 0;">', unsafe_allow_html=True)
            confirm_clear = st.checkbox("确认清空所有错题？", key="confirm_clear_wrong")
            if st.button("🗑️ 清空错题本", type="secondary") and confirm_clear:
                st.session_state.wrong_book = []
                st.success("已清空所有错题！")
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <p>©视“见”AI - 人工智能可视化学习平台 | 基于Streamlit构建</p>
</div>
""", unsafe_allow_html=True)
