# NYSE Stock Data Collection

This project allows you to get the active listed stocks in NYSE and get all their historical data using the yfinance library.

# Why
The stock data online is usually dated and may not provide the latest data. This will ensure you get the latest historical active stock data.

# Who
If you are in the data science world, this is great to gather data and study stock related problems. 

# How

Make sure you have python3. Please install all the libraries.

The reason why the scripts are split is because each step takes time to finish. If we fail at any step, we can pick up from where it failed. 

Run the scripts in the following order:
- python scrape_nyse.py <num_loops> 
    - Please check [NYSE] to see how many pages there are to scrape (click on LAST and look at the last page number)
- python get_data_per_stock.py <path to scraped stocks file>
    - Path to scraped stocks file should be placed in './data/scraped_stocks' from the previous script unless you move it elsewhere
- python aggregate_stock_sector_data.py
    - This is optional, but if you'd like all the data to be in one csv file, run this script (this will contain all historical data with the stock name and industry/sector that it is in). 

# Contributions

| Name  | Contributions |
| ------------- | ------------- |
| Pranav Lodha  | Developer |
| Wasae Qureshi  | Developer |

[NYSE]: <https://www.nyse.com/listings_directory/stock>