import pandas as pd
from datetime import datetime, timedelta

# Load the scraped data
scraped_data = pd.read_csv("nagpur_weather.csv")

# Generate the complete date range
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 12, 31)
all_dates = pd.date_range(start=start_date, end=end_date).strftime("%Y-%m-%d").tolist()

# Extract scraped dates
scraped_dates = scraped_data['datetime'].tolist()  # Adjust column name if different

# Find missing dates
missing_dates = list(set(all_dates) - set(scraped_dates))
missing_dates.sort()

# Print or save the missing dates
print("Missing dates:", missing_dates)
