import logging

from .config import ReportConfig
from .io import load_orders, save_report
from .report import create_overview_report, create_returns_report_by, create_sales_report_by
from .transform import calculate_order_values, clean_orders
from .validate import validate_orders


logger = logging.getLogger(__name__)


def run_pipeline(config: ReportConfig) -> None:

    orders = load_orders(config.input_path)

    validate_orders(orders)
    logger.info("Valideringen av orderdata slutfördes")

    orders = clean_orders(orders)
    orders = calculate_order_values(orders)

    overview = create_overview_report(orders)
    sales_by_category = create_sales_report_by(orders, "product_category")
    sales_by_region = create_sales_report_by(orders, "region")
    returns_by_category = create_returns_report_by(orders, "product_category")
    logger.info("Skapade 4 rapporter")

    overview_path = config.output_path / "overview.csv"
    save_report(overview, overview_path)

    sales_by_category_path = config.output_path / "sales_by_category.csv"
    save_report(sales_by_category, sales_by_category_path)

    sales_by_region_path = config.output_path / "sales_by_region.csv"
    save_report(sales_by_region, sales_by_region_path)

    returns_by_category_path = config.output_path / "returns_by_category.csv"
    save_report(returns_by_category, returns_by_category_path)

    logger.info("Alla rapporter sparades i %s", config.output_path)
