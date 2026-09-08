import pandas as pd
import pytest
from order_report.validate import validate_orders


def make_orders(**overrides: object) -> pd.DataFrame:
    data = {
        "order_id": "O0001",
        "order_date": "2026-01-04",
        "customer_id": "C018",
        "region": "South",
        "product_category": "Electronics",
        "quantity": 2.0,
        "unit_price": 799.0,
        "discount": 0.0,
        "returned": True,
    }
    data.update(overrides)
    return pd.DataFrame({column: [value] for column, value in data.items()})


def test_validate_orders_accepts_valid_orders() -> None:
    orders = make_orders()
    validate_orders(orders)


