# Data Acquisition and Inspection: 
Read only the Gender and Height ata columns from the attached Excel file. 
> `df = pd.read_excel(<filename>, usecols=<list of columns>)`

- You must install openpyxl package before using Pandas read_excel method. (ex: pip install openpyxl)
- Check the exact name of the Height data column.
- You may use Pandas function to change the column names to shorten them for convenient of use. 
(For example: `df.rename(columns={"A xxxx": "a"})` 
- Note: rename method will change the name of only those columns you specify. Remember that like most pandas methods, rename does not update the original dataframe unless you use inplace=True, or assign it to the same or a different data frame.)
- However, the original column name must be used as the label of the axis.

# Data Cleaning:
- The gender column data may have some non-uniformity on the name.  
- For example: "Male" may appear as "male" in some rows. Use Pandas function to resolve that problem.

# Data Visualization:
Use either of Plotly Express,  Seaborn to create the following distribution plots :
- Histogram pot
- Box plot
- Violin plot

Note that the plots must show distributions of the Male and Female heights separately (may overlap) on the same plot.

---

## Note :
This dataset contains the height, weight and 4 fingerprint measurements (length, width, area and circumference), collected from 200 participants. This data was collected with the intention of performing regression analysis to asses whether a significant relationship exists between fingerprint size and physical stature. The dataset was downloaded from https://repository.lboro.ac.uk/articles/dataset/Height_weight_and_fingerprint_measurements_collected_from_200_participants/7539206