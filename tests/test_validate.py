import pandas as pd
import pytest

from order_report.validate import validate_orders


def test_validate_orders_missing_columns() -> None:
    orders = pd.DataFrame({"order_id": [1]})
    expected = "Följande kolumner saknas"

    with pytest.raises(ValueError, match=expected):
        validate_orders(orders)


def test_validate_orders_empty_data() -> None:
    orders = pd.DataFrame(
        columns=[
            "order_id", "order_date", "customer_id", "region",
            "product_category", "quantity", "unit_price", "discount", "returned",
        ]
    )
    expected = "Orderdatan är tom"

    with pytest.raises(ValueError, match=expected):
        validate_orders(orders)


def test_validate_orders_invalid_number(caplog) -> None:
    orders = pd.DataFrame(
        {
            "order_id": [1],
            "order_date": ["2026-01-01"],
            "customer_id": [101],
            "region": ["North"],
            "product_category": ["Books"],
            "quantity": ["invalid"],
            "unit_price": [100.0],
            "discount": [0.1],
            "returned": [False],
        }
    )
    expected = "Kolumnen quantity innehåller ett eller flera rader som inte är ett tal."

    validate_orders(orders)

    assert expected in caplog.text
