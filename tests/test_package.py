import order_report


def test_public_api_exports_are_available() -> None:
    expected_exports = {
        "ReportConfig",
        "calculate_order_values",
        "clean_orders",
        "config_logging",
        "create_overview_report",
        "create_returns_report_by",
        "create_sales_report_by",
        "load_orders",
        "run_pipeline",
        "save_report",
        "validate_orders",
    }

    assert set(order_report.__all__) == expected_exports
    assert all(hasattr(order_report, name) for name in expected_exports)
