## Goal :
Reproduce a recent bar plot "Killer Quakes" from Sept 10, TOI (see attached). The source of the data has been mentioned to be https://ourworldindata.org. The goal is to acquire the data https://ourworldindata.org and plot an equivalent bar chart from the acquired data and verify the match (and mismatch if any).

## Details:  
The plot uses data from two different sets of  data available at https://ourworldindata.org. One dataset is available as a Webpage Table in https://ourworldindata.org/the-worlds-deadliest-earthquakes.
The other set is available form a natural disaster dataset available in the OurWorldInData servers.

## Data Acquisition:
-  Use pandas `read_html` method to Web Scrape data from https://ourworldindata.org/the-worlds-deadliest-earthquakes. See examples from https://pandas.pydata.org/docs/user_guide/io.html#html. (See the practice session on Wednesday, Sept 20, evening class). Note that read_html returns an array of tables.
- Acquire the natural disaster dataset using owid-catalog API (see https://pypi.org/project/owid-catalog/ and https://github.com/owid/owid-catalog-py).
You must install owid-catalog and import catalog as `from owid import catalog` before 
use `catalog.find('natural_disasters')` will return you a table (dataframe) listing two datasets. Choose the `natural_disasters_yearly` dataset, the 2nd row in the table. 
(ex: `data.iloc[1].load()` )

## Data Preparation and Data Cleaning:
-  From the owid catalog acquired data choose only those rows that correspond to earthquakes and are for years 2020 or higher.
-  Remove data rows to "World", "European Union (27)" and Continents. (you may list the continents manually or use a python API such as a-world-of-countries to get_continent_list. See https://pypi.org/project/a-world-of-countries/). Additionally  remove the names from the following list: ['Upper-middle-income countries', 'Lower-middle-income countries', 'High-income countries', 'Low-income countries'].
-  Sort the resulting data frame in decreasing order, pick only 5 rows from the data frame to concatenate with the scraped dataset. Before concatenating make sure that both the data frames have the same column names.
-  To avoid duplication of rows, use pandas dataframe method
 `drop_duplicates(subset=["country", "year"])`. 


## Data Visualization:
Use bar plot method of Plotly express or Seaborn to plot horizontal bar plots.
Note that you need to set the color (for Plotly), hue for (seaborn) to assign different hues to distinguish between bars before 2020 and the others.

---
Find attached the sample plot.
Notice a couple of mismatches. The mismatches may be attributed to manual addition of some of the data and to possible typographic error (in at least one case) during manual data addition.

---
## Additional comments:
- Use  `catalog.find('natural_disasters')`   after  `from owid import catalog`
It seems `owid.catalog.find(...)` after `import owid` does not work.
I will edit the instructions as well

- The dataframe from OWID comes with multicolumn indices. You can access rows by using a tuple as index. 
For ex: `df.loc[("Afghanistan", 1956, "earthquake")]` will return a row where the index is a tuple of three elements - country, year and disaster type.
However, you may find handling the required subsequent operations by simply using .reset_index. The index columns become independent columns.

-  `drop_duplicates(...)` looks for exact match. For example " China" and "China" are not duplicates.

- Apart from "World", continents, "European Union (27)", there are another few rows we do not want to include. They are    ['Upper-middle-income countries', 'Lower-middle-income countries', 'High-income countries', 'Low-income countries']. 
You should remove them as well. After you get rid of all those rows, you should sort them by total_deaths data, and keep only the top 5 rows to merge with the scrapped table of 10 rows.

- Remember that the Scraped table already contains 10 top killer earthquakes. You will no get any earthquakes that killed more people from the OWID acquired data. From this latter table you need data for years 2000 and higher. 
So, sort only after discarding all the rows that do not belong to countries and those rows that correspond to year less that 2020 and keep only 5 rows to merge.

- Sir could you give a clarification whether we need to take owid data for (2020 or higher) or (2000 and higher)?
It should be 2000 and higher as the newspaper says. Looks like I said 2020 in my previous posting by mistake.
