import os
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("Agg")

from src.config import settings


def generate_sales_chart(data: list, start_hour: int, end_hour: int) -> str:
    labels = [item.hour_range for item in data]
    values = [item.total_items for item in data]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labels, values, color="steelblue")
    ax.set_title(f"Vendas por hora ({start_hour:02d}:00 - {end_hour:02d}:00)")
    ax.set_xlabel("Intervalo de Hora")
    ax.set_ylabel("Total de Itens Vendidos")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_dir = Path(settings.FRONTEND_STATIC_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"sales_{start_hour:02d}_{end_hour:02d}.png"
    filepath = output_dir / filename
    fig.savefig(filepath)
    plt.close(fig)

    return str(filepath)
