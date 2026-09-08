import logging

from . import ReportConfig, config_logging, run_pipeline


logger = logging.getLogger(__package__)


def main() -> None:
    
    config_logging()
    config = ReportConfig()

    logger.info("Startar orderrapport")
    try:
        run_pipeline(config)
    except Exception:
        logger.exception("Orderrapporten kunde inte skapas")
        raise

    logger.info("Orderrapporten är klar")



if __name__ == "__main__":
    main()
