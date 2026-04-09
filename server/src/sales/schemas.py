from pydantic import BaseModel, Field


class SalesByHourItem(BaseModel):
    hour_range: str
    total_items: int


class SalesByHourResponse(BaseModel):
    data: list[SalesByHourItem]
    chart_path: str | None = None


class SalesByHourQuery(BaseModel):
    start_hour: int = Field(ge=0, le=23, description="Hora de início (0-23)")
    end_hour: int = Field(ge=1, le=24, description="Hora de fim (1-24)")
    save_chart: bool = Field(default=False,
                             description="Salvar gráfico no frontend")
