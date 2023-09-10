import pandas as pd

# Create the original dataframe
data = {
    'Jun-13': [(33.8, 24.6)],
    'Jul-13': [(29.5, 23.5)],
    'Aug-13': [(29.0, 22.9)],
    'Sep-13': [(33.1, 22.9)],
    'Oct-13': [(32.5, 21.5)],
    'Nov-13': [(30.1, 14.2)],
    'Dec-13': [(30.0, 10.6)]
}

combined_df = pd.DataFrame(data)

# Create a new dataframe with multi-level indexing
new_df = pd.DataFrame()

for column in combined_df.columns:
    min_val, max_val = zip(*combined_df[column].tolist())
    new_df[(column, 'min')] = min_val
    new_df[(column, 'max')] = max_val

# Add multi-level indexing
new_df.columns = pd.MultiIndex.from_tuples(new_df.columns, names=['Month', 'Min/Max'])

print(new_df)
