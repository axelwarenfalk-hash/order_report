import pandas as pd
from pandas.testing import assert_frame_equal

from order_report.report import (
    create_overview_report,
    create_returns_report_by,
    create_sales_report_by,
)


def test_create_overview_report_summarizes_orders() -> None:
    orders = pd.DataFrame(
        {
            "order_id": ["O0001", "O0001", "O0002"],
            "discounted_value": [100.126, 50.129, 25.0],
            "returned": [True, False, True],
        }
    )
    expected = pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [175.26, 2.0, 2.0],
        }
    )

    result = create_overview_report(orders)

    assert_frame_equal(result, expected)


def test_create_sales_report_by_groups_and_sorts_sales() -> None:
    orders = pd.DataFrame(
        {
            "order_id": ["O0001", "O0002", "O0003"],
            "product_category": [
                "Electronics",
                "Furniture",
                "Electronics",
            ],
            "discounted_value": [100.126, 80.0, 50.129],
            "returned": [True, False, False],
        }
    )
    expected = pd.DataFrame(
        {
            "product_category": ["Electronics", "Furniture"],
            "order_count": [2, 1],
            "total_sales": [150.26, 80.0],
            "returns": [1, 0],
            "return_rate": [0.5, 0.0],
        }
    )

    result = create_sales_report_by(orders, "product_category")

    assert_frame_equal(result, expected)


def test_create_returns_report_by_groups_and_sorts_returns() -> None:
    orders = pd.DataFrame(
        {
            "order_id": ["O0001", "O0002", "O0003", "O0004"],
            "product_category": [
                "Electronics",
                "Electronics",
                "Furniture",
                "Furniture",
            ],
            "returned": [True, False, True, True],
        }
    )
    expected = pd.DataFrame(
        {
            "product_category": ["Furniture", "Electronics"],
            "order_count": [2, 2],
            "returns": [2, 1],
            "return_rate": [1.0, 0.5],
        }
    )

    result = create_returns_report_by(orders, "product_category")

    assert_frame_equal(result, expected)
