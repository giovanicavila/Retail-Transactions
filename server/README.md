# Retail Transactions - Data Science & API

Projeto de análise exploratória de dados (EDA) e API para transações de varejo.

---

## Estrutura do Projeto

Estrutura baseada em [FastAPI Best Practices - zhanymkanov](https://github.com/zhanymkanov/fastapi-best-practices#project-structure):

```
retail_transaction_data_science/
├── src/
│   ├── sales/                  # Módulo de vendas (domínio principal)
│   │   ├── router.py           # Endpoints do módulo
│   │   ├── schemas.py          # Modelos Pydantic (request/response)
│   │   ├── service.py          # Lógica de negócio
│   │   ├── dependencies.py     # Dependências do módulo
│   │   ├── constants.py        # Constantes do módulo
│   │   ├── exceptions.py       # Exceções do módulo
│   │   └── utils.py            # Funções utilitárias (ex: geração de gráficos)
│   ├── config.py               # Configurações globais (pydantic-settings)
│   ├── exceptions.py           # Exceções globais
│   └── main.py                 # Inicialização do FastAPI
├── tests/
│   └── sales/                  # Testes do módulo de vendas
├── requirements/
│   ├── base.txt                # Dependências de produção
│   ├── dev.txt                 # Dependências de desenvolvimento
│   └── prod.txt                # Dependências extras para produção
├── .env                        # Variáveis de ambiente (não versionar)
├── learning.ipynb              # Notebook de aprendizado
└── retail_transaction.ipynb    # Notebook de EDA
```

---

## Setup

### 1. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements/base.txt
# Para desenvolvimento:
pip install -r requirements/dev.txt
```

### 3. Rodar a API

```bash
uvicorn src.main:app --reload
```

A documentação estará disponível em: http://localhost:8000/docs

---

## Endpoints disponíveis

### `GET /sales/by-hour`

Retorna a quantidade de itens vendidos em um intervalo de horas.

| Parâmetro    | Tipo    | Descrição                                    |
|--------------|---------|----------------------------------------------|
| `start_hour` | int     | Hora de início (0-23)                        |
| `end_hour`   | int     | Hora de fim (1-24)                           |
| `save_chart` | bool    | Salva o gráfico em `frontend/static/`        |

**Exemplo de uso:**
```
GET /sales/by-hour?start_hour=6&end_hour=7&save_chart=true
```

**Resposta:**
```json
{
  "data": [
    { "hour_range": "06:00-07:00", "total_items": 420 }
  ],
  "chart_path": "../frontend/static/sales_06_07.png"
}
```

---

## Variáveis de Ambiente (`.env`)

| Variável              | Padrão                        | Descrição                              |
|-----------------------|-------------------------------|----------------------------------------|
| `ENVIRONMENT`         | `local`                       | Ambiente da aplicação                  |
| `DATASET_PATH`        | `Retail_Transactions_Dataset.csv` | Caminho para o dataset             |
| `FRONTEND_STATIC_DIR` | `../frontend/static`          | Diretório para salvar gráficos         |
| `CORS_ORIGINS`        | `["http://localhost:3000"]`   | Origens permitidas pelo CORS           |

---

## Convenções adotadas

- Cada módulo/domínio possui seu próprio `router.py`, `schemas.py`, `service.py`, `exceptions.py` e `utils.py`
- Importações entre módulos usam o nome explícito: `from src.sales import service as sales_service`
- Configurações via `pydantic-settings` com leitura do `.env`
- Ambiente `production` desativa a documentação (`/docs` e `/redoc`)
