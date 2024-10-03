# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:24:03 2024

@author: angad
"""

Q10

import pandas as pd

# 1. Read the CSV file
file_path = 'D://Semester 1//Computing for Data Science//Assignments//hw2//covid.csv'  # Replace with your actual CSV file path
df = pd.read_csv(file_path)

# 2. Define the list of thresholds for Active cases
thresholds = [500, 1000, 5000]

# 3. Loop through each threshold and filter, group, and compute averages
for threshold in thresholds:
    print(f"\nCountries with more than {threshold} Active cases:")

    # Filter countries where Active cases are more than the current threshold
    filtered_df = df[df['Active'] > threshold]
    
    # Group by Country and calculate the mean of Confirmed and Deaths
    grouped_df = filtered_df.groupby('Country').agg(
        Avg_Confirmed=('Confirmed', 'mean'),
        Avg_Deaths=('Deaths', 'mean')
    ).reset_index()
    
    # Print the resulting DataFrame
    print(grouped_df)
