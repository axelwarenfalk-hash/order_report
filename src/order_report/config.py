import logging
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, kw_only=True)
class ReportConfig:
    '''Sökvägar och inställningar som behövs i rapporten'''
    input_path: Path = Path('data/orders.csv')
    output_path: Path = Path('output')


def config_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format=(
            "%(asctime)s | %(levelname)s | "
            "%(name)s | %(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

