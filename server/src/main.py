from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.sales.router import router as sales_router

app = FastAPI(
    title="Retail Transactions API",
    description="API para análise de transações de varejo",
    version="1.0.0",
    openapi_url="/openapi.json"
    if settings.ENVIRONMENT != "production" else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sales_router, prefix="/sales", tags=["Sales"])


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
