import yfinance as yf
import pandas as pd
from src.utils import logger

def add_moving_average(df, window=20):

    logger.info("Data Preprocessing Started")
    df['MA'] = df['Close'].rolling(window=window).mean()
    logger.info("Data Preprocessing Ended Successfully")
    return df
