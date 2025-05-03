import streamlit as st
from langchain.prompts import PromptTemplate
from query_engine.sql_query_graph import answer_question  # 你构建的自定义图

# --- 自定义 CSS ---
# --- 自定义 CSS ---
import streamlit as st

st.title("📊 SQL 助手")

# 侧边栏：数据源上下文
st.sidebar.title("🗂️ 数据源")

st.sidebar.markdown("""
**已连接数据库:**

- `sample_data_dev.tickit`  
  票务平台数据 — 活动、用户、场地、列表和销售  

- `sqlite` (Northwind)  
  经典零售数据集 — 客户、订单、产品、员工  

- `bigquery-public-data.samples`  
  Google BigQuery 公共样本 — 包括 `natality`, `github_nested`, `weather_stations` 等

💡 *尝试提问:*  
- "列出所有来自德国的客户。"  
- "哪个活动的票务销售最多？"  
- "natality 数据集中的平均出生体重是多少？"
""")


# --- 初始化会话状态 ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # 每个项目是一个字典: {"question", "sql", "answer"}

# --- 聊天界面渲染 (从上到下) ---
for item in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(f"**🧠 问题:** {item['question']}")
    with st.chat_message("assistant"):
        st.markdown(f"**🛠️ SQL 查询:**\n```sql\n{item['sql']}\n```")
        st.markdown(f"**🤖 回答:** {item['answer']}")

# --- 底部用户输入 ---
user_question = st.chat_input("提出您的数据问题:")

# --- 运行图并更新内存 ---
if user_question:
    with st.spinner("思考中..."):

        result = {}
        for update in answer_question(user_question):  # 你的流式图
            result.update(update)

        sql_query = result.get("write_query", {}).get("query", "未生成SQL查询。")
        answer = result.get("generate_answer", {}).get("answer", "无可用答案。")

        # 保存到内存
        st.session_state.chat_history.append({
            "question": user_question,
            "sql": sql_query,
            "answer": answer
        })
       # st.experimental_rerun()
    for item in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(f"**🧠 问题:** {item['question']}")
        with st.chat_message("assistant"):
            st.markdown(f"**🛠️ SQL 查询:**\n```sql\n{item['sql']}\n```")
            st.markdown(f"**🤖 回答:** {item['answer']}")