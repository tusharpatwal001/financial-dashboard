import plotly.graph_objs as go
from src.utils import logger


# ---------------------------
# Plot Functions
# ---------------------------


def plot_price(df, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Close'))
    if 'MA' in df:
        fig.add_trace(go.Scatter(x=df.index, y=df['MA'], name='Moving Avg'))
    if 'BB_Upper' in df:
        fig.add_trace(go.Scatter(
            x=df.index, y=df['BB_Upper'], name='Upper BB', line=dict(dash='dot')))
        fig.add_trace(go.Scatter(
            x=df.index, y=df['BB_Lower'], name='Lower BB', line=dict(dash='dot')))
    fig.update_layout(title=f"{ticker} Price",
                      xaxis_title="Date", yaxis_title="Price (USD)")
    return fig


def plot_volume(df, ticker):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name="Volume"))
    fig.update_layout(title=f"{ticker} Volume",
                      xaxis_title="Date", yaxis_title="Volume")
    return fig


def plot_rsi(df, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, y=df['RSI'], name="RSI", line=dict(color="orange")))
    fig.add_hline(y=70, line_dash="dash", line_color="red")
    fig.add_hline(y=30, line_dash="dash", line_color="green")
    fig.update_layout(title=f"{ticker} RSI (14)",
                      xaxis_title="Date", yaxis_title="RSI")
    return fig


def plot_macd(df, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], name="MACD"))
    fig.add_trace(go.Scatter(x=df.index, y=df['Signal'], name="Signal"))
    fig.update_layout(title=f"{ticker} MACD",
                      xaxis_title="Date", yaxis_title="MACD")
    return fig
