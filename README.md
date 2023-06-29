
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
Place the crime2017.csv and weather.csv files in the same directory as the script file crime_analysis.py. Alternatively, you can modify the file paths in the script to match the locations of your files.
Usage
To run the script and generate the crime analysis visualization:

Open a terminal or command prompt.

Navigate to the directory containing the script file crime_analysis.py and the data files.

Run the following command:

shell
Copy code
python crime_analysis.py
This will execute the script and display a tkinter window showing the crime incidents by type and temperature in 2017.

Customization
You can customize the visualization and analysis by modifying the code:

Adjust the figure size and other visual aspects of the plot by modifying the fig, ax parameters in the script.
Change the filtering criteria for temperatures by modifying the threshold values in the high_temp_data and low_temp_data lines.
Modify the labels and title of the plot by changing the corresponding strings in the ax.set_xlabel, ax.set_ylabel, and ax.set_title lines.
Customize the rotation of the x-axis labels by modifying the value in the ax.tick_params line.
Licens
