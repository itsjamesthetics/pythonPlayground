'''
    Developed by: James Ald Teves
    BS Computer Science

    Instructor: Dr. Chuchi S. Montenegro
    Description: Python Program that can read and manipulate CSV Data
'''

import csv
import pandas as pd

# Function to fill missing values with column average
def fill_missing_with_average(df):
    return df.fillna(df.mean())

# Function to fill missing values using linear interpolation
def fill_missing_with_interpolation(df):
    return df.interpolate()

# Define the input and output file names
input_file = 'Datasamp.csv'
output_file = 'NewDataSet.csv'

try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"File '{input_file}' not found.")
    exit(1)

# Ask the user for filling method
fill_method = input("Choose a method to fill in a missing DATA ((1) Column Average, (2) Linear Interpolation): ")

# Check if the chosen method is valid
if fill_method in ['1', '2']:
    if fill_method == '1':
        # Fill missing values with column averages
        df_filled = fill_missing_with_average(df)
    else:
        # Fill missing values using linear interpolation
        df_filled = fill_missing_with_interpolation(df)

    # Save the modified data to a new CSV file
    df_filled.to_csv(output_file, index = False)
    print(f"Data with missing values filled using method {fill_method} saved to '{output_file}'.")
else:
    print("Invalid choice. Please enter 1 or 2 for the fill method.")