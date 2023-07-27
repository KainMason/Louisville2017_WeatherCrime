
# Crime Analysis: Crime Incidents by Type and Temperature in 2017

This Python script analyzes crime incidents by type and temperature in the year 2017. It uses data from two CSV files, `crime2017.csv` and `weather.csv`, and visualizes the results in a bar chart using matplotlib and tkinter libraries.

## Installation

1. Clone this repository 
2. run `main.py`.

3. Ensure that you have the required dependencies installed:
   - pandas
   - matplotlib
   - tkinter

  ## using gui
  first tab will direct you to each visualization
  click between each tab to view and the final tab for my conclusion

## Project Plan

### Loading Data:
1. Read two CSV files: one for historical weather data and the other for crime reports in Louisville.

### Data Cleaning and Operation:
1. Clean and preprocess the data, ensuring consistency in formatting and resolving any inconsistencies between the datasets.
2. Merge the datasets using pandas merge or create a new dataset with combined attributes/columns.
3. Perform necessary data transformations, feature engineering, or calculations on the merged dataset.

### Data Visualization and Presentation:
1. Create three visualizations using matplotlib, seaborn, or other plotting libraries.
2. Consider using additional tools like Tableau or pandas pivot table for summarizing the data.
3. Design the visualizations to be easily understandable by non-technical audiences.

### Best Practices:
1. Create Data Dictionary and put it in readme

## Interpretation of Data:
1. Focus on clear communication skills in the project documentation.
2. Provide insights into the coding decisions and their relevance to the project.
3. Make the project easily understandable for non-technical users.

# Data Dictionary:
## Weather.csv
| Variable | Description                               | Data Type |
|----------|-------------------------------------------|-----------|
| date     | The date of the weather record             | Date      |
| high     | The highest temperature recorded           | Numeric   |
| events   | Describes weather events (e.g., rain, fog)  | String    |

## crime2017.csv
| Variable        | Description                                              | Data Type |
|-----------------|----------------------------------------------------------|-----------|
| Unnamed: 0      | Index of the crime record                                | Numeric   |
| INCIDENT_NUMBER | Unique identifier for each incident                       | String    |
| DATE_REPORTED   | Date when the incident was reported                       | DateTime  |
| date            | Date when the incident occurred                          | DateTime  |
| UOR_DESC        | Uniform Offense Reporting (UOR) description              | String    |
| CRIME_TYPE      | Type of crime                                            | String    |
| NIBRS_CODE      | National Incident-Based Reporting System (NIBRS) code     | String    |
| UCR_HIERARCHY   | Uniform Crime Reporting (UCR) hierarchy code             | String    |
| ATT_COMP        | Status of the crime (e.g., completed, attempted)          | String    |
| LMPD_DIVISION   | LMPD division where the crime occurred                   | String    |
| LMPD_BEAT       | LMPD beat where the crime occurred                       | Numeric   |
| PREMISE_TYPE    | Type of premises where the crime occurred                | String    |
| BLOCK_ADDRESS   | Block-level address where the crime occurred             | String    |
| CITY            | City where the crime occurred                            | String    |
| ZIP_CODE        | ZIP code where the crime occurred                        | String    |
| ID              | Unique identifier for each crime record                   | Numeric   |
| Time To Report in Days | Time elapsed between the incident and its reporting (in days) | Numeric   |
| YEAR_OCCURED    | Year when the incident occurred                          | Numeric   |


The project meets the requirements as follows:

**Loading Data:**
The code reads two CSV files: one for historical weather data (`weather.csv`) and the other for crime reports in Louisville (`crime2017.csv`).

**Data Cleaning and Operation:**
The code performs data cleaning for both the weather and crime datasets by dropping NaN values, converting date columns to datetime format, and removing duplicate entries.
It then merges the crime and weather datasets using pandas' `merge` function based on the common column 'date'.
The code calculates crime type counts, groups the data by crime type and temperature condition, and creates a pivot table summarizing crime counts by crime type and month.

**Data Visualization and Presentation:**
The code creates three visualizations using matplotlib:

1. A bar chart of crime types and their counts (`crime_type_counts`).
2. A bar chart of crime types grouped by temperature conditions (below 50°F and 50°F and above) (`grouped_df`).
3. A bar chart of crime counts by crime type and month using a pivot table (`pivot_table`).

The charts are designed with clear labeling for easy understanding by non-technical audiences. The x-axis represents categories (crime types), and the y-axis represents counts of crimes. The charts have appropriate titles, axis labels, and grid lines for better presentation.

While the code uses pandas' pivot table for summarizing crime data, it doesn't involve additional tools like Tableau. However, pandas pivot table effectively summarizes the data, and the resulting chart presents crime counts by crime type and month in an easily understandable format.

Overall, the code successfully loads, cleans, and merges the datasets, performs necessary data operations, and creates visualizations that are suitable for non-technical audiences to comprehend the relationship between crime types and weather conditions in Louisville for the year 2017.

**BEST PRACTICES**
1. data dictionary and .readme file

**Conclusion:**

Based on the analysis of the crime data from Louisville in 2017 and its correlation with weather conditions, we observe the following:

1. **Crime Types Occurrence:** Most crime types occur more frequently during cooler temperatures (below 50°F) compared to temperatures at or above 50°F. The exceptions are certain crime types, such as arson, which may have unique factors influencing their occurrences.

2. **Seasonal Variations:** We also notice some seasonal variations in crime counts, with certain crime types peaking during specific months. This information could be valuable for law enforcement and city planning.

Please note that this analysis is based on the data available for the year 2017, and there could be other factors that may influence crime rates. Further research and analysis may be necessary to gain deeper insights.
