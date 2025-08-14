# Project: Supplier Data Integration & Analysis Pipeline

Welcome to my submission for the Supplier Data Integration & Analysis Pipeline task!

## Installation

## Assumptions

Here are some assumptions I made for this task:

Task 1.

- The `cost_price` column only has three different types of values: a number, NaN, or a string with a dollar sign in front of a number

- The dates that are of the form `03/04/24` are `mm/dd/yy` (month first)

Task 2.

- Assuming `product_metadata.csv` does not require processing/cleaning

- Assuming `part_id` can be used as a primary key for the `product_metadata` table (i.e. only a single row per `part_id` are present)

Task 3.

- Assuming `category` names are uniform. For example, a Filter will always have a category of `Filters` and not `Filter`

## Figures

Histogram of non-numeric stock levels in the supplier feed
![Histogram of non-numeric stock levels in the supplier feed](figures/nonnumeric_stock_levels_histogram.png)
