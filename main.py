from src.data_ingestion import get_data
from src.data_processing import add_moving_average
from src.utils import logger

result = get_data("HUM", "2025-01-01", "2025-04-01")
data_processing = add_moving_average(result)
print(data_processing)