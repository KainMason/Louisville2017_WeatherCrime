
# Crime Analysis: Crime Incidents by Type and Temperature in 2017

This Python script analyzes crime incidents by type and temperature in the year 2017. It uses data from two CSV files, `crime2017.csv` and `weather.csv`, and visualizes the results in a bar chart using matplotlib and tkinter libraries.

## Installation

1. Clone this repository or download the script file `crime_analysis.py`.

2. Ensure that you have the required dependencies installed:
   - pandas
   - matplotlib
   - tkinter

   You can install them using pip:

   ```shell
   pip install pandas matplotlib tkinter
Place the crime2017.csv and weather.csv files in the same directory as the script file main.py. Alternatively, you can modify the file paths in the script to match the locations of your files.
Usage
To run the script and generate the crime analysis visualization:

Open a terminal or command prompt.

Navigate to the directory containing the script file crime_analysis.py and the data files.

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

#Data Dictionary:
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


