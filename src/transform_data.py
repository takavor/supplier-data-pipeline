import pandas as pd
import matplotlib.pyplot as plt

# import supplier feed data
supplier_df = pd.read_csv('data/supplier_feed.csv')
print(f'Head of supplier feed:\n{supplier_df.head(10)}')
print(f'\nSupplier feed column data types:\n{supplier_df.dtypes}')

# check for missing values
supplier_na_counts = supplier_df.isna().sum()
print(f'\nNumber of missing values:\n{supplier_na_counts}') # stock level and cost price have missing values (to be addressed later)

# get supplier feed data value counts to see the different kinds of values we have
stock_level_counts = supplier_df['stock_level'].value_counts()
print(f'Counts of stock levels in the supplier feed:{stock_level_counts}')
print('-'*100)

# notice that there are non-numeric values for stock counts
# let's get all non-numeric values and their counts
# get indices with non-numeric values for stock level
nonnumeric_stock_level_idx = pd.to_numeric(stock_level_counts.index, errors='coerce').isna() # non-numeric rows are NaN
nonnumeric_stock_level_counts = stock_level_counts[nonnumeric_stock_level_idx] # mask at indices
print(f'Counts of non-numeric stock levels:\n{nonnumeric_stock_level_counts}')
print('-'*100)

# there are only 5 different such categories, which can be grouped into 2: low stock and unavailable
# we must map those to appropriate stock levels
# unavailable is easy (means stock of 0)
# for low stock, we can create a histogram of stock values, see what numbers represent low stock, and set it to be near those values
numeric_stock_levels = stock_level_counts[~nonnumeric_stock_level_idx]

plt.figure(figsize=(12, 8))
plt.hist(numeric_stock_levels, bins=100)
plt.xlabel('Stock level')
plt.ylabel('Count')
plt.show()

# lowest stock levels are concentrated around 30, so I'm choosing 30 as the low stock value
# create new df
supplier_df_cleaned = supplier_df.copy()

# replace non-numeric stock levels
stock_levels_map = {
    'LOW': 30,
    'Low Stock': 30,
    'UNAVAILABLE': 0,
    'low stock': 30,
    'Out of Stock': 0
}

supplier_df_cleaned['stock_level'] = supplier_df_cleaned['stock_level'].replace(stock_levels_map)

print(f'Supplier feed with cleaned stock levels:\n{supplier_df_cleaned.head(10)}')