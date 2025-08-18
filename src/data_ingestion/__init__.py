import yfinance
import pandas as pd
from src.utils import logger


def get_data(ticker, start_date, end_date):
    logger.info("Data Ingestion Started")
    df = yfinance.download(ticker, start_date, end_date)
    logger.info("Data Ingestion Ended Successfully")
    return df