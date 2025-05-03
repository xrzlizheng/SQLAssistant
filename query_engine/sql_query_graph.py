from langchain_community.utilities import SQLDatabase
from langchain import hub
from typing import TypedDict
import os
from typing_extensions import Annotated
from langgraph.graph import START, StateGraph
from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from query_engine.model import init_llm
from langchain.prompts import PromptTemplate
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from data_sources.db_connections import get_database_configs
from PIL import Image
llm = init_llm()

prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")

# 连接到SQLite数据库
class State(TypedDict):
    question: str
    query: str
    result: str
    answer: str
    db: SQLDatabase
    db_info: str

class QueryOutput(TypedDict):
    query: Annotated[str, ..., "语法有效的SQL查询。"]

def choose_db(state: State) -> str:
    """
    选择要查询的数据库。
    """
    # 这里你可以实现基于问题选择数据库的逻辑
    # 目前，我们只是返回当前数据库

    db_configs = get_database_configs()

    prompt_template = PromptTemplate.from_template(
        """"
        你是一个数据库路由器。请选择最适合回答用户问题的数据库。

        数据库：
        {db_descriptions}

        问题：{question}

        仅返回最合适的数据库名称（例如：bigquery, sqlite, redshift）。
        """
    )

    prompt = prompt_template.invoke(
        {"db_descriptions": db_configs, "question": state["question"]}
    )

    answer = llm.invoke(prompt)

    chosen_db = db_configs[answer.content]

    return {"db": chosen_db["db"], "db_info": chosen_db["table_info"]}

def write_query(state: State) -> str:

    prompt = prompt_template.invoke(
        {
            "dialect": state["db"].dialect,
            "top_k": 5,
            "table_info": state["db_info"],
            "input": state["question"],
        }
    )
    result = llm.with_structured_output(QueryOutput).invoke(prompt)

    return {"query": result["query"]}

def execute_query(state: State):
    execute_query_tool = QuerySQLDatabaseTool(db=state["db"])
    return {"result": execute_query_tool.invoke(state["query"])}

def generate_answer(state: State):
    prompt = (
        "根据以下用户问题、相应的SQL查询和SQL结果，回答用户问题。\n\n"
        f'问题：{state["question"]}\n'
        f'SQL查询：{state["query"]}\n'
        f'SQL结果：{state["result"]}'
    )
    response = llm.invoke(prompt)

    return {"answer": response.content}


def answer_question(question: str) -> str:
    """
    给定一个问题，返回答案。
    """
    graph_builder = StateGraph(State).add_sequence(
        [choose_db,write_query, execute_query, generate_answer]
    )
    graph_builder.add_edge(START, "choose_db")
    graph = graph_builder.compile()

    return graph.stream({"question": question})

