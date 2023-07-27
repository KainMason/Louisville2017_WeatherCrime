import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Read the crime data from crime2017.csv
crime_df = pd.read_csv('crime2017.csv', dtype={'ZIP_CODE': str})

# Read the weather data from weather.csv
weather_df = pd.read_csv('weather.csv')

# Clean the crime data
crime_df = crime_df[crime_df['YEAR_OCCURED'] == 2017.0]
crime_df.dropna(subset=['date'], inplace=True)
crime_df['date'] = pd.to_datetime(crime_df['date'])
crime_df.drop_duplicates(inplace=True)

# Clean the weather data
weather_df.dropna(subset=['date'], inplace=True)
weather_df['date'] = pd.to_datetime(weather_df['date'])
weather_df.drop_duplicates(inplace=True)

# Merge the crime and weather data on the common column 'date'
combined_df = pd.merge(crime_df, weather_df, on='date')

# Calculate crime type counts
crime_type_counts = combined_df['CRIME_TYPE'].value_counts()

# Group the data by crime type and temperature condition
grouped_df = combined_df.groupby(['CRIME_TYPE', combined_df['high'] >= 50]).size().unstack()

# Create a pivot table to summarize crime count by crime type and month
pivot_table = crime_df.pivot_table(index='CRIME_TYPE', columns=crime_df['date'].dt.month_name(), aggfunc='size', fill_value=0)

# Function to create and display the bar chart in a tab
def create_chart_tab(notebook, title, data_df):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=title)
    fig, ax = plt.subplots(figsize=(8, 5))
    data_df.plot(kind='bar', ax=ax)
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a Tkinter application
root = tk.Tk()
root.title("Crime Data Analysis")

# Maximize the window to fill the screen
root.state('zoomed')

# Create a tabbed interface
notebook = ttk.Notebook(root)

# Create and display the Home tab
home_frame = ttk.Frame(notebook)
notebook.add(home_frame, text='Home')

# Project information for the Home tab
project_title_label = ttk.Label(home_frame, text="Louisville 2017 Crime and Weather Analysis", font=("Helvetica", 18, "bold"))
project_title_label.pack(pady=10)
project_purpose_label = ttk.Label(home_frame, text="Purpose: The purpose of this project is to analyze the crime data "
                                                  "from Louisville in 2017 and understand its relationship with "
                                                  "weather conditions.", font=("Helvetica", 12))
project_purpose_label.pack(pady=5)

# Information about the graphs for the Home tab
graphs_info_label = ttk.Label(home_frame, text="Graphs Information:\n\n"
                                               "1. Crime Types: This bar chart displays the count of each crime type "
                                               "recorded in Louisville in 2017.\n\n"
                                               "2. Number of Crimes by Crime Type and Temperature Condition: This "
                                               "bar chart shows the number of crimes for each crime type based on "
                                               "temperature conditions (below 50°F (FALSE) and 50°F and above(TRUE)).\n\n"
                                               "3. Crime Count by Crime Type and Month: This bar chart summarizes "
                                               "the crime count for each crime type on a month-wise basis.", font=("Helvetica", 12))
graphs_info_label.pack(pady=5)

# Create and display the chart tabs
create_chart_tab(notebook, 'Crime Types', crime_type_counts)
create_chart_tab(notebook, 'Number of Crimes by Crime Type and Temperature Condition', grouped_df)
create_chart_tab(notebook, 'Crime Count by Crime Type and Month', pivot_table)

# Create the Conclusion tab
conclusion_frame = ttk.Frame(notebook)
notebook.add(conclusion_frame, text='Conclusion')

# Analyze data and provide conclusion
conclusion_text = (
    "Conclusion:\n\n"
    "Based on the analysis of the crime data from Louisville in 2017 and its correlation with weather conditions, "
    "we observe the following:\n\n"
    "1. Crime Types Occurrence: Most crime types occur more frequently during cooler temperatures (below 50°F) "
    "compared to temperatures at or above 50°F. The exceptions are certain crime types, such as arson, which may have "
    "unique factors influencing their occurrences.\n\n"
    "2. Seasonal Variations: We also notice some seasonal variations in crime counts, with certain crime types "
    "peaking during specific months. This information could be valuable for law enforcement and city planning.\n\n"
    "Please note that this analysis is based on the data available for the year 2017, and there could be other "
    "factors that may influence crime rates. Further research and analysis may be necessary to gain deeper insights."
)

conclusion_label = ttk.Label(conclusion_frame, text=conclusion_text, font=("Helvetica", 12))
conclusion_label.pack(pady=10)

notebook.pack(fill=tk.BOTH, expand=1)

root.mainloop()
