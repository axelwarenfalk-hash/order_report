from pathlib import Path

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from order_report.io import load_orders, save_report


def test_load_orders_raises_file_not_found_for_missing_file(
    tmp_path: Path,
) -> None:
    input_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError, match="Datafilen saknas"):
        load_orders(input_path)


def test_load_orders_raises_value_error_for_empty_file(
    tmp_path: Path,
) -> None:
    input_path = tmp_path / "empty.csv"
    input_path.touch()

    with pytest.raises(ValueError, match="Datafilen är tom"):
        load_orders(input_path)


def test_load_orders_reads_csv(tmp_path: Path) -> None:
    expected = pd.DataFrame(
        {
            "order_id": ["O0001", "O0002"],
            "quantity": [2, 3],
        }
    )
    input_path = tmp_path / "orders.csv"
    expected.to_csv(input_path, index=False)

    result = load_orders(input_path)

    assert_frame_equal(result, expected)


def test_save_report_writes_csv_without_index(tmp_path: Path) -> None:
    report = pd.DataFrame(
        {
            "metric": ["total_sales", "order_count"],
            "value": [250.0, 2.0],
        }
    )
    output_path = tmp_path / "reports" / "overview.csv"

    save_report(report, output_path)

    assert output_path.exists()
    saved_report = pd.read_csv(output_path)
    assert_frame_equal(saved_report, report)
