from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, JSONResponse

from app import models, crud, langchain_agent
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# ✅ Primeiro crie a instância
app = FastAPI(
    title="Sales Insights API",
    description="API para insights de vendas utilizando FastAPI, SQLAlchemy e LangChain",
    version="1.0"
)

# ✅ Só depois monte os diretórios estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

# ✅ Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para top produtos
@app.get("/top-products")
def read_top_products(db: Session = Depends(get_db)):
    return crud.get_top_products_last_month(db)

# Endpoint para insights de vendas
@app.get("/sales-insights")
def get_sales_insights(question: str = Query(..., description="Pergunta sobre as vendas")):
    result = langchain_agent.process_question(question)

    response_data = {
        "question": question,
        "answer": {
            "summary": f"A resposta para sua pergunta é: {result}.",
            "raw": result
        }
    }
    return JSONResponse(content=response_data)

# Redirecionamento para o frontend
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/frontend")
