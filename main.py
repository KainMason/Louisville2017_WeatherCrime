import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
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

# Function to create and display the bar chart in a tile
def show_bar_chart(title, data_df):
    fig, ax = plt.subplots(figsize=(8, 5))
    data_df.plot(kind='bar', ax=ax)
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a Tkinter application
root = tk.Tk()
root.title("Crime Data Analysis")

# Create and display the bar chart of crime types and their counts
crime_type_counts_chart = show_bar_chart('Crime Types', crime_type_counts)

# Create and display the bar chart of crime types grouped by temperature conditions
grouped_df_chart = show_bar_chart('Number of Crimes by Crime Type and Temperature Condition', grouped_df)

# Create and display the pivot table and bar plot showing crime counts by crime type and month
pivot_table_chart = show_bar_chart('Crime Count by Crime Type and Month', pivot_table)

root.mainloop()
