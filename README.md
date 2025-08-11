
# Project: Supplier Data Integration & Analysis Pipeline

## Objective
Parts Avatar is looking to integrate a new auto parts supplier to expand our inventory. We have received a sample data feed (`supplier_feed.csv`) containing their product stock levels and costs, along with a separate file (`product_metadata.csv`) that maps supplier part IDs to our internal product information.

Our goal is to build a reliable, automated pipeline to process this data, load it into a database, and perform an initial analysis to determine the viability of this supplier.

## The Challenge
The supplier's data feed is notoriously unreliable. It contains inconsistencies, missing values, and mixed data types that must be handled gracefully. Your task is to design and implement a small-scale ETL (Extract, Transform, Load) pipeline that is robust enough to handle these issues and produce clean, analytics-ready data.

## Datasets
* `data/supplier_feed.csv`: The raw, messy data from the new supplier.
* `data/product_metadata.csv`: Maps the supplier's parts to our internal system.

## Your Tasks
1.  **Extract & Transform:**
    * Write a Python script (`src/transform_data.py`) to read, clean, and standardize the `supplier_feed.csv` data.
    * **Problem-Solving:** You must make and document key decisions. For example: How do you handle "Low Stock"? How do you impute missing `cost_price` values? What is your strategy for standardizing the messy `entry_date` column? Justify your choices in this README.

2.  **Load:**
    * Create a simple SQLite database (`parts_avatar.db`).
    * Load the cleaned supplier data and the product metadata into two separate tables in the database. Ensure the data types are correct and consider setting up primary keys.

3.  **Analyze & Visualize:**
    * Write a Python script or a Jupyter Notebook to query the SQLite database and answer the following business questions:
        * What is the average cost price per product category?
        * Which top 5 parts have the highest stock levels right now?
        * How has the number of new parts entries from this supplier changed over time (on a monthly basis)?
    * Create at least two clear and informative visualizations (e.g., using Matplotlib, Seaborn, or Plotly) to present your findings.

4.  **Documentation:**
    * Update this `README.md` file to be a comprehensive report of your project.
    * Explain your data cleaning strategies and justify your decisions.
    * Describe the schema of your database tables.
    * Present your findings from the analysis, including the visualizations you created.
    * Provide clear instructions on how to run your entire pipeline from start to finish.

## Evaluation Criteria
* **Problem-Solving:** The logic and justification behind your data cleaning and transformation decisions.
* **Python & SQL Proficiency:** The quality, efficiency, and organization of your code.
* **Data Engineering Concepts:** The structure and robustness of your ETL pipeline.
* **Data Visualization & Communication:** The clarity and impact of your analysis and visualizations in the README report.

## Disclaimer: Data and Evaluation Criteria
Please be advised that the datasets utilized in this project are synthetically generated and intended for illustrative purposes only. Furthermore, they have been significantly reduced in terms of sample size and the number of features to streamline the exercise. They do not represent or correspond to any actual business data. The primary objective of this evaluation is to assess the problem-solving methodology and the strategic approach employed, not necessarily the best possible tailored solution for the data. 
