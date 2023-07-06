import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to display the bar chart of crime types
def show_crime_types_chart():
    plt.figure(figsize=(10, 6))
    crime_type_counts.plot(kind='bar')
    plt.xlabel('Crime Type')
    plt.ylabel('Count')
    plt.title('Crime Types')
    plt.show()

# Function to display the bar chart of crime types and temperature conditions
def show_crimes_by_temperature_chart():
    fig, ax = plt.subplots(figsize=(12, 6))
    grouped_df.plot(kind='bar', ax=ax)
    plt.xlabel('Crime Type')
    plt.ylabel('Number of Crimes')
    plt.title('Number of Crimes by Crime Type and Temperature Condition')
    plt.legend(['Below 50', '50 and Above'])
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Function to display the pivot table and bar plot
def show_crime_count_by_month():
    pivot_table.plot(kind='bar', figsize=(12, 6))
    plt.xlabel('Crime Type')
    plt.ylabel('Count')
    plt.title('Crime Count by Crime Type and Month')
    plt.legend(title='Month', bbox_to_anchor=(1, 1))
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Read the crime data from crime2017.csv
crime_df = pd.read_csv('crime2017.csv', dtype={'ZIP_CODE': str})

# Read the weather data from weather.csv
weather_df = pd.read_csv('weather.csv')
# Clean the crime data
crime_df = pd.read_csv('crime2017.csv', dtype={'ZIP_CODE': str})
crime_df = crime_df[crime_df['YEAR_OCCURED'] == 2017.0]



# Clean the crime data
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

# Create the GUI window
root = tk.Tk()
root.title('Crime Data Visualization')
root.geometry('800x600')

# Create a label to explain the purpose of the program
explanation_label = tk.Label(root, text='This program visualizes crime data')
explanation_label.pack(pady=10)

# Create buttons for each chart
crime_types_button = tk.Button(root, text='Crime Types', command=show_crime_types_chart)
crime_types_button.pack()

crimes_by_temperature_button = tk.Button(root, text='Crimes by Temperature', command=show_crimes_by_temperature_chart)
crimes_by_temperature_button.pack()
crime_count_by_month_button = tk.Button(root, text='Crime Count by Month', command=show_crime_count_by_month)
crime_count_by_month_button.pack()

# Create a matplotlib figure and canvas for embedding plots in the GUI
figure = plt.figure(figsize=(8, 6))
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Function to update the embedded plot in the GUI
def update_plot(plot_func):
    figure.clear()
    plot_func()
    canvas.draw()

# Update the embedded plot when the corresponding button is pressed
crime_types_button.config(command=lambda: update_plot(show_crime_types_chart))
crimes_by_temperature_button.config(command=lambda: update_plot(show_crimes_by_temperature_chart))
crime_count_by_month_button.config(command=lambda: update_plot(show_crime_count_by_month))

# Display the GUI window
root.mainloop()