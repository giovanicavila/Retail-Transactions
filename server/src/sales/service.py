import os
from pathlib import Path

import pandas as pd

from src.config import settings
from src.exceptions import DatasetNotFound
from src.sales.exceptions import NoDataFound
from src.sales.schemas import SalesByHourItem, SalesByHourResponse
from src.sales.utils import generate_sales_chart


def get_dataset() -> pd.DataFrame:
    path = Path(settings.DATASET_PATH)
    if not path.exists():
        raise DatasetNotFound()
    return pd.read_csv(path)


async def get_sales_by_hour_range(start_hour: int, end_hour: int,
                                  save_chart: bool) -> SalesByHourResponse:
    dataset = get_dataset()

    date_col = pd.to_datetime(dataset["Date"])
    hour_col = date_col.dt.hour

    mask = (hour_col >= start_hour) & (hour_col < end_hour)
    filtered = dataset[mask]

    if filtered.empty:
        raise NoDataFound()

    sales = filtered.groupby(
        hour_col[mask])["Total_Items"].count().reset_index()
    sales.columns = ["hour", "total_items"]

    data = [
        SalesByHourItem(
            hour_range=
            f"{int(row['hour']):02d}:00-{int(row['hour']) + 1:02d}:00",
            total_items=int(row["total_items"]),
        ) for _, row in sales.iterrows()
    ]

    chart_path = None
    if save_chart:
        chart_path = generate_sales_chart(data, start_hour, end_hour)

    return SalesByHourResponse(data=data, chart_path=chart_path)
