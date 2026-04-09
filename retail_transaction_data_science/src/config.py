from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENVIRONMENT: str = "local"
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000", "http://localhost:5173"
    ]
    DATASET_PATH: str = "Retail_Transactions_Dataset.csv"
    FRONTEND_STATIC_DIR: str = "../frontend/static"

    class Config:
        env_file = ".env"


settings = Config()
