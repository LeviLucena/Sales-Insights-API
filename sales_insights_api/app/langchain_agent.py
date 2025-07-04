from langchain_openai import OpenAI
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY não definida no .env.")

# Conectar ao banco SQLite
db_engine = create_engine("sqlite:///./sales.db")
db = SQLDatabase.from_uri("sqlite:///./sales.db")

# Inicializar o LLM da OpenAI
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

# Criar o agente de consulta SQL
agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

# Função para processar a pergunta do usuário
def process_question(question: str):
    response = agent.invoke({
        "input": (
            f"{question}. "
            f"Retorne em português o NOME do produto mais vendido e o total de vendas em números, "
            f"não o id, utilizando join com a tabela de produtos."
        )
    })
    return response["output"]

