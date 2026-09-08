import logging
import pandas as pd
from pathlib import Path


logger = logging.getLogger(__name__)


def load_orders(input_path: Path) -> pd.DataFrame:
    logger.info("Läser in orderdata från %s", input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Datafilen saknas: {input_path}")

    try:
        orders = pd.read_csv(input_path)
    except pd.errors.EmptyDataError as error:
        raise ValueError(f"Datafilen är tom: {input_path}") from error

    logger.info("Läste in %d rader från %s", len(orders), input_path)
    return orders


def save_report(report: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(output_path, index=False)
    logger.info("Sparade %s", output_path)
