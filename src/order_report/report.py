import pandas as pd


def create_overview_report(orders: pd.DataFrame) -> pd.DataFrame:
    
    total_sales = round(orders["discounted_value"].sum(), 2)
    number_of_orders = orders["order_id"].nunique()
    number_of_returns = int(orders["returned"].sum())

    overview = pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )

    return overview


def create_sales_report_by(
    orders: pd.DataFrame,
    group_column: str,
) -> pd.DataFrame:
    sales_report = (
        orders.groupby(group_column, as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    sales_report["total_sales"] = sales_report["total_sales"].round(2)
    sales_report["return_rate"] = (
        sales_report["returns"] / sales_report["order_count"]
    ).round(3)

    sales_report = (
        sales_report.sort_values("total_sales", ascending=False)
        .reset_index(drop=True)
    )

    return sales_report


def create_returns_report_by(
    orders: pd.DataFrame,
    group_column: str,
) -> pd.DataFrame:
    returns_report = (
        orders.groupby(group_column, as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    returns_report["return_rate"] = (
        returns_report["returns"] / returns_report["order_count"]
    ).round(3)

    returns_report = (
        returns_report.sort_values("return_rate", ascending=False)
        .reset_index(drop=True)
    )

    return returns_report
