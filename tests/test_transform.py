import pandas as pd
from pandas.testing import assert_frame_equal

from order_report.transform import calculate_order_values, clean_orders


def test_clean_orders_cleans_order_data() -> None:
    orders = pd.DataFrame(
        {
            "region": [" north ", None],
            "product_category": [" electronics ", None],
            "returned": [" yes ", None],
            "quantity": ["invalid", "2"],
            "unit_price": ["100", None],
            "discount": ["invalid", "0.1"],
        }
    )
    expected = pd.DataFrame(
        {
            "region": ["North", "Unknown"],
            "product_category": ["Electronics", "Unknown"],
            "returned": [True, False],
            "quantity": [1.0, 2.0],
            "unit_price": [100.0, 100.0],
            "discount": [0.0, 0.1],
        }
    )

    result = clean_orders(orders)

    assert_frame_equal(result, expected)


def test_calculate_order_values_adds_order_and_discounted_values() -> None:
    orders = pd.DataFrame(
        {
            "quantity": [2.0],
            "unit_price": [100.0],
            "discount": [0.25],
        }
    )
    expected = pd.DataFrame(
        {
            "quantity": [2.0],
            "unit_price": [100.0],
            "discount": [0.25],
            "order_value": [200.00],
            "discounted_value": [150.00]    
        }
    )

    result = calculate_order_values(orders)

    assert_frame_equal(result, expected)
