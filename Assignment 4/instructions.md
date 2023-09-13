## Goal: 

Live access NSE market data using nsepython. Acquire and compare the relative changes of a few NIFTY index data over the last 9 yrs.

## Detail:  

Acquire and create visual comparison of percent changes of the following 3 index funds over the last 9 years.
- NIFTY 50
- NIFTY BANK
- NIFTY IT

## Data Acquisition Component:

Install nsepython package and use its index_total_returns for the above mentioned funds 
(symbols of the funds are as written above) to acquire historical index data for the following period (See https://unofficed.com/nse-python/documentation/ for details).

- Start Date: "01-May-2014"
- End Data: "10-Sept-2023"

## Data Cleaning and Data Preparation Component:

- For every acquired timeseries index data: Compute the relative percent change in the index return value from the start date. 

- It will require you to apply the following calculation at every date:

> 100*(Return at the date of interest -  Return at the start date)/Return at the start date
- Combine the updated index data to create a single data frame. Rename the columns to distinguish the relative percent change data for the three index funds from each other. 

## Data Visualization: 

- Use Plotly Express or Seaborn to create line plots of on a single chart.

- See sample plots (attached)