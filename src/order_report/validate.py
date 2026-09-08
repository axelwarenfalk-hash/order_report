import pandas as pd
import logging

REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
}

NUMERIC_COLUMNS = ("quantity", "unit_price", "discount")

logger = logging.getLogger(__name__)

def validate_orders(orders: pd.DataFrame) -> None:
    if not REQUIRED_COLUMNS.issubset(orders.columns):
        missing_columns = REQUIRED_COLUMNS - set(orders.columns)
        raise ValueError(f"Följande kolumner saknas: {missing_columns}")

    if orders.empty:
        raise ValueError("Orderdatan är tom")

    for column in NUMERIC_COLUMNS:
        try:
            pd.to_numeric(orders[column], errors="raise")
        except (ValueError, TypeError):
            logger.warning(f"Kolumnen {column} innehåller ett eller flera rader som inte är ett tal.")


