from fastapi import APIRouter, Query

from src.sales import service
from src.sales.exceptions import InvalidHourRange
from src.sales.schemas import SalesByHourResponse

router = APIRouter()


@router.get(
    "/by-hour",
    response_model=SalesByHourResponse,
    summary="Vendas por intervalo de hora",
    description=
    "Retorna a quantidade de itens vendidos em um intervalo de horas e opcionalmente salva o gráfico no frontend.",
)
async def get_sales_by_hour(
    start_hour: int = Query(ge=0, le=23, description="Hora de início (0-23)"),
    end_hour: int = Query(ge=1, le=24, description="Hora de fim (1-24)"),
    save_chart: bool = Query(
        default=False, description="Salvar gráfico no diretório frontend"),
):
    if start_hour >= end_hour:
        raise InvalidHourRange()

    return await service.get_sales_by_hour_range(start_hour, end_hour,
                                                 save_chart)
