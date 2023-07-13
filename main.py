import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the GUI window
root = tk.Tk()
root.title('Crime / Weather 2017 Data Visualization')
root.geometry('800x600')

# Create a function to display the bar chart of crime types
def show_crime_types_chart():
    # Create a new frame for the plot
    frame = ttk.Frame(scrollable_frame)
    frame.pack(pady=10)

    # Add text above the plot
    label = ttk.Label(frame, text='Crime Types')
    label.pack()

    # Create the plot
    plt.figure(figsize=(10, 6))
    crime_type_counts.plot(kind='bar')
    plt.xlabel('Crime Type')
    plt.ylabel('Count')
    plt.title('Crime Types')

    # Create a canvas for embedding the plot
    canvas = FigureCanvasTkAgg(plt.gcf(), master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a function to display the bar chart of crime types and temperature conditions
def show_crimes_by_temperature_chart():
    # Create a new frame for the plot
    frame = ttk.Frame(scrollable_frame)
    frame.pack(pady=10)

    # Add text above the plot
    label = ttk.Label(frame, text='Crimes by Temperature')
    label.pack()

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    grouped_df.plot(kind='bar', ax=ax)
    plt.xlabel('Crime Type')
    plt.ylabel('Number of Crimes')
    plt.title('Number of Crimes by Crime Type and Temperature Condition')
    plt.legend(['Below 50', '50 and Above'])
    plt.xticks(rotation=45)
    plt.grid(True)

    # Create a canvas for embedding the plot
    canvas = FigureCanvasTkAgg(plt.gcf(), master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a function to display the pivot table and bar plot
def show_crime_count_by_month():
    # Create a new frame for the plot
    frame = ttk.Frame(scrollable_frame)
    frame.pack(pady=10)

    # Add text above the plot
    label = ttk.Label(frame, text='Crime Count by Month')
    label.pack()

    # Create the plot
    pivot_table.plot(kind='bar', figsize=(12, 6))
    plt.xlabel('Crime Type')
    plt.ylabel('Count')
    plt.title('Crime Count by Crime Type and Month')
    plt.legend(title='Month', bbox_to_anchor=(1, 1))
    plt.xticks(rotation=45)
    plt.grid(True)

    # Create a canvas for embedding the plot
    canvas = FigureCanvasTkAgg(plt.gcf(), master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a scrollable frame
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

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

# Call the functions to show the plots in the GUI
show_crime_types_chart()
show_crimes_by_temperature_chart()
show_crime_count_by_month()

root.mainloop()