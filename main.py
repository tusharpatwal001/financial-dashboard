from src.data_ingestion import get_data
from src.data_processing import add_moving_average
from src.utils import logger
from src.plots import plot_price

ticker = "HUM"

result = get_data(ticker, "2025-01-01", "2025-04-01")
preprocessed_data = add_moving_average(result)

print(plot_price(preprocessed_data, ticker))
