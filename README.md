<p align="center">
  <!-- Python 3.12+ -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+" />
  </a>

  <!-- FastAPI -->
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  </a>

  <!-- SQLAlchemy -->
  <a href="https://www.sqlalchemy.org/">
    <img src="https://img.shields.io/badge/SQLAlchemy-FF4136?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
  </a>

  <!-- SQLite -->
  <a href="https://www.sqlite.org/">
    <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  </a>

  <!-- LangChain -->
  <a href="https://docs.langchain.com/docs/">
    <img src="https://img.shields.io/badge/LangChain-8B4513?style=for-the-badge&logo=python&logoColor=white" alt="LangChain" />
  </a>

  <!-- OpenAI -->
  <a href="https://platform.openai.com/">
    <img src="https://img.shields.io/badge/OpenAI-6A0DAD?style=for-the-badge&logo=openai&logoColor=white" alt="OpenAI" />
  </a>

  <!-- Bootstrap 5 -->
  <a href="https://getbootstrap.com/">
    <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap 5" />
  </a>

  <!-- HTML + JavaScript -->
  <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5">
    <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML" />
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  </a>
</p>

# 📊 Sales Insights API

![image](https://github.com/user-attachments/assets/6d60b318-ae77-4bfb-8991-db27df419be1)


Este é um projeto API REST construída com **FastAPI + LangChain + OpenAI + SQLAlchemy** para **análise de vendas** em linguagem natural, retornando insights inteligentes consultando dados reais de um banco relacional. Inclui **frontend responsivo em Bootstrap**, permitindo consultas diretas sem necessidade de ferramentas externas.

---

## 🚀 Funcionalidades

✅ API REST construída em **FastAPI**  
✅ Consulta de insights em **linguagem natural** usando **LangChain + OpenAI + RAG**  
✅ Endpoint para listar os **5 produtos mais vendidos no último mês**  
✅ Integração com **SQLite + SQLAlchemy**  
✅ Frontend elegante em **Bootstrap 5**  
✅ **Swagger e ReDoc** gerados automaticamente para documentação  
✅ Loader **“Pensando...”** durante o processamento de requisições  
✅ Retorno formatado para fácil leitura e apresentação

---

## 💡 Exemplos de perguntas

- "Qual foi o produto mais vendido no último mês?"
- "Quais produtos mais venderam na última semana?"
- "Quantas vendas ocorreram em junho?"

---

## 📸 Prints

| ![image](https://github.com/user-attachments/assets/79a2b2bf-abce-459b-9637-91f737d08b49) | ![image](https://github.com/user-attachments/assets/27385b06-982f-48b4-8f4e-7ae2e5971f1a) | ![image](https://github.com/user-attachments/assets/78e85b5f-6504-401c-a9fb-11fcd165e1ab) |
|---|---|---|

---

## 🛠️ Tecnologias utilizadas

- Python 3.12+
- FastAPI
- SQLAlchemy
- SQLite
- LangChain
- OpenAI
- Bootstrap 5
- HTML + JavaScript

---

## 📂 Estrutura de pastas

```bash
sales_insights_api/
│
├── app/                  # Backend FastAPI
│   ├── __init__.py       # Torna a pasta um pacote Python
│   ├── main.py           # Inicializa o FastAPI, define rotas e serve frontend
│   ├── database.py       # Configuração do SQLAlchemy e conexão com SQLite
│   ├── models.py         # Modelos ORM (ex: tabela 'sales')
│   ├── crud.py           # Funções CRUD para consultas no banco
│   ├── langchain_agent.py # Integra LangChain + OpenAI para processar perguntas
│   ├── schemas.py        # (Opcional) Schemas Pydantic para validações
│
├── frontend/             # Frontend Bootstrap
│   └── index.html        # Interface de consulta com loaders e cards
│
├── .env                  # Variáveis de ambiente (OPENAI_API_KEY)
├── sales_data.sql        # Script SQL para popular o banco
├── sales.db              # Banco SQLite gerado/populado
├── requirements.txt      # Dependências Python
└── README.md             # Este arquivo de documentação
```

## ⚙️ Instalação e execução
1️⃣ Clone o repositório:
```bash
git clone https://github.com/seuusuario/Sales-Insights-Api.git
cd Sales-Insights-Api
```

2️⃣ Crie o ambiente virtual:
```bash
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/Mac
source venv/bin/activate
```

3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

4️⃣ Configure seu .env com a chave da OpenAI:
```bash
OPENAI_API_KEY=sua_chave_aqui
```

5️⃣ Crie e popule o banco SQLite:
```bash
sqlite3 sales.db < sales_data.sql
```

6️⃣ Execute o servidor:
```bash
uvicorn app.main:app --reload
```

| **Descrição**                     | **Endereço**                                     |
|----------------------------------|--------------------------------------------------|
| 🌐 Acesso ao Frontend           | [http://127.0.0.1:8000/](http://127.0.0.1:8000/)       |
| ✅ Documentação Swagger           | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)          |
| ✅ Documentação ReDoc             | [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)        |
