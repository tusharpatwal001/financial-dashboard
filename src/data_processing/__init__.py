import yfinance as yf
import pandas as pd
from src.utils import logger


# ---------------------------
# Indicators
# ---------------------------

def add_moving_average(df, window=20):

    logger.info("Data Preprocessing Started")
    df['MA'] = df['Close'].rolling(window=window).mean()
    logger.info("Data Preprocessing Ended Successfully")
    return df


def add_bollinger_bands(df, window=20):
    rolling_mean = df['Close'].rolling(window=window).mean()
    rolling_std = df['Close'].rolling(window=window).std()

    df['BB_MA'] = rolling_mean
    df['BB_Upper'] = rolling_mean + (rolling_std * 2)
    df['BB_Lower'] = rolling_mean - (rolling_std * 2)
    return df


def add_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df


def add_macd(df, short=12, long=26, signal=9):
    df['EMA_short'] = df['Close'].ewm(span=short, adjust=False).mean()
    df['EMA_long'] = df['Close'].ewm(span=long, adjust=False).mean()
    df['MACD'] = df['EMA_short'] - df['EMA_long']
    df['Signal'] = df['MACD'].ewm(span=signal, adjust=False).mean()
    return df
