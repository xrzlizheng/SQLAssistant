# SQL助手

基于LangChain和LLM技术构建的智能SQL查询助手，可以将自然语言问题转换为SQL查询，并提供友好的答案解释。

## 🌟 主要功能

- 🗣️ **自然语言转SQL**：将普通问题自动转换为准确的SQL查询
- 🔄 **多数据库支持**：连接SQLite、BigQuery和Redshift等多种数据源  
- 📊 **交互式界面**：使用Streamlit构建的直观界面，轻松提问和查看结果
- 🤖 **智能解释**：自动解释查询结果，以通俗易懂的方式呈现

## 🛠️ 技术栈

- **LangChain**：构建LLM应用程序框架
- **LangGraph**：用于创建有状态的推理流程
- **Streamlit**：用户界面
- **SQLDatabase**：数据库连接和查询
- **大语言模型(LLM)**：用于理解问题、生成SQL和解释结果

## 📋 项目结构

```
SQL助手/
├── streamlit.py             # Streamlit应用主入口
├── query_engine/            # 查询引擎
│   ├── model.py             # LLM模型初始化
│   └── sql_query_graph.py   # LangGraph查询流程
├── data_sources/            # 数据源配置
│   ├── db_connections.py    # 数据库连接配置
│   └── aws_tickit_metadata.py # Redshift数据库元数据
```

## 🚀 安装指南

1. 克隆仓库
```bash
git clone https://github.com/xrzlizheng/SQLAssistant.git
cd SQLAssistant
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建`.env`文件并配置必要的API密钥和数据库连接信息：
```
# LLM API配置
OPENAI_API_KEY=your_openai_api_key

# Redshift配置（如需连接）
AMAZON_REDSHIFT_USER=your_redshift_user
AMAZON_REDSHIFT_PASSWORD=your_redshift_password
AMAZON_REDSHIFT_ENDPOINT=your_redshift_endpoint
```

## 🏃‍♂️ 使用方法

1. 启动Streamlit应用
```bash
streamlit run streamlit.py
```

2. 在浏览器中访问应用（通常是`http://localhost:8501`）

3. 在对话框中输入自然语言问题，如：
   - "列出所有来自德国的客户"
   - "哪个活动的票务销售最多？"
   - "natality数据集中的平均出生体重是多少？"

## 📝 示例

用户问题：
> "列出销售额最高的前5个事件"

生成的SQL：
```sql
SELECT e.eventname, SUM(s.pricepaid) as total_sales
FROM sample_data_dev.tickit.sales s
JOIN sample_data_dev.tickit.event e ON s.eventid = e.eventid
GROUP BY e.eventname
ORDER BY total_sales DESC
LIMIT 5;
```

## 📄 许可证

[MIT](LICENSE) 
