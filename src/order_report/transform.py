import pandas as pd


def clean_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.copy()

    orders["region"] = (
        orders["region"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    orders["product_category"] = (
        orders["product_category"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    orders["returned"] = (
        orders["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )

    orders["quantity"] = pd.to_numeric(
        orders["quantity"], errors="coerce"
    ).fillna(1)

    orders["unit_price"] = pd.to_numeric(
        orders["unit_price"], errors="coerce"
    )
    orders["unit_price"] = orders["unit_price"].fillna(
        orders["unit_price"].median()
    )

    orders["discount"] = pd.to_numeric(
        orders["discount"], errors="coerce"
    ).fillna(0)

    return orders


def calculate_order_values(orders: pd.DataFrame) -> pd.DataFrame:

    orders = orders.copy()

    orders["order_value"] = (
        orders["quantity"] * orders["unit_price"]
    )

    orders["discounted_value"] = (
        orders["order_value"] * (1 - orders["discount"])
    )

    return orders