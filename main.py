import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Read the crime.csv file with specified data types and low_memory=False
crime_data = pd.read_csv('crime2017.csv', dtype={'ID': str}, low_memory=False)

# Read the weather.csv file
weather_data = pd.read_csv('weather.csv')

# Convert the date columns to the appropriate data type
crime_data['DATE_OCCURED'] = pd.to_datetime(crime_data['DATE_OCCURED']).dt.date
weather_data['date'] = pd.to_datetime(weather_data['date']).dt.date

# Merge the datasets based on the date column
merged_data = pd.merge(crime_data, weather_data, left_on='DATE_OCCURED', right_on='date', how='inner')

# Filter the merged dataset for the year 2017
merged_data_2017 = merged_data[pd.to_datetime(merged_data['DATE_OCCURED']).dt.year == 2017]

# Separate the data into two groups based on temperature
high_temp_data = merged_data_2017[merged_data_2017['high'] >= 50]
low_temp_data = merged_data_2017[merged_data_2017['high'] < 50]

# Calculate the count of each crime type for high temperatures (>= 50)
high_temp_counts = high_temp_data['CRIME_TYPE'].value_counts()

# Calculate the count of each crime type for low temperatures (< 50)
low_temp_counts = low_temp_data['CRIME_TYPE'].value_counts()

# Combine the counts for each crime type
combined_counts = pd.concat([high_temp_counts, low_temp_counts], axis=1, keys=['High Temperature', 'Low Temperature'])

# Create a Tkinter window
window = tk.Tk()
window.title('Crime Incidents by Type and Temperature in 2017')

# Create a Figure and Axes for the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bar chart on the Figure and Axes
combined_counts.plot(kind='bar', ax=ax)
ax.set_xlabel('Crime Type')
ax.set_ylabel('Number of Incidents')
ax.set_title('Crime Incidents by Type and Temperature in 2017')
ax.tick_params(axis='x', rotation=90)
ax.legend()

# Create a FigureCanvasTkAgg widget and add it to the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
tk.mainloop()
