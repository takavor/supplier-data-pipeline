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
print('-'*100)

# let's now take a look at cost prices
print(f'Supplier feed cost prices:\n{supplier_df_cleaned.head(10)['cost_price']}')

# we have a mix of instances: some are numbers, some are NaN, and some are strings with a dollar sign followed by a number
# remove dollar signs
supplier_df_cleaned['cost_price'] = supplier_df_cleaned['cost_price'].str.replace('$', '')

# convert cost prices back to numeric types
supplier_df_cleaned['cost_price'] = pd.to_numeric(supplier_df_cleaned['cost_price'])

print(f'\nCost prices with $ stripped:\n{supplier_df_cleaned['cost_price'].head(10)}')
print('-'*100)

# idea: we can replace NaNs by the average of the cost prices for the given stock over time

avg_cost_prices_per_stock = supplier_df_cleaned.groupby('part_id')['cost_price'].mean()
print(f'Avg cost prices per stock:\n{avg_cost_prices_per_stock}')

supplier_df_cleaned['cost_price'] = supplier_df_cleaned['cost_price'].fillna(supplier_df_cleaned['part_id'].map(avg_cost_prices_per_stock))
print(f'\nCost prices with NaN filled:\n{supplier_df_cleaned['cost_price'].head(10)}')
print('-'*100)

# edge case: part could have NaN for all of its cost prices
# check if there are still NaN
print(f'Number of NaN values in cleaned cost prices:\n{supplier_df_cleaned['cost_price'].isna().sum()}') # it's 0!

# now for entry date, we must see the different kinds of formats we have
print(f'Entry dates:\n{supplier_df_cleaned.head(10)['entry_date']}')

# use pandas to_datetime to convert all to a uniform format
# assuming month is first for cases like 03/04/24 (view README)
supplier_df_cleaned['entry_date'] = pd.to_datetime(supplier_df_cleaned['entry_date'], format='mixed', dayfirst=False)
print(f'\nCleaned entry dates:\n{supplier_df_cleaned['entry_date']}')

# check if there are NaT (not a time) values
print(f'\nCount of NaT values:\n{supplier_df_cleaned['entry_date'].isna().sum()}')
