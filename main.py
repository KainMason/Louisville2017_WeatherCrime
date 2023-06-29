import pandas as pd
import matplotlib.pyplot as plt

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

# Plot the bar chart
plt.figure(figsize=(10, 6))  # Create a figure with specified size
combined_counts.plot(kind='bar')  # Plot the combined counts as a bar chart
plt.xlabel('Crime Type')  # Set the x-axis label
plt.ylabel('Number of Incidents')  # Set the y-axis label
plt.title('Crime Incidents by Type and Temperature in 2017')  # Set the chart title
plt.xticks(rotation=90)  # Rotate the x-axis tick labels for better readability
plt.legend()  # Show the legend

plt.show()  # Display the chart
