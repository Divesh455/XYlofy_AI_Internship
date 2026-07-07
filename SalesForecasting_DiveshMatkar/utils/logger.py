import logging

from config import LOG_DIR

LOG_FILE = LOG_DIR / "sales_forecasting.log"

logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s",

    datefmt="%d-%m-%Y %H:%M:%S"

)

logger = logging.getLogger("SalesForecasting")