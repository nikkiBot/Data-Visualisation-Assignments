### Goal : Create a time-series visualization of  local monthly temperatures over a few years.
### Data Source URL : https://data.telengana.gov.in/dataset/telengana-temperature-data-2013-2017

---

## Data Acquisition component - 

- You may directly download the Maximum and Minimum data sets from the source URL mentioned above or use the following steps to get the datasets as Pandas dataframes.
(see https://data.telangana.gov.in/dataset/62a1cc18-7613-460b-a0b1-4b71c78fa1ce/api)

- Use python api requests and query the metadata from the above mentioned URL as
  
```r = requests.get("https://data.telangana.gov.in/api/1/metastore/schemas/dataset/items/62a1cc18-7613-460b-a0b1-4b71c78fa1ce&quot;)```
```dataInfo = r.json()```

-  Use the two URLs listed in the metadata in the distributions item array of dataInfo to read_csv as
  
```df_max = pd.read_csv(dataInfo["distribution"][0]["downloadURL"])```
```df_min = pd.read_csv(dataInfo["distribution"][1]["downloadURL"])```

---

## Data Preparation and Cleaning component -

- Extract the data rows corresponding to Medchal district and Kapra Mandal from the data frames. 
- You may combine the two rows into a single data frame if it helps in creating the visualization.
  
```df = pd.concat([df_max, df_min], axis=1)``` 
- You may also use the following code to extract the data rows corresponding to Medchal district and Kapra Mandal from the data frames.
  
```df_max = df_max[(df_max["District"] == "MEDCHAL") & (df_max["Mandal"] == "KAPRA")]```
```df_min = df_min[(df_min["District"] == "MEDCHAL") & (df_min["Mandal"] == "KAPRA")]```
- Use Pandas transpose (T) operation to transpose the table columns into rows and rows into columns.
  
```df_max = df_max.T```
```df_min = df_min.T```
- Convert the months and year data to Pandas Datetime format.
  
```df_max.index = pd.to_datetime(df_max.index)```
```df_min.index = pd.to_datetime(df_min.index)```
(see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
(to be discussed in Day 2 of week 4 practice session).

---

## Data Visualization component -

- Create line plots using either of plotly.express and seaborn to show the minimum and maximum temperatures for the months and years available in the dataset.
- Sample Visuals from plotly express and seaborn are attached.
- (Note: Most of the concepts used in this assignments will be covered during the week's practice session.)

